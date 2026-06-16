---
layout: archive-no-title
permalink: /research/
title: "Research"
author_profile: true

---

{% include base_path %}
<h2 class="page__title">Research</h2>
{% for post in site.research %}
  {% include archive-single-research.html %}
{% endfor %}
