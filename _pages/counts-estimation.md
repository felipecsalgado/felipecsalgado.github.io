---
layout: archive-no-title
permalink: /counts-estimation/
title: "Counts Estimation"
author_profile: true
redirect_from: 
  - /counts-estimation
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
.counts-container {
  width: 100%;
  margin: 0;
  padding: 20px;
  box-sizing: border-box;
  padding-bottom: 60px;
}
.counts-form {
  background: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
  min-height: 300px;
}
.counts-form .form-group {
  margin-bottom: 10px;
}
.counts-form .section-title {
  font-size: 14px;
  font-weight: bold;
  color: #2c3e50;
  margin: 15px 0 8px 0;
  border-bottom: 1px solid #ddd;
  padding-bottom: 2px;
}
.counts-form .section-title:first-of-type {
  margin-top: 0;
}
.counts-form label {
  display: block;
  font-weight: bold;
  margin-bottom: 2px;
  font-size: 12px;
}
.counts-form input, .counts-form select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 13px;
  box-sizing: border-box;
}
.counts-form input:disabled, .counts-form select:disabled {
  background-color: #e9ecef !important;
  color: #495057 !important;
  cursor: not-allowed;
  border-color: #ced4da;
}
.counts-form input:not(:disabled), .counts-form select:not(:disabled) {
  background-color: #ffffff !important;
}
.counts-form select {
  height: 37px;
  background: white;
}
.counts-form button {
  background: #2c3e50;
  color: white;
  padding: 10px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  width: 100%;
  margin-top: 15px;
  font-weight: bold;
}
.counts-form button:hover {
  background: #34495e;
}
.form-row-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}
.form-row-3 {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 12px;
}
.form-row-2 > .form-group, .form-row-3 > .form-group {
  display: flex;
  flex-direction: column;
}
.form-row-2 > .form-group input, .form-row-2 > .form-group select,
.form-row-3 > .form-group input, .form-row-3 > .form-group select {
  margin-top: auto;
}
.result-card {
  background: #f9f5f5;
  padding: 10px 12px;
  border-radius: 6px;
  text-align: center;
  border: 1px solid #ddd;
}
.result-card h4 {
  margin: 0 0 4px 0;
  font-size: 11px;
  color: #333;
  font-weight: bold;
  text-transform: uppercase;
}
.result-card .value {
  font-size: 13px;
  font-weight: normal;
  color: #2c3e50;
}
.result-card.highlight {
  background: #0e6655;
  color: white;
  border-color: #0b5345;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}
.result-card.highlight h4 {
  color: #a3e4d7;
}
.result-card.highlight .value {
  color: white;
  font-size: 14px;
  font-weight: bold;
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
  grid-template-columns: 450px 1fr;
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
.results-section-header {
  margin: 20px 0 8px 0;
  font-size: 13px;
  font-weight: bold;
  color: #2c3e50;
  border-bottom: 1px solid #eee;
  padding-bottom: 4px;
}
.results-section-header:first-of-type {
  margin-top: 0;
}
.results-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
}
@media (max-width: 900px) {
  .input-results-row {
    grid-template-columns: 1fr;
  }
  .input-column {
    order: 1;
  }
  .results-column {
    order: 2;
  }
  .counts-container {
    padding: 15px 20px;
  }
  .results-grid {
    grid-template-columns: 1fr !important;
  }
}
@media (max-width: 600px) {
  .form-row-2, .form-row-3 {
    grid-template-columns: 1fr;
    gap: 8px;
  }
}
</style>

<div class="counts-container">
  {% include base_path %}
  <h2 class="page__title">Counts Estimation</h2>
  <p>Calculate the estimated number of camera counts based on the scintillator material, imaging system configuration, and camera specifications. For a detailed explanation of the physical and mathematical formulas used, see the <a href="/counts-estimation-explanation/">Counts Estimation Calculation Details</a> page.</p>
  
  <div id="errorMessage" class="error-message"></div>
  
  <div class="input-results-row" id="resultsSection">
    <div class="input-column">
      <div class="counts-form">
        <div class="section-title">1. Crystal & Energy</div>
        <div class="form-group" style="margin-bottom: 12px;">
          <label for="crystalSelect">Crystal Type:</label>
          <select id="crystalSelect">
            <option value="CsI">CsI</option>
            <option value="CsI(Na)">CsI(Na)</option>
            <option value="CsI(Tl)" selected>CsI(Tl)</option>
            <option value="LYSO(Ce)">LYSO(Ce)</option>
            <option value="NaI(Tl)">NaI(Tl)</option>
            <option value="YAG(Ce)">YAG(Ce)</option>
            <option value="PbF2">PbF2</option>
            <option value="Custom">Custom</option>
          </select>
        </div>
        <div class="form-row-2">
          <div class="form-group">
            <label for="density">Density of crystal (g/cm³):</label>
            <input type="number" id="density" value="5.4" min="0.0001" step="0.01">
          </div>
          <div class="form-group">
            <label for="lightYield">Light yield (photons/keV):</label>
            <input type="number" id="lightYield" value="54" min="0" step="1">
          </div>
        </div>
        <div class="form-row-2">
          <div class="form-group">
            <label for="dEdxMass">Mass stopping power dE/dx (MeV·cm²/g):</label>
            <input type="number" id="dEdxMass" value="1.628" min="0.0001" step="0.001">
          </div>
          <div class="form-group">
            <label for="thicknessCm">Crystal thickness (cm):</label>
            <input type="number" id="thicknessCm" value="5" min="0.0001" step="0.1">
          </div>
        </div>

        <div class="section-title">2. Camera specs</div>
        <div class="form-group" style="margin-bottom: 12px;">
          <label for="cameraSelect">Camera Model:</label>
          <select id="cameraSelect">
            <option value="Manta-G145B NIR">Manta-G145B NIR</option>
            <option value="Manta-033">Manta-033</option>
            <option value="Andor Ikon-L (936 BV)" selected>Andor Ikon-L (936 BV)</option>
            <option value="Andor Ikon-L (936 BEX2-DD )">Andor Ikon-L (936 BEX2-DD )</option>
            <option value="Andor Ikon-M (934 BV)">Andor Ikon-M (934 BV)</option>
            <option value="Andor Ikon-M (BEX2-DD)">Andor Ikon-M (BEX2-DD)</option>
            <option value="Andor Ikon-M SO (BN/BEN/BR-DD)">Andor Ikon-M SO (BN/BEN/BR-DD)</option>
            <option value="Andor Ikon-L SO (BN/BEN/BR-DD)">Andor Ikon-L SO (BN/BEN/BR-DD)</option>
            <option value="Basler acA2440-20gm">Basler acA2440-20gm</option>
            <option value="Basler acA1920-40gm">Basler acA1920-40gm</option>
            <option value="Custom">Custom</option>
          </select>
        </div>
        <div class="form-row-3">
          <div class="form-group">
            <label for="fwc">Full well capacity (e⁻):</label>
            <input type="number" id="fwc" value="100000" min="1" step="1000">
          </div>
          <div class="form-group">
            <label for="adcBits">ADC Resolution (bits):</label>
            <input type="number" id="adcBits" value="16" min="1" max="32" step="1">
          </div>
          <div class="form-group">
            <label for="qe">Quantum Efficiency (%):</label>
            <input type="number" id="qe" value="95" min="0" max="100" step="1">
          </div>
        </div>
        <div class="form-row-2">
          <div class="form-group">
            <label for="dynamicRange">Dynamic Range (dB) <span style="font-weight:normal; font-size:11px; color:#777;">(optional)</span>:</label>
            <input type="number" id="dynamicRange" placeholder="e.g. 65.6" min="0" step="0.1">
          </div>
          <div class="form-group">
            <label for="readNoise">Read Noise (e⁻) <span style="font-weight:normal; font-size:11px; color:#777;">(optional)</span>:</label>
            <input type="number" id="readNoise" placeholder="e.g. 8.8" min="0" step="0.1">
          </div>
        </div>

        <div class="section-title">3. Imaging System</div>
        <div class="form-row-2">
          <div class="form-group">
            <label for="fNumber">Lens f-number (f/#):</label>
            <input type="number" id="fNumber" value="1.6" min="0.1" step="0.1">
          </div>
          <div class="form-group">
            <label for="focalLength">Lens Focal Length (mm):</label>
            <input type="number" id="focalLength" value="25" min="0.1" step="1">
          </div>
        </div>
        <div class="form-group" style="margin-bottom: 0;">
          <label for="objectDist">Object Distance (mm):</label>
          <input type="number" id="objectDist" value="345" min="0.1" step="1">
        </div>

        <button id="calculateBtn">Calculate</button>
      </div>
    </div>
    
    <div class="results-column">
      <div class="result-card" style="text-align: left;">
        <div class="results-info">
          <span><strong>Status:</strong> Calculations based on the input parameters shown on the left.</span>
        </div>
        
        <div class="results-section-header">General Metrics</div>
        <div class="results-grid" style="grid-template-columns: repeat(3, 1fr); margin-bottom: 20px;">
          <div class="result-card">
            <h4>Energy Deposited</h4>
            <div class="value" id="energyDeposited">-</div>
          </div>
          <div class="result-card">
            <h4>Photons Generated</h4>
            <div class="value" id="photonsGenerated">-</div>
          </div>
          <div class="result-card">
            <h4>Conversion Gain</h4>
            <div class="value" id="conversionGain">-</div>
          </div>
        </div>

        <div class="results-section-header" id="drCrossCheckHeader" style="display:none;">Dynamic Range Cross-Check</div>
        <div class="results-grid" id="drCrossCheckGrid" style="grid-template-columns: repeat(2, 1fr); margin-bottom: 20px; display:none;">
          <div class="result-card">
            <h4>Implied Saturation</h4>
            <div class="value" id="impliedSaturation">-</div>
          </div>
          <div class="result-card">
            <h4>DR / Read Noise</h4>
            <div class="value" id="drReadNoise">-</div>
          </div>
        </div>

        <div class="results-section-header">Isotropic Emission (unpolished/unwrapped crystal)</div>
        <div class="results-grid" style="margin-bottom: 20px;">
          <div class="result-card">
            <h4>Collection Efficiency</h4>
            <div class="value" id="effIsotropic">-</div>
          </div>
          <div class="result-card">
            <h4>Electrons Generated</h4>
            <div class="value" id="electronsIsotropic">-</div>
          </div>
          <div class="result-card highlight">
            <h4>ADC Counts</h4>
            <div class="value" id="adcIsotropic">-</div>
          </div>
          <div class="result-card" id="snrIsoCard" style="display:none;">
            <h4>SNR</h4>
            <div class="value" id="snrIsotropic">-</div>
          </div>
        </div>

        <div class="results-section-header">Lambertian Emission (polished/wrapped light-guide)</div>
        <div class="results-grid">
          <div class="result-card">
            <h4>Collection Efficiency</h4>
            <div class="value" id="effLambertian">-</div>
          </div>
          <div class="result-card">
            <h4>Electrons Generated</h4>
            <div class="value" id="electronsLambertian">-</div>
          </div>
          <div class="result-card highlight">
            <h4>ADC Counts</h4>
            <div class="value" id="adcLambertian">-</div>
          </div>
          <div class="result-card" id="snrLambCard" style="display:none;">
            <h4>SNR</h4>
            <div class="value" id="snrLambertian">-</div>
          </div>
        </div>
        
        <div style="margin-top: 20px; font-size: 12px; color: #7f8c8d; text-align: center; border-top: 1px solid #eee; padding-top: 12px;">
          If any error is found in the specs or calculations, please let me know and I can correct them.
        </div>
      </div>
    </div>
  </div>
</div>

<script>
const CRYSTALS = {
  'CsI': { lightYield: 2, density: 5.41 },
  'CsI(Na)': { lightYield: 41, density: 5.4 },
  'CsI(Tl)': { lightYield: 54, density: 5.4 },
  'LYSO(Ce)': { lightYield: 25, density: 7.1 },
  'NaI(Tl)': { lightYield: 55, density: 3.7 },
  'YAG(Ce)': { lightYield: 35, density: 4.5 },
  'PbF2': { lightYield: 0, density: 7.77 }
};

const CAMERAS = {
  'Manta-G145B NIR': { fwc: 17900, adcBits: 12, qe: 38, dynamicRange: 65.6, readNoise: 8.8 },
  'Manta-033': { fwc: 25949, adcBits: 12, qe: 38, dynamicRange: null, readNoise: null },
  'Andor Ikon-L (936 BV)': { fwc: 100000, adcBits: 16, qe: 95, dynamicRange: null, readNoise: null },
  'Andor Ikon-L (936 BEX2-DD )': { fwc: 150000, adcBits: 16, qe: 90, dynamicRange: null, readNoise: null },
  'Andor Ikon-M (934 BV)': { fwc: 100000, adcBits: 16, qe: 95, dynamicRange: null, readNoise: null },
  'Andor Ikon-M (BEX2-DD)': { fwc: 150000, adcBits: 16, qe: 90, dynamicRange: null, readNoise: null },
  'Andor Ikon-M SO (BN/BEN/BR-DD)': { fwc: 150000, adcBits: 16, qe: 90, dynamicRange: null, readNoise: null },
  'Andor Ikon-L SO (BN/BEN/BR-DD)': { fwc: 100000, adcBits: 16, qe: 90, dynamicRange: null, readNoise: null },
  'Basler acA2440-20gm': { fwc: 10400, adcBits: 12, qe: 68, dynamicRange: 73.3, readNoise: 2.3 },
  'Basler acA1920-40gm': { fwc: 31900, adcBits: 12, qe: 70, dynamicRange: 73.5, readNoise: 6.7 }
};

function formatValue(value, decimals = 1) {
  if (value === undefined || value === null || isNaN(value)) return '-';
  return value.toFixed(decimals);
}

function formatScientific(value, decimals = 1) {
  if (value === undefined || value === null || isNaN(value)) return '-';
  return value.toExponential(decimals);
}

function formatInteger(value) {
  if (value === undefined || value === null || isNaN(value)) return '-';
  return Math.round(value).toLocaleString();
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

function updateCrystalFields() {
  const crystal = document.getElementById('crystalSelect').value;
  const densityInput = document.getElementById('density');
  const lightYieldInput = document.getElementById('lightYield');
  
  if (crystal === 'Custom') {
    densityInput.disabled = false;
    lightYieldInput.disabled = false;
  } else {
    const data = CRYSTALS[crystal];
    densityInput.value = data.density;
    lightYieldInput.value = data.lightYield;
    densityInput.disabled = true;
    lightYieldInput.disabled = true;
  }
}

function updateCameraFields() {
  const camera = document.getElementById('cameraSelect').value;
  const fwcInput = document.getElementById('fwc');
  const adcBitsInput = document.getElementById('adcBits');
  const qeInput = document.getElementById('qe');
  const dynamicRangeInput = document.getElementById('dynamicRange');
  const readNoiseInput = document.getElementById('readNoise');
  
  if (camera === 'Custom') {
    fwcInput.disabled = false;
    adcBitsInput.disabled = false;
    qeInput.disabled = false;
    dynamicRangeInput.disabled = false;
    readNoiseInput.disabled = false;
  } else {
    const data = CAMERAS[camera];
    fwcInput.value = data.fwc;
    adcBitsInput.value = data.adcBits;
    qeInput.value = data.qe;
    
    if (data.dynamicRange !== null) {
      dynamicRangeInput.value = data.dynamicRange;
    } else {
      dynamicRangeInput.value = '';
    }
    
    if (data.readNoise !== null) {
      readNoiseInput.value = data.readNoise;
    } else {
      readNoiseInput.value = '';
    }
    
    fwcInput.disabled = true;
    adcBitsInput.disabled = true;
    qeInput.disabled = true;
    dynamicRangeInput.disabled = true;
    readNoiseInput.disabled = true;
  }
}

function calculateSignal() {
  hideError();

  // Retrieve inputs
  const dEdxMass = parseFloat(document.getElementById('dEdxMass').value);
  const density = parseFloat(document.getElementById('density').value);
  const thicknessCm = parseFloat(document.getElementById('thicknessCm').value);
  const lightYield = parseFloat(document.getElementById('lightYield').value);

  const fwc = parseFloat(document.getElementById('fwc').value);
  const adcBits = parseInt(document.getElementById('adcBits').value, 10);
  const qePercent = parseFloat(document.getElementById('qe').value);
  const fNumber = parseFloat(document.getElementById('fNumber').value);
  const focalLength = parseFloat(document.getElementById('focalLength').value);

  const objectDist = parseFloat(document.getElementById('objectDist').value);

  // Optional inputs
  const dynamicRangeStr = document.getElementById('dynamicRange').value.trim();
  const readNoiseStr = document.getElementById('readNoise').value.trim();

  const dynamicRangeInput = dynamicRangeStr !== '' ? parseFloat(dynamicRangeStr) : null;
  const readNoiseInput = readNoiseStr !== '' ? parseFloat(readNoiseStr) : null;

  // Validation
  if (isNaN(dEdxMass) || dEdxMass <= 0) return showError('Mass stopping power must be a positive number.');
  if (isNaN(density) || density <= 0) return showError('Density must be a positive number.');
  if (isNaN(thicknessCm) || thicknessCm <= 0) return showError('Thickness must be a positive number.');
  if (isNaN(lightYield) || lightYield < 0) return showError('Light yield must be greater than or equal to 0.');
  if (isNaN(fwc) || fwc <= 0) return showError('Full well capacity must be a positive number.');
  if (isNaN(adcBits) || adcBits < 1 || adcBits > 32) return showError('ADC resolution must be between 1 and 32 bits.');
  if (isNaN(qePercent) || qePercent < 0 || qePercent > 100) return showError('Quantum Efficiency must be between 0% and 100%.');
  if (isNaN(fNumber) || fNumber <= 0) return showError('Lens f-number must be a positive number.');
  if (isNaN(focalLength) || focalLength <= 0) return showError('Focal length must be a positive number.');
  if (isNaN(objectDist) || objectDist <= 0) return showError('Object distance must be a positive number.');
  if (dynamicRangeInput !== null && (isNaN(dynamicRangeInput) || dynamicRangeInput <= 0)) return showError('Dynamic Range must be a positive number.');
  if (readNoiseInput !== null && (isNaN(readNoiseInput) || readNoiseInput < 0)) return showError('Read Noise must be a non-negative number.');

  if (objectDist <= focalLength) {
    return showError('Object distance must be strictly greater than lens focal length (to form a real image).');
  }

  // Convert QE percent to fraction
  const qe = qePercent / 100;

  // 1. Energy deposition in the crystal
  const energyDepositedMev = dEdxMass * density * thicknessCm;
  const energyDepositedKev = energyDepositedMev * 1000;

  // 2. Scintillation Photon Generation
  const photonsGenerated = energyDepositedKev * lightYield;

  // 3. Optical Collection Efficiency
  const magnification = focalLength / (objectDist - focalLength);
  const inverseMagTerm = Math.pow(1 + (1 / magnification), 2);

  const etaIsotropic = 1 / (16 * Math.pow(fNumber, 2) * inverseMagTerm);
  const etaLambertian = 1 / (4 * Math.pow(fNumber, 2) * inverseMagTerm);

  // 4. Sensor Photoelectron Conversion
  const electronsIso = photonsGenerated * etaIsotropic * qe;
  const electronsLamb = photonsGenerated * etaLambertian * qe;

  // 5. ADC Conversion
  const maxAdc = Math.pow(2, adcBits) - 1;
  const electronsPerAdc = fwc / maxAdc;

  // Round down to nearest integer (Counts cannot have decimals)
  const adcIso = Math.floor(electronsIso / electronsPerAdc);
  const adcLamb = Math.floor(electronsLamb / electronsPerAdc);

  // 6. Dynamic Range & SNR (optional)
  let snrIso = null;
  let snrLamb = null;
  let impliedSaturation = null;

  if (readNoiseInput !== null && readNoiseInput > 0) {
    snrIso = electronsIso / readNoiseInput;
    snrLamb = electronsLamb / readNoiseInput;
  }

  if (dynamicRangeInput !== null && readNoiseInput !== null && readNoiseInput > 0) {
    impliedSaturation = readNoiseInput * Math.pow(10, dynamicRangeInput / 20.0);
  }

  // Display Results
  document.getElementById('energyDeposited').textContent = formatValue(energyDepositedMev, 1) + ' MeV';
  document.getElementById('photonsGenerated').textContent = formatScientific(photonsGenerated, 3) + ' photons';
  document.getElementById('conversionGain').textContent = formatValue(electronsPerAdc, 2) + ' e⁻/DN';

  // Dynamic Range Cross-Check
  const drHeader = document.getElementById('drCrossCheckHeader');
  const drGrid = document.getElementById('drCrossCheckGrid');
  if (impliedSaturation !== null) {
    drHeader.style.display = '';
    drGrid.style.display = '';
    document.getElementById('impliedSaturation').textContent = formatInteger(impliedSaturation) + ' e⁻';
    document.getElementById('drReadNoise').textContent = formatValue(dynamicRangeInput, 1) + ' dB / ' + formatValue(readNoiseInput, 1) + ' e⁻';
  } else {
    drHeader.style.display = 'none';
    drGrid.style.display = 'none';
  }

  // Isotropic
  document.getElementById('effIsotropic').textContent = formatScientific(etaIsotropic, 1);
  document.getElementById('electronsIsotropic').textContent = formatValue(electronsIso, 1) + ' e⁻';
  document.getElementById('adcIsotropic').textContent = formatInteger(adcIso) + ' counts';

  // Isotropic SNR
  const snrIsoCard = document.getElementById('snrIsoCard');
  if (snrIso !== null) {
    snrIsoCard.style.display = '';
    const snrIsoDb = 20 * Math.log10(snrIso);
    document.getElementById('snrIsotropic').textContent = formatValue(snrIso, 2) + ' (' + formatValue(snrIsoDb, 1) + ' dB)';
  } else {
    snrIsoCard.style.display = 'none';
  }

  // Lambertian
  document.getElementById('effLambertian').textContent = formatScientific(etaLambertian, 1);
  document.getElementById('electronsLambertian').textContent = formatValue(electronsLamb, 1) + ' e⁻';
  document.getElementById('adcLambertian').textContent = formatInteger(adcLamb) + ' counts';

  // Lambertian SNR
  const snrLambCard = document.getElementById('snrLambCard');
  if (snrLamb !== null) {
    snrLambCard.style.display = '';
    const snrLambDb = 20 * Math.log10(snrLamb);
    document.getElementById('snrLambertian').textContent = formatValue(snrLamb, 2) + ' (' + formatValue(snrLambDb, 1) + ' dB)';
  } else {
    snrLambCard.style.display = 'none';
  }
}

document.getElementById('calculateBtn').addEventListener('click', calculateSignal);

document.getElementById('crystalSelect').addEventListener('change', () => {
  updateCrystalFields();
  calculateSignal();
});

document.getElementById('cameraSelect').addEventListener('change', () => {
  updateCameraFields();
  calculateSignal();
});

// Initial run on page load
updateCrystalFields();
updateCameraFields();
calculateSignal();
</script>
