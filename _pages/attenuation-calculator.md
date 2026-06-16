---
layout: archive-no-title
permalink: /attenuation-calculator/
title: "Photon Attenuation Calculator"
author_profile: true
redirect_from: 
  - /attenuation-calculator
---

<style>
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  overflow-x: hidden;
}
.page__footer {
  display: none !important;
}
.attenuation-container {
  width: 100%;
  margin: 0;
  padding: 20px;
  box-sizing: border-box;
  padding-bottom: 60px;
}
.attenuation-form {
  background: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
  min-height: 300px;
}
.attenuation-form .form-group {
  margin-bottom: 10px;
}
.attenuation-form label {
  display: block;
  font-weight: bold;
  margin-bottom: 4px;
  font-size: 14px;
}
.attenuation-form select,
.attenuation-form input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
  box-sizing: border-box;
}
.attenuation-form button {
  background: #2c3e50;
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  width: 100%;
  margin-top: 8px;
}
.attenuation-form button:hover {
  background: #34495e;
}
.result-card {
  background: #f9f5f5;
  padding: 8px 12px;
  border-radius: 6px;
  text-align: center;
  border: 1px solid #ddd;
}
.result-card h4 {
  margin: 0 0 4px 0;
  font-size: 12px;
  color: #333;
  font-weight: bold;
  text-transform: uppercase;
}
.result-card .value {
  font-size: 13px;
  font-weight: normal;
  color: #2c3e50;
}
.error-message {
  color: #e74c3c;
  padding: 12px;
  background: #fadbd8;
  border-radius: 4px;
  margin: 12px 0;
  display: none;
  font-size: 14px;
}
.error-message.visible {
  display: block;
}
.input-results-row {
  display: grid;
  grid-template-columns: 256px 350px;
  gap: 30px;
  margin-bottom: 25px;
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
}
.input-column {
  order: 1;
}
.results-column {
  order: 2;
}
.results-info {
  margin-bottom: 15px;
  font-size: 13px;
  line-height: 1.6;
}
@media (max-width: 900px) {
  .input-results-row {
    grid-template-columns: 1fr;
  }
  .input-column {
    order: 2;
  }
  .results-column {
    order: 1;
  }
  .attenuation-container {
    padding: 15px 20px;
  }
}
</style>

<div class="attenuation-container">
  {% include base_path %}
  <h2 class="page__title">Photon Attenuation Calculator</h2>
  <p>Calculate attenuation, transmission, and interaction probabilities for photon-matter interactions.</p>
  <p>Source for the mass interaction coefficients: <a href="https://physics.nist.gov/PhysRefData/Xcom/html/xcom1.html" target="_blank">XCOM NIST database</a></p>
  <p>For more details on how to calculate, <a href="/attenuation-explanation/">here</a>.</p>
  
  <div id="errorMessage" class="error-message"></div>
  
  <div class="input-results-row" id="resultsSection">
    <div class="input-column">
      <div class="attenuation-form">
        <div class="form-group">
          <label for="material">Target Material:</label>
          <select id="material">
            <option value="">Loading materials...</option>
          </select>
        </div>
        <div class="form-group">
          <label for="length">Material Length (mm):</label>
          <input type="number" id="length" value="10" min="0.1" step="0.1">
        </div>
        <div class="form-group">
          <label for="energy">Photon Energy (keV):</label>
          <input type="number" id="energy" value="1000" min="1" step="1">
        </div>
        <button id="calculateBtn">Calculate</button>
      </div>
    </div>
    
    <div class="results-column">
      <div class="result-card" style="text-align: left;">
        <div class="results-info">
          <span><strong>Material:</strong> <span id="resultMaterial">-</span>, <strong>Energy:</strong> <span id="resultEnergy">-</span> keV</span>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px;">
          <div class="result-card">
            <h4>Attenuation</h4>
            <div class="value" id="attenuationValue">-</div>
          </div>
          <div class="result-card">
            <h4>Transmission</h4>
            <div class="value" id="transmissionValue">-</div>
          </div>
          <div class="result-card">
            <h4>Rayleigh (Coherent)</h4>
            <div class="value" id="rayleighProb">-</div>
          </div>
          <div class="result-card">
            <h4>Compton (Incoherent)</h4>
            <div class="value" id="comptonProb">-</div>
          </div>
          <div class="result-card">
            <h4>Photoelectric</h4>
            <div class="value" id="photoelectricProb">-</div>
          </div>
          <div class="result-card">
            <h4>Nuclear Pair Prod.</h4>
            <div class="value" id="nuclearProb">-</div>
          </div>
          <div class="result-card">
            <h4>Electron Pair Prod.</h4>
            <div class="value" id="electronProb">-</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
