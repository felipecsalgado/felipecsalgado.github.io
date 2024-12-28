---
layout: archive-no-title
title: "Publications"
permalink: /publications/
author_profile: true
---

A complete list of my publications, including preprint papers, can be found on [Google Scholar](https://scholar.google.de/citations?user=XFDI87QAAAAJ&hl=en) or [ResearchGate](https://www.researchgate.net/profile/Felipe-Salgado-6).

{% include base_path %}

<h2 class="page__title">Relevant Peer-Review Papers</h2>
<ol>
    {% assign sorted_publications = site.publications | sort: "path" %}
    {% for post in sorted_publications %}
    <li>{% include archive-single-publication.html %}</li>
    {% endfor %}
</ol>

<br>
<hr>
<h2 class="page__title">Patents</h2>
<ol>
    {% for post in site.patents reversed %}
    <li>{% include archive-single-patent.html %}</li>
    {% endfor %}
</ol>
