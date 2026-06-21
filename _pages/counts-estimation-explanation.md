---
layout: archive-no-title
permalink: /counts-estimation-explanation/
title: "Counts Estimation Calculation Details"
---

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<style>
.explanation-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}
.explanation-container h2 {
  margin-top: 30px;
  margin-bottom: 15px;
  padding-bottom: 10px;
  border-bottom: 1px solid #ddd;
}
.explanation-container p {
  margin-bottom: 15px;
  line-height: 1.7;
}
.equation-box {
  background: #f9f9f9;
  padding: 20px;
  margin: 20px 0;
  border-radius: 8px;
  border-left: 4px solid #2c3e50;
}
.equation-box p {
  margin: 10px 0;
}
.note-box {
  background: #e8f4f8;
  padding: 15px;
  margin: 15px 0;
  border-radius: 6px;
  border-left: 4px solid #3498db;
}
.note-box p {
  margin: 0;
}
</style>

<div class="explanation-container">
  {% include base_path %}
  <h1 class="page__title">Camera Counts Estimation Details</h1>
  
  <p>This page explains the physics, geometry, and mathematical formulas behind the camera counts estimation tool.</p>
  
  <h2>1. Energy Deposition in the Crystal</h2>
  
  <p>First, we calculate the energy deposited in the scintillator crystal by the ionizing radiation. This depends on the mass stopping power (or energy deposition rate) of the material, its physical density, and the path length (thickness) through the crystal:</p>
  
  <div class="equation-box">
    <p>\[E_{\text{deposited, MeV}} = \left(\frac{dE}{dx}\right)_{\text{mass}} \cdot \rho \cdot t\]</p>
  </div>
  
  <p>where:</p>
  <ul>
    <li>\(\left(\frac{dE}{dx}\right)_{\text{mass}}\) is the mass stopping power (in \(\text{MeV}\cdot\text{cm}^2/\text{g}\)),</li>
    <li>\(\rho\) is the crystal density (in \(\text{g/cm}^3\)),</li>
    <li>\(t\) is the crystal thickness (in \(\text{cm}\)).</li>
  </ul>
  
  <p>We convert the deposited energy from mega-electronvolts (\(\text{MeV}\)) to kilo-electronvolts (\(\text{keV}\)):</p>
  <div class="equation-box">
    <p>\[E_{\text{deposited, keV}} = E_{\text{deposited, MeV}} \cdot 1000\]</p>
  </div>

  <h2>2. Scintillation Photon Generation</h2>
  
  <p>The total number of optical scintillation photons generated inside the crystal volume is determined by the light yield of the crystal material:</p>
  
  <div class="equation-box">
    <p>\[N_{\text{photons}} = E_{\text{deposited, keV}} \cdot Y_{\text{light}}\]</p>
  </div>
  
  <p>where \(Y_{\text{light}}\) is the crystal light yield (in \(\text{photons/keV}\)).</p>

  <h2>3. Optical Collection Efficiency (\(\eta\))</h2>
  
  <p>Only a fraction of the generated scintillation photons will be collected by the lens and reach the camera sensor. This geometric and optical collection efficiency is heavily influenced by the lens aperture (\(f\)-number), focal length, and magnification.</p>
  
  <p>First, we calculate the lens magnification \(m\) from the focal length \(f\) and the object distance \(d_o\) (distance from the crystal to the lens principal plane):</p>
  
  <div class="equation-box">
    <p>\[m = \frac{f}{d_o - f}\]</p>
  </div>

  <p>The inverse magnification factor is defined as:</p>
  <div class="equation-box">
    <p>\[\text{Term}_{\text{mag}} = \left(1 + \frac{1}{m}\right)^2\]</p>
  </div>

  <p>Depending on the crystal surface preparation and wrapping, the light emission can be modeled in two ways:</p>

  <h3>Isotropic Emission (unpolished/unwrapped crystal)</h3>
  <p>For rough or unwrapped pixels, the light is emitted uniformly into \(4\pi\) steradians. The collection efficiency is given by:</p>
  <div class="equation-box">
    <p>\[\eta_{\text{isotropic}} = \frac{1}{16 \cdot (f/\#)^2 \cdot \text{Term}_{\text{mag}}}\]</p>
  </div>

  <h3>Lambertian Emission (polished/wrapped light-guide)</h3>
  <p>For polished or wrapped crystal interfaces with a light-guide, the emission profile is directional (Lambertian, into a \(2\pi\) hemisphere facing the lens). This increases the collection efficiency by a factor of 4:</p>
  <div class="equation-box">
    <p>\[\eta_{\text{lambertian}} = \frac{1}{4 \cdot (f/\#)^2 \cdot \text{Term}_{\text{mag}}}\]</p>
  </div>
  
  <p>where \(f/\#\) is the lens \(f\)-number (aperture setting).</p>

  <h2>4. Sensor Photoelectron Conversion</h2>
  
  <p>The collected photons hitting the sensor are converted into photoelectrons based on the camera's Quantum Efficiency (\(QE\)):</p>
  
  <div class="equation-box">
    <p>\[N_{e^-} = N_{\text{photons}} \cdot \eta \cdot QE\]</p>
  </div>
  
  <p>where \(QE\) is the sensor's Quantum Efficiency (expressed as a fraction between 0 and 1) at the scintillation light wavelength.</p>

  <h2>5. Analog-to-Digital Conversion (ADC Counts)</h2>
  
  <p>The accumulated charge (photoelectrons) in each pixel is digitized into ADC counts. The conversion gain (electrons per ADC step) is defined by the Full Well Capacity (\(\text{FWC}\)) and the bit depth of the Analog-to-Digital Converter (\(B\)):</p>
  
  <div class="equation-box">
    <p>\[\text{Gain}_{\text{ADC}} = \frac{\text{FWC}}{2^B - 1}\]</p>
  </div>

  <div class="note-box">
    <p><strong>Note:</strong> Many camera datasheets report a <strong>saturation capacity</strong> (measured per the EMVA 1288 standard) which may differ from the nominal full well capacity. When available, use the EMVA 1288 saturation capacity as the FWC value for a more accurate conversion gain. Similarly, use the actual ADC bit depth from the datasheet (e.g. 12-bit), not the output bit depth (which may be 16-bit due to padding).</p>
  </div>
  
  <p>The recorded digital ADC counts is calculated by dividing the total generated photoelectrons by the conversion gain. Because physical digital counts are discrete and cannot be fractional, the value is rounded down to the nearest integer:</p>
  
  <div class="equation-box">
    <p>\[\text{ADC Counts} = \left\lfloor \frac{N_{e^-}}{\text{Gain}_{\text{ADC}}} \right\rfloor\]</p>
  </div>

  <h2>6. Dynamic Range and Signal-to-Noise Ratio</h2>

  <p>The <strong>dynamic range</strong> of a camera sensor quantifies the ratio between the maximum signal it can capture (saturation capacity) and the minimum signal it can distinguish from noise (read noise). It is defined as:</p>

  <div class="equation-box">
    <p>\[\text{DR}_{\text{dB}} = 20 \cdot \log_{10}\left(\frac{\text{Saturation Capacity}}{\sigma_{\text{read}}}\right)\]</p>
  </div>

  <p>where:</p>
  <ul>
    <li><strong>Saturation Capacity</strong> is the maximum number of electrons a pixel can hold before saturating (in \(\text{e}^-\)),</li>
    <li>\(\sigma_{\text{read}}\) is the temporal dark noise or read noise (in \(\text{e}^-\\)).</li>
  </ul>

  <p>Given the dynamic range and read noise, we can derive the <strong>implied saturation capacity</strong>:</p>

  <div class="equation-box">
    <p>\[\text{Saturation Capacity} = \sigma_{\text{read}} \cdot 10^{\text{DR}_{\text{dB}} / 20}\]</p>
  </div>

  <p>This serves as a useful <strong>cross-check</strong>: if the implied saturation capacity differs significantly from the FWC entered by the user, the input parameters may be inconsistent.</p>

  <h3>Signal-to-Noise Ratio (SNR)</h3>

  <p>When read noise is provided, the tool computes a simplified Signal-to-Noise Ratio for the detected signal. This indicates whether the signal is detectable above the camera's noise floor:</p>

  <div class="equation-box">
    <p>\[\text{SNR} = \frac{N_{e^-}}{\sigma_{\text{read}}}\]</p>
  </div>

  <div class="note-box">
    <p><strong>Note:</strong> This is a simplified SNR that only considers read noise. A full noise model would also include photon shot noise (\(\sqrt{N_{e^-}}\)) and dark current noise, but for the low-light signals typical of scintillator imaging, read noise is often the dominant noise source.</p>
  </div>

  <h3>Understanding Datasheet "Signal-to-Noise Ratio (typical/minimal)"</h3>

  <p>Camera datasheets (e.g., from manufacturers like Basler or Allied Vision) often list a typical "Signal-to-Noise Ratio" (such as 40 dB) alongside the "Dynamic Range" (such as 73 dB). These two metrics describe different limits of the camera:</p>
  <ul>
    <li><strong>Dynamic Range (DR)</strong> characterizes performance at the <strong>dark limit</strong> (the ratio between saturation and the noise floor).</li>
    <li><strong>Signal-to-Noise Ratio (SNR)</strong> in a datasheet characterizes performance at the <strong>bright limit</strong> (the maximum possible SNR achieved at saturation, $SNR_{\text{max}}$).</li>
  </ul>

  <p>The full SNR equation for a given signal \(S\) (in electrons) is:</p>
  <div class="equation-box">
    <p>\[\text{SNR} = \frac{S}{\sqrt{\sigma_{\text{read}}^2 + S}}\]</p>
  </div>
  <p>where the term \(S\) under the square root represents <strong>photon shot noise</strong> (which follows Poisson statistics, so its variance equals the signal itself).</p>

  <p>At the absolute limit of the sensor's capacity (when the signal equals the Saturation Capacity, \(C_{\text{sat}}\)), the shot noise dominates completely because \(C_{\text{sat}} \gg \sigma_{\text{read}}^2\). Therefore, the read noise term becomes negligible, and the maximum SNR simplifies to:</p>
  <div class="equation-box">
    <p>\[\text{SNR}_{\text{max}} \approx \frac{C_{\text{sat}}}{\sqrt{C_{\text{sat}}}} = \sqrt{C_{\text{sat}}}\]</p>
  </div>

  <p>Expressed in decibels:</p>
  <div class="equation-box">
    <p>\[\text{SNR}_{\text{max, dB}} = 20 \cdot \log_{10}(\sqrt{C_{\text{sat}}}) = 10 \cdot \log_{10}(C_{\text{sat}})\]</p>
  </div>

  <p><strong>Example:</strong> For a sensor with a Saturation Capacity of \(10.4\text{ ke}^- = 10,400\text{ e}^-\) and a Dark Noise of \(2.3\text{ e}^-\):</p>
  <ul>
    <li><strong>Dynamic Range:</strong> \(20 \cdot \log_{10}(10,400 / 2.3) \approx \mathbf{73.1\text{ dB}}\) (performance in darkness).</li>
    <li><strong>Typical SNR:</strong> \(10 \cdot \log_{10}(10,400) \approx \mathbf{40.2\text{ dB}}\) (performance at saturation).</li>
  </ul>

</div>