const DENSITIES = {
  'al': 2.699,
  'pb': 11.35,
  'cu': 8.96,
  'c': 2.267,
  'ti': 4.506,
  'w': 19.30,
  'be': 1.85,
  'ge': 5.323,
  'ga': 5.91,
  'o': 0.001429,
  'csi': 4.51,
  'lanex': 7.32,
  'teflon': 2.20,
  'mylar': 1.40,
  'polyethylene': 0.94,
  'kapton': 1.42
};

const DISPLAY_NAMES = {
  'csi': 'CsI',
  'lanex': 'Lanex (Gadolinium)',
  'teflon': 'Teflon',
  'mylar': 'Mylar',
  'polyethylene': 'Polyethylene',
  'kapton': 'Kapton (Polyamid)',
  'pb': 'Pb (Lead)',
  'cu': 'Cu (Copper)',
  'al': 'Al (Aluminum)',
  'w': 'W (Tungsten)',
  'ti': 'Ti (Titanium)',
  'be': 'Be (Beryllium)',
  'ge': 'Ge (Germanium)',
  'ga': 'Ga (Gallium)',
  'o': 'O (Oxygen)',
  'c': 'C (Carbon)'
};

let materialsData = {};

function formatPercent(value) {
  if (value === undefined || value === null || isNaN(value)) return '-';
  return (value * 100).toPrecision(5) + '%';
}

function ensurePositive(value, epsilon = 1e-12) {
  if (value <= 0) return epsilon;
  return value;
}

async function loadMaterials() {
  const materialSelect = document.getElementById('material');
  
  try {
    const response = await fetch('/attenuation/nist-xcom-data/');
    const html = await response.text();
    
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    const links = doc.querySelectorAll('a');
    
    const csvFiles = [];
    links.forEach(link => {
      const href = link.getAttribute('href');
      if (href && href.endsWith('.csv')) {
        const filename = href.replace('/attenuation/nist-xcom-data/', '').replace('.csv', '');
        csvFiles.push(filename);
      }
    });
    
    if (csvFiles.length === 0) {
      csvFiles.push('al', 'pb', 'cu', 'c');
    }
    
    materialSelect.innerHTML = '';
    csvFiles.forEach(name => {
      const option = document.createElement('option');
      option.value = name;
      option.textContent = DISPLAY_NAMES[name] || (name.charAt(0).toUpperCase() + name.slice(1));
      materialSelect.appendChild(option);
    });
    
    await loadAllMaterials(csvFiles);
    
  } catch (error) {
    console.error('Error loading materials:', error);
    materialSelect.innerHTML = '<option value="al">Al (default)</option>';
    await loadMaterialData('al');
  }
}

async function loadAllMaterials(files) {
  for (const file of files) {
    await loadMaterialData(file);
  }
}

async function loadMaterialData(material) {
  if (materialsData[material]) return;
  
  try {
    const response = await fetch(`/attenuation/nist-xcom-data/${material}.csv`);
    if (!response.ok) {
      const fallbackMaterials = ['al', 'pb', 'cu', 'c'];
      if (fallbackMaterials.includes(material)) {
        console.warn(`Could not load ${material}.csv, using fallback data`);
        materialsData[material] = generateFallbackData(material);
        return;
      }
      throw new Error(`Failed to load ${material}.csv`);
    }
    
    const text = await response.text();
    const data = parseCSV(text);
    materialsData[material] = data;
    
  } catch (error) {
    console.error(`Error loading ${material}:`, error);
    materialsData[material] = generateFallbackData(material);
  }
}

