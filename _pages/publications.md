---
layout: archive-no-title
title: "Publications"
permalink: /publications/
author_profile: true
---

<div class="main-content" style="width: 100%;">
    <p>A complete list of my publications, including preprint papers, can be found on <a href="https://scholar.google.de/citations?user=XFDI87QAAAAJ&hl=en">Google Scholar</a> or <a href="https://www.researchgate.net/profile/Felipe-Salgado-6">ResearchGate</a>.</p>

    <h2 class="page__title">Relevant Peer-Review Papers</h2>
    <ol>
        {% assign sorted_publications = site.publications | where: "venue", "paper" | sort: "date" | reverse %}
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
  </div>
