---
layout: archive-no-title
permalink: /attenuation-explanation/
title: "Attenuation Calculation Details"
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
  <h1 class="page__title">Photon Attenuation Calculation Details</h1>
  
  <p>This page explains the physics and mathematics behind the photon attenuation calculator. The mass interaction coefficients are obtained from the XCOM NIST database.</p>
  
  <h2>Definitions</h2>
  
  <p>Let \(\sigma_i\) (in cm<sup>2</sup>/g) be the mass interaction coefficient from XCOM for process \(i\) (e.g., pair production, scattering, or photoelectric absorption), \(\rho\) (in g/cm<sup>3</sup>) the material density, and \(t\) (in cm) the slab thickness.</p>
  
  <h2>From Mass Cross Section to Linear Attenuation</h2>
  
  <p>First, we convert each mass cross section to a linear attenuation coefficient:</p>
  
  <div class="equation-box">
    <p>\[\mu_i = \sigma_i \cdot \rho\]</p>
  </div>
  
  <p>where \(\mu_i\) is the linear attenuation coefficient for process \(i\) (in cm<sup>-1</sup>).</p>
  
  <h2>Total Attenuation</h2>
  
  <p>The total linear attenuation coefficient is the sum over all processes:</p>
  
  <div class="equation-box">
    <p>\[\mu_\text{tot} = \sigma_\text{tot} \cdot \rho = \left( \sum_i \sigma_i \right) \cdot \rho\]</p>
  </div>
  
  <p>where \(\sigma_\text{tot}\) is the total mass attenuation coefficient from the XCOM database.</p>
  
  <h2>Interaction Probabilities</h2>
  
  <p>The probability that a photon traverses the full slab without any interaction is:</p>
  
  <div class="equation-box">
    <p>\[P_\text{no interaction} = e^{-\mu_\text{tot} \, t}\]</p>
  </div>
  
  <p>The probability that a photon interacts at least once in the slab (i.e., is attenuated) is:</p>
  
  <div class="equation-box">
    <p>\[P_\text{interact} = 1 - e^{-\mu_\text{tot} \, t}\]</p>
  </div>
  
  <p>This is the <strong>attenuation</strong> displayed in the calculator. The <strong>transmission</strong> is simply \(P_\text{no interaction}\).</p>
  
  <h2>Process-Specific Probabilities</h2>
  
  <p>Since each process contributes independently and proportionally to \(\mu_\text{tot}\), the probability that a photon undergoes a specific process (given that an interaction occurred) is:</p>
  
  <div class="equation-box">
    <p>\[P_\text{pair} = \frac{\sigma_\text{pair}}{\sigma_\text{tot}} \cdot \left(1 - e^{-\mu_\text{tot} \, t}\right)\]</p>
  </div>
  
  <p>Similarly, for scattering processes:</p>
  
  <div class="equation-box">
    <p>\[P_\text{scat} = \frac{\sigma_\text{scat}}{\sigma_\text{tot}} \cdot \left(1 - e^{-\mu_\text{tot} \, t}\right)\]</p>
  </div>
  
  <p>Where the scattering cross section is the sum of coherent (Rayleigh) and incoherent (Compton) scattering:</p>
  
  <div class="equation-box">
    <p>\[\sigma_\text{scat} = \sigma_\text{coherent} + \sigma_\text{incoherent}\]</p>
  </div>
  
  <p>And the pair production includes both nuclear and electron pair production:</p>
  
  <div class="equation-box">
    <p>\[\sigma_\text{pair} = \sigma_\text{nuclear} + \sigma_\text{electron}\]</p>
  </div>
  
  <h2>Thin-Target Limit</h2>
  
  <p>In the thin-target limit where \(\mu_\text{tot} \, t \ll 1\), the exponential can be expanded to first order, giving the simplified approximations:</p>
  
  <div class="equation-box">
    <p>\[P_\text{pair} \approx \sigma_\text{pair} \cdot \rho \cdot t\]</p>
    <p>\[P_\text{scat} \approx \sigma_\text{scat} \cdot \rho \cdot t\]</p>
  </div>
  
  <div class="note-box">
    <p><strong>Note:</strong> The product \(\rho \cdot t\) is the areal density in g/cm<sup>2</sup>. Multiplying it directly by the XCOM cross section in cm<sup>2</sup>/g gives the dimensionless interaction probability.</p>
  </div>
  
  <h2>Summary</h2>
  
  <ul>
    <li><strong>Attenuation:</strong> \(1 - e^{-\mu_\text{tot} t}\) — probability that the photon interacts at least once</li>
    <li><strong>Transmission:</strong> \(e^{-\mu_\text{tot} t}\) — probability that the photon passes through without interaction</li>
    <li><strong>Process probability:</strong> \(\frac{\sigma_i}{\sigma_\text{tot}} \cdot (1 - e^{-\mu_\text{tot} t})\) — probability that the interaction is specifically process \(i\)</li>
  </ul>
  
  <p>The sum of all process-specific probabilities equals the total attenuation probability.</p>
  
</div>