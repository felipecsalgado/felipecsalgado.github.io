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

<script src="{{ base_path }}/assets/js/counts-estimation.js"></script>

