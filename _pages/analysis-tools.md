---
layout: archive-no-title
permalink: /analysis-tools/
title: "Analysis & Tools"
author_profile: true
---

{% include base_path %}
<h2 class="page__title">Analysis & Tools</h2>
<p>Interactive calculators and useful programming codes that I developed to help making a quick estimates for experiments or analyze data.</p>

<style>
.analysis-cards-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-top: 30px;
  width: 100%;
  box-sizing: border-box;
}
.analysis-card {
  background: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.12);
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0,0,0,0.06), 0 1px 3px rgba(0,0,0,0.08);
  transition: box-shadow 0.25s ease, transform 0.25s ease;
  display: flex;
  flex-direction: column;
}
.analysis-card:hover {
  box-shadow: 0 10px 15px rgba(0,0,0,0.1), 0 4px 6px rgba(0,0,0,0.05);
}
.analysis-card-image-link {
  display: block;
  overflow: hidden;
  position: relative;
  aspect-ratio: 16 / 10;
  border-bottom: 1px solid rgba(0, 0, 0, 0.08);
}
.analysis-card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  display: block;
}
.analysis-card-image-link:hover .analysis-card-image {
  transform: scale(1.05);
}
.analysis-card-title-container {
  padding: 20px 15px;
  text-align: center;
  flex-grow: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fdfdfd;
}
.analysis-card-title-link {
  font-size: 1.1rem;
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none !important;
  transition: color 0.2s ease;
}
.analysis-card-title-link:hover {
  color: darkcyan !important;
}
@media (max-width: 800px) {
  .analysis-cards-container {
    grid-template-columns: 1fr;
    gap: 20px;
  }
}
</style>

<div class="analysis-cards-container">
  <!-- Card 1: Photon Attenuation -->
  <div class="analysis-card">
    <a class="analysis-card-image-link" href="{{ base_path }}/attenuation-calculator/">
      <img class="analysis-card-image" src="{{ base_path }}/images/xray-photon-att.png" alt="Photon Attenuation">
    </a>
    <div class="analysis-card-title-container">
      <a class="analysis-card-title-link" href="{{ base_path }}/attenuation-calculator/">Photon Attenuation</a>
    </div>
  </div>

  <!-- Card 2: Counts Estimation -->
  <div class="analysis-card">
    <a class="analysis-card-image-link" href="{{ base_path }}/counts-estimation/">
      <img class="analysis-card-image" src="{{ base_path }}/images/camera_counts.png" alt="Counts Estimation">
    </a>
    <div class="analysis-card-title-container">
      <a class="analysis-card-title-link" href="{{ base_path }}/counts-estimation/">Counts Estimation</a>
    </div>
  </div>

  <!-- Card 3: Programming -->
  <div class="analysis-card">
    <a class="analysis-card-image-link" href="{{ base_path }}/programming/">
      <img class="analysis-card-image" src="{{ base_path }}/images/programming.png" alt="Programming">
    </a>
    <div class="analysis-card-title-container">
      <a class="analysis-card-title-link" href="{{ base_path }}/programming/">Programming</a>
    </div>
  </div>
</div>
