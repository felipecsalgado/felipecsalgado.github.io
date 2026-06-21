def calculate_camera_signal(dynamic_range_db=None, read_noise_e=None):
    # 1. Input parameter
    # a. Energy Deposition and crystal characteristics
    dE_dx_mass = 1.628     # MeV cm^2/g # LYSO = 1.628
    density_lyso = 5.4     # g/cm^3 density of LYSO = 7.1 g/cm^3
    thickness_cm = 50     # cm (5 mm)

    # b. Camera characteristics
    fwc = 100000            # Full well capacity in electrons
    adc_bits = 16
    qe = 0.95              # Manta G-033B typical QE at LYSO emission
    f_number = 1.6
    focal_length_mm = 25   # mm

    #c object location
    object_dist_mm = 260. + 85   # mm


    # Energy deposition in the crystal
    energy_deposited_mev = dE_dx_mass * density_lyso * thickness_cm
    energy_deposited_kev = energy_deposited_mev * 1000
    
    # 2. Scintillation Photon Generation
    light_yield_per_kev = 54 # photons/keV
    photons_generated = energy_deposited_kev * light_yield_per_kev
    
    # 3. Optical Collection Efficiency
    # Isotropic into 4*pi (unpolished/unwrapped pixels)
    magnification = focal_length_mm / (object_dist_mm - focal_length_mm)
    inverse_mag_term = (1 + (1 / magnification))**2
    
    eta_isotropic = 1 / (16 * (f_number**2) * inverse_mag_term)

    # Lambertian into 2*pi (polished/wrapped light-guide pixels)
    eta_lambertian = 1 / (4 * (f_number**2) * inverse_mag_term)
    
    # 4. Sensor Photoelectron Conversion

    
    electrons_iso = photons_generated * eta_isotropic * qe
    electrons_lamb = photons_generated * eta_lambertian * qe
    
    # 5. ADC Conversion
    max_adc = (2**adc_bits) - 1 # 4095
    electrons_per_adc = fwc / max_adc

    adc_iso = electrons_iso / electrons_per_adc
    adc_lamb = electrons_lamb / electrons_per_adc
    
    # 6. Dynamic Range & SNR (optional)
    # If dynamic range (dB) and/or read noise are provided, compute SNR
    snr_iso = None
    snr_lamb = None

    if read_noise_e is not None and read_noise_e > 0:
        # SNR = signal / noise  (signal in electrons, noise = read noise)
        snr_iso = electrons_iso / read_noise_e
        snr_lamb = electrons_lamb / read_noise_e

    # Cross-check: if dynamic range is given, derive the implied saturation capacity
    implied_saturation = None
    if dynamic_range_db is not None and read_noise_e is not None and read_noise_e > 0:
        import math
        implied_saturation = read_noise_e * (10 ** (dynamic_range_db / 20.0))

    # Print Results
    print("--- Scintillator & Camera Signal Calculation ---")
    print(f"Energy Deposited:       {energy_deposited_mev:.4f} MeV")
    print(f"Total Photons Generated:{photons_generated:.0f} photons")
    print(f"Conversion Gain:        {electrons_per_adc:.2f} e-/ADC count")

    if implied_saturation is not None:
        print(f"\n--- Dynamic Range Cross-Check ---")
        print(f"Dynamic Range:          {dynamic_range_db:.1f} dB")
        print(f"Read Noise:             {read_noise_e:.1f} e-")
        print(f"Implied Saturation:     {implied_saturation:.0f} e-")

    print("\n--- Results: Isotropic Emission ---")
    print(f"Collection Efficiency:  {eta_isotropic:.3e}")
    print(f"Electrons Generated:    {electrons_iso:.3f} e-")
    print(f"ADC Counts:             {adc_iso:.3f} counts")
    if snr_iso is not None:
        print(f"SNR:                    {snr_iso:.2f} ({20 * __import__('math').log10(snr_iso):.1f} dB)")

    print("\n--- Results: Lambertian Emission ---")
    print(f"Collection Efficiency:  {eta_lambertian:.3e}")
    print(f"Electrons Generated:    {electrons_lamb:.3f} e-")
    print(f"ADC Counts:             {adc_lamb:.3e} counts")
    if snr_lamb is not None:
        print(f"SNR:                    {snr_lamb:.2f} ({20 * __import__('math').log10(snr_lamb):.1f} dB)")

if __name__ == "__main__":
    # Example: run with default values
    calculate_camera_signal()

    # Example: run with Manta G-145B NIR datasheet values (DR and read noise)
    print("\n" + "="*55)
    print("=== With Manta G-145B NIR DR & read noise ===")
    print("="*55 + "\n")
    calculate_camera_signal(dynamic_range_db=65.6, read_noise_e=8.8)