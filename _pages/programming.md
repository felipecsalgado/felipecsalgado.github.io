---
layout: archive-no-title
permalink: /programming/
title: "Programming"
author_profile: true
---
{% include base_path %}
<h2 class="page__title">Programming codes</h2>
Below are some programming codes that I have developed for my projects and researches. These codes are utilized for simulating various physical processes, predicting diagnostic responses, and conducting post-processing of experimental data.

{% for post in site.programming %}
  {% include archive-single-programming.html %}
{% endfor %}
