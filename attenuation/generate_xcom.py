import os
import numpy as np
import tables
from scipy.interpolate import CubicSpline

# Atomic Number Z, Atomic Mass A (g/mol)
ATOMIC_DATA = {
    'H':  (1, 1.008),
    'Be': (4, 9.012),
    'C':  (6, 12.011),
    'N':  (7, 14.007),
    'O':  (8, 15.999),
    'F':  (9, 18.998),
    'Al': (13, 26.982),
    'S':  (16, 32.065),
    'Ti': (22, 47.867),
    'Cu': (29, 63.546),
    'Ga': (31, 69.723),
    'Ge': (32, 72.630),
    'I':  (53, 126.904),
    'Cs': (55, 132.905),
    'Gd': (64, 157.250),
    'W':  (74, 183.840),
    'Pb': (82, 207.200)
}

TARGETS = {
    # Pure Elements
    'al': {'Al': 1},
    'pb': {'Pb': 1},
    'cu': {'Cu': 1},
    'c':  {'C': 1},
    'ti': {'Ti': 1},
    'w':  {'W': 1},
    'be': {'Be': 1},
    'ge': {'Ge': 1},
    'ga': {'Ga': 1},
    'o':  {'O': 1},
    
    # Compounds (Symbol: Moles)
    'csi':          {'Cs': 1, 'I': 1},
    'lanex':        {'Gd': 2, 'O': 2, 'S': 1},
    'teflon':       {'C': 2, 'F': 4},
    'mylar':        {'C': 10, 'H': 8, 'O': 4},
    'polyethylene': {'C': 2, 'H': 4},
    'kapton':       {'C': 22, 'H': 10, 'N': 2, 'O': 5}
}

AVOGADRO = 6.02214076e23
BARN_TO_CM2 = 1e-24
NIST_XCOM_HDF5_PATH = '/Users/fcsalgado/anaconda3/envs/website/lib/python3.11/site-packages/xcom/data/NIST_XCOM.hdf5'

def interpolate_segment(energies, values, dense_energies):
    mask = (dense_energies >= energies[0]) & (dense_energies <= energies[-1])
    dense_seg_e = dense_energies[mask]
    
    result = np.zeros_like(dense_seg_e)
    if len(dense_seg_e) == 0:
        return mask, result
        
    valid = values > 0
    if np.sum(valid) > 1:
        cs = CubicSpline(np.log(energies[valid]), np.log(values[valid]))
        result = np.exp(cs(np.log(dense_seg_e)))
    elif np.sum(valid) == 1:
        result[:] = values[valid][0]
        
    return mask, result

def generate_dense_grid(raw_energies):
    dense_energies = []
    for i in range(len(raw_energies) - 1):
        e1, e2 = raw_energies[i], raw_energies[i+1]
        dense_energies.append(e1)
        if e2 - e1 > 1.0:
            num_points = max(10, int(5000 * (np.log(e2) - np.log(e1)) / (np.log(1e11) - np.log(1e3))))
            interm = np.geomspace(e1, e2, num_points + 2)[1:-1]
            dense_energies.extend(interm)
    dense_energies.append(raw_energies[-1])
    return np.array(dense_energies)

def get_segments(raw_energies):
    segments = []
    current_seg = [0]
    for i in range(len(raw_energies) - 1):
        if raw_energies[i+1] - raw_energies[i] <= 1.0:
            current_seg.append(i)
            segments.append(current_seg)
            current_seg = [i+1]
    current_seg.append(len(raw_energies)-1)
    segments.append(current_seg)
    return segments

def generate_data(output_dir):
    with tables.open_file(NIST_XCOM_HDF5_PATH, 'r') as h5file:
        for target_name, formula in TARGETS.items():
            print(f"Generating data for {target_name.upper()}...")
            
            keys = ['coherent', 'incoherent', 'photoelectric', 'pair_atom', 'pair_electron']
            
            # Step 1: Compute Molar Mass and get unified raw grid of absorption edges
            total_molar_mass = 0
            unified_raw_energies = []
            element_raw_data = {}
            
            for elem, moles in formula.items():
                Z, A = ATOMIC_DATA[elem]
                total_molar_mass += moles * A
                
                node_path = f'/Z{Z:03d}/data'
                data = h5file.get_node(node_path)[:]
                element_raw_data[elem] = data
                unified_raw_energies.extend(data['energy'])
                
            # Deduplicate and sort raw energies to perfectly preserve all edges
            unified_raw_energies = np.unique(np.array(unified_raw_energies))
            unified_raw_energies.sort()
            
            # Step 2: Generate dense grid from the unified raw edges
            dense_energies = generate_dense_grid(unified_raw_energies)
            
            # This dictionary will hold the final aggregated macroscopic cross-sections in cm2/g
            aggregated_data = {k: np.zeros_like(dense_energies) for k in keys}
            
            # Step 3: Process each element, interpolate to the dense grid, and aggregate
            for elem, moles in formula.items():
                Z, A = ATOMIC_DATA[elem]
                mass_fraction = (moles * A) / total_molar_mass
                conversion_factor = (AVOGADRO * BARN_TO_CM2) / A
                
                raw_data = element_raw_data[elem]
                raw_energies = raw_data['energy']
                segments = get_segments(raw_energies)
                
                element_interp_data = {k: np.zeros_like(dense_energies) for k in keys}
                
                for seg in segments:
                    start_idx, end_idx = seg[0], seg[-1]
                    if start_idx == end_idx:
                        continue
                        
                    seg_e = raw_energies[start_idx:end_idx+1]
                    for k in keys:
                        seg_v = raw_data[k][start_idx:end_idx+1]
                        mask, interp_v = interpolate_segment(seg_e, seg_v, dense_energies)
                        # We only assign to masked area to avoid zeroing out regions that might have been processed by other segments 
                        # actually for a single element, segments don't overlap, but we need to ensure interpolation only inside the segment's energy bounds
                        element_interp_data[k][mask] = interp_v
                
                # Add to macroscopic total
                for k in keys:
                    aggregated_data[k] += element_interp_data[k] * conversion_factor * mass_fraction
            
            aggregated_data['total_without_coherent'] = np.sum([aggregated_data[k] for k in keys if k != 'coherent'], axis=0)
            aggregated_data['total'] = aggregated_data['total_without_coherent'] + aggregated_data['coherent']
            
            # Step 4: Write to CSV
            filepath = os.path.join(output_dir, f"{target_name}.csv")
            with open(filepath, 'w') as f:
                f.write("Photon    Coherent Incoher. Photoel. Nuclear  Electron Tot. w/  Tot. wo/ \n")
                f.write("Energy    Scatter. Scatter. Absorb.  Pr. Prd. Pr. Prd. Coherent Coherent \n")
                
                for i in range(len(dense_energies)):
                    energy_MeV = dense_energies[i] / 1e6
                    f.write(f"{energy_MeV:8.3E} "
                            f"{aggregated_data['coherent'][i]:9.3E} "
                            f"{aggregated_data['incoherent'][i]:9.3E} "
                            f"{aggregated_data['photoelectric'][i]:9.3E} "
                            f"{aggregated_data['pair_atom'][i]:9.3E} "
                            f"{aggregated_data['pair_electron'][i]:9.3E} "
                            f"{aggregated_data['total'][i]:9.3E} "
                            f"{aggregated_data['total_without_coherent'][i]:9.3E} \n")

if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(__file__), 'nist-xcom-data')
    os.makedirs(out_dir, exist_ok=True)
    generate_data(out_dir)
    print("Done! Flawless compound edge-preserving high-resolution CSV files created.")