function generateFallbackData(material) {
  const energies = [0.001, 0.0015, 0.002, 0.003, 0.004, 0.005, 0.006, 0.008, 0.01, 0.015, 0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.022, 1.25, 1.5, 2.0, 2.044, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 15.0, 20.0, 30.0, 40.0, 50.0, 60.0, 80.0, 100.0];
  
  const baseValues = {
    'al': { coherent: 2.256, incoherent: 0.01427, photoelectric: 1183, nuclear: 0, electron: 0 },
    'pb': { coherent: 368.0, incoherent: 0.38, photoelectric: 4850, nuclear: 0, electron: 0 },
    'cu': { coherent: 41.5, incoherent: 0.048, photoelectric: 385, nuclear: 0, electron: 0 },
    'c': { coherent: 0.8, incoherent: 0.002, photoelectric: 0.42, nuclear: 0, electron: 0 }
  };
  
  const base = baseValues[material] || baseValues['al'];
  const density = DENSITIES[material] || 2.7;
  
  return energies.map(E => {
    const scale = E < 0.1 ? 1 + Math.log10(0.1/E) : (E > 10 ? 1 + Math.log10(E/10) * 0.3 : 1);
    return {
      energy: E,
      coherent: base.coherent * scale / E,
      incoherent: base.incoherent * (1 + Math.log10(E)),
      photoelectric: base.photoelectric * scale / Math.sqrt(E),
      nuclear: E > 1.022 ? (E - 1.022) * 0.0001 * density : 0,
      electron: E > 2.044 ? (E - 2.044) * 0.00005 * density : 0,
      total: base.coherent * scale / E + base.incoherent * (1 + Math.log10(E)) + base.photoelectric * scale / Math.sqrt(E),
      totalNoCoherent: base.incoherent * (1 + Math.log10(E)) + base.photoelectric * scale / Math.sqrt(E)
    };
  });
}

function parseCSV(text) {
  const lines = text.trim().split('\n');
  const data = [];
  
  for (let i = 2; i < lines.length; i++) {
    const line = lines[i].trim();
    if (!line) continue;
    
    const parts = line.split(/\s+/);
    if (parts.length < 8) continue;
    
    try {
      const entry = {
        energy: parseFloat(parts[0]),
        coherent: parseFloat(parts[1]),
        incoherent: parseFloat(parts[2]),
        photoelectric: parseFloat(parts[3]),
        nuclear: parseFloat(parts[4]),
        electron: parseFloat(parts[5]),
        total: parseFloat(parts[6]),
        totalNoCoherent: parseFloat(parts[7])
      };
      data.push(entry);
    } catch (e) {
      console.warn('Parse error on line', i, e);
    }
  }
  
  return data.sort((a, b) => a.energy - b.energy);
}

function interpolate(data, targetEnergy) {
  if (targetEnergy <= data[0].energy) {
    return { ...data[0] };
  }
  if (targetEnergy >= data[data.length - 1].energy) {
    return { ...data[data.length - 1] };
  }
  
  const logInterp = (x, x1, x2, y1, y2) => {
    if (y1 <= 0 || y2 <= 0) {
      const ratio = (x - x1) / (x2 - x1);
      return y1 + ratio * (y2 - y1);
    }
    const logX = Math.log(x);
    const logX1 = Math.log(x1);
    const logX2 = Math.log(x2);
    const logY1 = Math.log(y1);
    const logY2 = Math.log(y2);
    
    const logY = logY1 + (logX - logX1) * (logY2 - logY1) / (logX2 - logX1);
    return Math.exp(logY);
  };
  
  for (let i = 0; i < data.length - 1; i++) {
    if (targetEnergy >= data[i].energy && targetEnergy <= data[i + 1].energy) {
      const x = targetEnergy;
      const x1 = data[i].energy;
      const x2 = data[i + 1].energy;
      
      return {
        energy: targetEnergy,
        coherent: logInterp(x, x1, x2, data[i].coherent, data[i + 1].coherent),
        incoherent: logInterp(x, x1, x2, data[i].incoherent, data[i + 1].incoherent),
        photoelectric: logInterp(x, x1, x2, data[i].photoelectric, data[i + 1].photoelectric),
        nuclear: logInterp(x, x1, x2, data[i].nuclear, data[i + 1].nuclear),
        electron: logInterp(x, x1, x2, data[i].electron, data[i + 1].electron),
        total: logInterp(x, x1, x2, data[i].total, data[i + 1].total),
        totalNoCoherent: logInterp(x, x1, x2, data[i].totalNoCoherent, data[i + 1].totalNoCoherent)
      };
    }
  }
  
  return { ...data[Math.floor(data.length / 2)] };
}

