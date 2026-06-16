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
  
  <p>Let \(\sigma_i\) (in cm<sup>2</sup>/g) be the mass interaction coefficient from XCOM for process \(i\), \(\rho\) (in g/cm<sup>3</sup>) the material density, and \(t\) (in cm) the slab thickness.</p>

  <p>The calculator breaks interactions down into the following five core physical processes:</p>
  <ul>
    <li><strong>Rayleigh Scattering</strong> (Coherent Scattering)</li>
    <li><strong>Compton Scattering</strong> (Incoherent Scattering)</li>
    <li><strong>Photoelectric Absorption</strong></li>
    <li><strong>Nuclear Field Pair Production</strong></li>
    <li><strong>Electron Field Pair Production</strong></li>
  </ul>
  
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
  
  <p>where \(\sigma_\text{tot}\) is the total mass attenuation coefficient.</p>
  
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
  
  <h2>Process-Specific Absolute Probabilities</h2>
  
  <p>Since each process contributes independently and proportionally to \(\mu_\text{tot}\), the absolute probability that a photon entering the material will undergo a specific process \(i\) across the total material length is calculated by multiplying the relative fraction of the interaction by the total interaction probability:</p>
  
  <div class="equation-box">
    <p>\[P_i = \frac{\sigma_i}{\sigma_\text{tot}} \cdot \left(1 - e^{-\mu_\text{tot} \, t}\right)\]</p>
  </div>

  <p>For example, the absolute probability of Photoelectric Absorption is:</p>
  <div class="equation-box">
    <p>\[P_\text{photoelectric} = \frac{\sigma_\text{photoelectric}}{\sigma_\text{tot}} \cdot \left(1 - e^{-\mu_\text{tot} \, t}\right)\]</p>
  </div>

  <p>Because these represent absolute macroscopic probabilities across the slab thickness, the sum of all process-specific probabilities exactly equals the total <strong>attenuation</strong> probability.</p>

  <h2>Data Interpolation and Absorption Edges</h2>

  <p>The calculator evaluates coefficients for exact photon energies dynamically. However, since the NIST XCOM database contains discrete datapoints, values between these points must be interpolated. Because photon cross sections follow steep non-linear power laws across energy magnitudes, standard linear interpolation introduces severe physical errors.</p>
  
  <p>Instead, the tool employs a <strong>Log-Log Linear Interpolation</strong> algorithm. For any target energy, it locates the two closest discrete energy points in the NIST database and performs a linear interpolation in log-log space. This choice matches the power-law scaling of photon cross sections across energy ranges and prevents the severe physical errors of simple linear interpolation.</p>

  <p>To handle absorption edges (such as K-edges and L-edges), the NIST XCOM database contains pairs of points placed extremely close to each other at the discontinuity. The log-log interpolation natively handles these sharp transitions, ensuring accurate values immediately below and above the binding energy thresholds.</p>

  <h2>Compounds and Bragg's Additivity Rule</h2>

  <p>For molecular compounds and complex materials (e.g., Kapton, Water, Lanex), the calculator natively fuses atomic components using <strong>Bragg's Additivity Rule</strong>. The total mass attenuation coefficient for a compound is derived by summing the independent coefficients of its constituent elemental components, appropriately weighted by their proportional mass fractions (\(w_j\)):</p>

  <div class="equation-box">
    <p>\[\left(\frac{\mu}{\rho}\right)_{\text{compound}} = \sum_j w_j \left(\frac{\mu}{\rho}\right)_j\]</p>
  </div>
  
  <p>where the fractional weight \(w_j\) of element \(j\) in the molecule is defined by the number of atoms \(n_j\), the atomic mass \(A_j\), and the total molecular mass \(M_\text{total}\):</p>

  <div class="equation-box">
    <p>\[w_j = \frac{n_j \cdot A_j}{M_\text{total}}\]</p>
  </div>
  
  <h2>Summary</h2>
  
  <ul>
    <li><strong>Attenuation:</strong> \(1 - e^{-\mu_\text{tot} t}\) — probability that the photon interacts at least once</li>
    <li><strong>Transmission:</strong> \(e^{-\mu_\text{tot} t}\) — probability that the photon passes through without interaction</li>
    <li><strong>Process probability:</strong> \(\frac{\sigma_i}{\sigma_\text{tot}} \cdot (1 - e^{-\mu_\text{tot} t})\) — probability that the interaction is specifically process \(i\)</li>
  </ul>
  
</div>
