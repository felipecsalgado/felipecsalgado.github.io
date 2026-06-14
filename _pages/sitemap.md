---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---

{% include base_path %}

<p>This is a sitemap of all user-accessible pages, research projects, and tools on this website. A machine-readable <a href="{{ base_path }}/sitemap.xml">XML Sitemap</a> is also available.</p>

<div style="margin-top: 2em; line-height: 2.0; font-size: 0.95em;">
  
  <h3>Main Pages</h3>
  <ul>
    <li><a href="{{ base_path }}/">About / Home</a></li>
    <li><a href="{{ base_path }}/research/">Research Overview</a></li>
    <li><a href="{{ base_path }}/publications/">Publications &amp; Patents</a></li>
    <li><a href="{{ base_path }}/talks/">Talks &amp; Presentations</a></li>
    <li><a href="{{ base_path }}/programming/">Programming Codes</a></li>
    <li><a href="{{ base_path }}/attenuation-calculator/">Photon Attenuation Calculator</a></li>
    <li><a href="{{ base_path }}/cv/">CV / Resume</a></li>
  </ul>

  <h3>Research Projects</h3>
  <ul>
    {% for item in site.research %}
      <li><a href="{{ base_path }}{{ item.url }}">{{ item.title }}</a></li>
    {% endfor %}
  </ul>

  <h3>Programming Projects</h3>
  <ul>
    {% for item in site.programming %}
      <li><a href="{{ base_path }}{{ item.url }}">{{ item.title }}</a></li>
    {% endfor %}
  </ul>

  <h3>Scientific Tools</h3>
  <ul>
    <li><a href="{{ base_path }}/attenuation-calculator/">Photon Attenuation Calculator</a></li>
    <li><a href="{{ base_path }}/attenuation-explanation/">Photon Attenuation Calculation Details</a></li>
  </ul>

</div>