function calculate(material, lengthMm, energyKeV) {
  const density = DENSITIES[material] || 2.7;
  const energyMeV = energyKeV / 1000;
  const lengthCm = lengthMm * 0.1;
  
  const data = materialsData[material];
  if (!data) {
    throw new Error('Material data not loaded');
  }
  
  if (energyMeV < data[0].energy || energyMeV > data[data.length - 1].energy) {
    console.warn(`Energy ${energyMeV} MeV outside data range [${data[0].energy}, ${data[data.length - 1].energy}] MeV`);
  }
  
  const interpolated = interpolate(data, energyMeV);
  
  const sigmaTotal = interpolated.total;
  const muTotal = sigmaTotal * density;
  
  const transmission = Math.exp(-muTotal * lengthCm);
  const attenuation = 1 - transmission;
  
  const pInteract = attenuation;
  
  const probabilities = {
    rayleigh: (interpolated.coherent / sigmaTotal) * pInteract,
    compton: (interpolated.incoherent / sigmaTotal) * pInteract,
    photoelectric: (interpolated.photoelectric / sigmaTotal) * pInteract,
    nuclear: (interpolated.nuclear / sigmaTotal) * pInteract,
    electron: (interpolated.electron / sigmaTotal) * pInteract
  };

  return {
    attenuation: attenuation,
    transmission: transmission,
    probabilities: probabilities,
    data: data,
    interpolated: interpolated,
    density: density
  };
}

function showError(message) {
  const errorDiv = document.getElementById('errorMessage');
  errorDiv.textContent = message;
  errorDiv.classList.add('visible');
}

function hideError() {
  const errorDiv = document.getElementById('errorMessage');
  errorDiv.classList.remove('visible');
}

function displayResults(result, material, energy) {
  document.getElementById('resultMaterial').textContent = DISPLAY_NAMES[material] || (material.charAt(0).toUpperCase() + material.slice(1));
  document.getElementById('resultEnergy').textContent = energy;
  
  document.getElementById('attenuationValue').textContent = formatPercent(result.attenuation);
  document.getElementById('transmissionValue').textContent = formatPercent(result.transmission);
  document.getElementById('rayleighProb').textContent = formatPercent(result.probabilities.rayleigh);
  document.getElementById('comptonProb').textContent = formatPercent(result.probabilities.compton);
  document.getElementById('photoelectricProb').textContent = formatPercent(result.probabilities.photoelectric);
  document.getElementById('nuclearProb').textContent = formatPercent(result.probabilities.nuclear);
  document.getElementById('electronProb').textContent = formatPercent(result.probabilities.electron);
}

document.getElementById('calculateBtn').addEventListener('click', async () => {
  hideError();
  
  const material = document.getElementById('material').value;
  const length = parseFloat(document.getElementById('length').value);
  const energy = parseFloat(document.getElementById('energy').value);
  
  if (!material) {
    showError('Please select a material');
    return;
  }
  
  if (isNaN(length) || length <= 0) {
    showError('Please enter a valid length');
    return;
  }
  
  if (isNaN(energy) || energy <= 0) {
    showError('Please enter a valid energy');
    return;
  }
  
  await loadMaterialData(material);
  
  try {
    const result = calculate(material, length, energy);
    displayResults(result, material, energy);
  } catch (error) {
    showError('Error calculating: ' + error.message);
  }
});

loadMaterials();
</script>