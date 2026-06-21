---
layout: archive-no-title
permalink: /physics-tree/
title: "Physics tree"
author_profile: true
redirect_from:
  - /physics-tree
---

<style>
.physics-tree-container {
  width: 100%;
  margin: 0 auto;
  padding: 10px 0;
  box-sizing: border-box;
}
.physics-tree-card {
  background: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: 8px;
  padding: 20px 24px;
  margin-bottom: 24px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04), 0 1px 2px rgba(0, 0, 0, 0.05);
  transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
  position: relative;
  overflow: hidden;
}
.physics-tree-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.08), 0 3px 6px rgba(0, 0, 0, 0.04);
  border-color: rgba(0, 0, 0, 0.15);
}
.physics-tree-card.nobel-laureate {
  border-left: 5px solid #d4af37;
  background: linear-gradient(135deg, #ffffff 0%, #fffdf0 100%);
  border-color: rgba(212, 175, 55, 0.3) rgba(0, 0, 0, 0.08) rgba(0, 0, 0, 0.08) #d4af37;
}
.physics-tree-card.nobel-laureate:hover {
  border-color: rgba(212, 175, 55, 0.5) rgba(0, 0, 0, 0.15) rgba(0, 0, 0, 0.15) #d4af37;
}
.nobel-badge-container {
  position: absolute;
  top: 16px;
  right: 20px;
}
.nobel-medal-icon {
  width: 42px;
  height: auto;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.12));
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.physics-tree-card:hover .nobel-medal-icon {
  transform: scale(1.15) rotate(5deg);
}
.card-content-wrapper {
  width: 100%;
}
.researcher-name {
  font-size: 20px;
  font-weight: 700;
  color: #2c3e50;
  margin: 0 0 12px 0;
  padding-bottom: 6px;
  border-bottom: 1px solid #eaeaea;
  display: inline-block;
  width: 100%;
}
.nobel-laureate .researcher-name {
  color: #b08d26;
  border-bottom-color: rgba(212, 175, 55, 0.2);
  padding-right: 50px; /* Prevent overlapping with the absolute positioned medal */
}
.researcher-details {
  list-style: none;
  padding: 0;
  margin: 0;
}
.researcher-details li {
  display: flex;
  margin-bottom: 8px;
  font-size: 14px;
  line-height: 1.6;
  color: #4f5f6f;
}
.researcher-details li:last-child {
  margin-bottom: 0;
}
.detail-label {
  color: #2c3e50;
  font-weight: 600;
  flex-shrink: 0;
  width: 160px;
}
.detail-value {
  flex-grow: 1;
}
@media (max-width: 600px) {
  .researcher-details li {
    flex-direction: column;
    margin-bottom: 12px;
  }
  .detail-label {
    width: auto;
    margin-bottom: 2px;
  }
  .nobel-badge-container {
    position: static;
    display: inline-block;
    float: right;
    margin-top: -6px;
  }
  .nobel-laureate .researcher-name {
    padding-right: 0;
  }
}
</style>

<div class="physics-tree-container">
  {% include base_path %}
  <h2 class="page__title">Physics Tree</h2>
  <p>PhD supervisor and academic advisor genealogy tree.</p>
  
  <div style="margin-top: 30px;">
    <div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Felipe Salgado</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Completed PhD (Dr. rer. nat.) in <strong>2023</strong>.</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">Friedrich Schiller University Jena.</span></li>
      <li><strong class="detail-label">Supervisors:</strong><span class="detail-value">Matt Zepf.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">High-intensity laser-plasma interactions, laser-driven particle acceleration as laser wakefield acceleration. Strong-field quantum electrodynamics (SF-QED) experiments (e.g., E-320 at FACET-II and FOR2783 at CALA).</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value">Felipe Cezar Salgado, <a href="https://www.db-thueringen.de/receive/dbt_mods_00055695" target="_blank"><em>Design of a single-particle detection system for strong-field QED experiments</em></a>, Dissertation, Friedrich-Schiller-Universität Jena (2023).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Matt Zepf</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Joined as a DPhil student in 1994; Completed PhD in <strong>1997</strong>.</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Oxford.</span></li>
      <li><strong class="detail-label">Supervisor:</strong><span class="detail-value">Justin Wark.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">High-intensity laser-plasma interactions, laser-driven particle acceleration, and the generation of secondary radiation sources (X-rays, protons) from plasmas.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value">C. N. Danson <em>et al.</em>, A history of high-power laser research and development in the United Kingdom, High Power Laser Sci. Eng. <strong>9</strong>, e18 (2021). <em>(Notes Zepf as a DPhil student in Wark's group)</em>.</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Justin Wark</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Began undergraduate studies in 1979 (tutored by Paul Ewart); completed PhD in <strong>1985</strong> (Imperial College); joined the department as a Royal Society URF in 1988.</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Oxford / Imperial College London.</span></li>
      <li><strong class="detail-label">Undergraduate Tutor:</strong><span class="detail-value">Paul Ewart.</span></li>
      <li><strong class="detail-label">PhD Supervisor:</strong><span class="detail-value">Joseph D. Kilkenny.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Warm dense matter, ultra-fast X-ray science, and shock-compressed matter diagnostics. Director of the Oxford Centre for High Energy Density Science (OxCHEDS).</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value">C. N. Danson <em>et al.</em>, A history of high-power laser research and development in the United Kingdom, High Power Laser Sci. Eng. <strong>9</strong>, e18 (2021). <em>(Explicitly notes Wark was tutored by Ewart and details his doctoral and postdoctoral contributions)</em>.</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Joseph D. Kilkenny</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Completed PhD in <strong>1972</strong>.</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">Imperial College London.</span></li>
      <li><strong class="detail-label">PhD Supervisor:</strong><span class="detail-value">Robert Latham.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Inertial confinement fusion (ICF) and high-speed plasma instrumentation (e.g., x-ray streak cameras). Program Leader for ICF at Lawrence Livermore National Laboratory (LLNL).</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value">Joseph D. Kilkenny, <em>Measurement of the ion energy in a theta pinch</em>, Ph.D. Thesis, University of London (Imperial College) (1972). <em>(Explicitly notes Dr. R. Latham as his supervisor in the acknowledgements)</em>.</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Robert Latham</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Completed PhD in <strong>1946</strong> (Research Fellow at Queens' College 1945–1948).</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Cambridge (Cavendish Laboratory) / Imperial College London.</span></li>
      <li><strong class="detail-label">PhD Supervisor / Mentor:</strong><span class="detail-value">George Paget Thomson. <em>(Note: Latham began his research at Cambridge, but his post-war academic and research lineage is mapped via Sir George Paget Thomson, who recruited him for early thermonuclear fusion research at Imperial College in 1948).</em></span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Plasma physics, gas discharge, and early thermonuclear fusion research (Z-pinch). Worked on microwave radar valves during World War II.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://academictree.org/physics/peopleinfo.php?pid=844789" target="_blank">Robert Latham</a>, Physics Tree (Accessed 2026); and <a href="https://history.queens.cam.ac.uk/sites/default/files/downloads/record-1995.pdf" target="_blank">Queens' College Record 1995</a>, University of Cambridge. <em>(Obituary of Robert Latham, Research Fellow 1945–1948, p. 9; note that the same issue on p. 8 notes John Wilson Findlay, and not Latham, as Lord Rutherford's last research student, clarifying the connection).</em></span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card nobel-laureate">
  <div class="nobel-badge-container">
    <img src="/images/nobel_medal.png" class="nobel-medal-icon" alt="Nobel Medal" title="Nobel Laureate">
  </div>
  <div class="card-content-wrapper">
    <h3 class="researcher-name">George Paget Thomson</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Nobel Prize in Physics in <strong>1937</strong> (for discovering wave properties of electron by diffraction); Professor of Physics at Imperial College London (1930–1952); Master of Corpus Christi College, Cambridge (1952–1962).</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Cambridge (Cavendish Laboratory) / Imperial College London.</span></li>
      <li><strong class="detail-label">Supervisor:</strong><span class="detail-value">J. J. Thomson.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Discovered electron diffraction, worked on neutron physics, and chaired the MAUD Committee in WWII. Co-founded early thermonuclear fusion research at Imperial College.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://en.wikipedia.org/wiki/George_Paget_Thomson" target="_blank">George Paget Thomson Biography</a>, Wikipedia (Accessed 2026); and <a href="https://academictree.org/physics/peopleinfo.php?pid=74104" target="_blank">George Paget Thomson</a>, Physics Tree (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card nobel-laureate">
  <div class="nobel-badge-container">
    <img src="/images/nobel_medal.png" class="nobel-medal-icon" alt="Nobel Medal" title="Nobel Laureate">
  </div>
  <div class="card-content-wrapper">
    <h3 class="researcher-name">J. J. Thomson</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">M.A. awarded 1883 (Nobel Prize in Physics in 1906).</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Cambridge (Cavendish Laboratory).</span></li>
      <li><strong class="detail-label">Supervisor:</strong><span class="detail-value">Lord Rayleigh.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Discovered the electron and isotopes, and pioneered the mass spectrometer.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=50701" target="_blank">Joseph John Thomson</a>, Mathematics Genealogy Project (Accessed 2026); and <a href="https://academictree.org/physics/peopleinfo.php?pid=13139" target="_blank">J. J. Thomson</a>, Physics Tree (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card nobel-laureate">
  <div class="nobel-badge-container">
    <img src="/images/nobel_medal.png" class="nobel-medal-icon" alt="Nobel Medal" title="Nobel Laureate">
  </div>
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Lord Rayleigh</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">M.A. <strong>1868</strong>.</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Cambridge.</span></li>
      <li><strong class="detail-label">Tutors:</strong><span class="detail-value">Edward Routh, George Gabriel Stokes, and James Clerk Maxwell.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Formulated the theory of acoustic scattering ("Rayleigh scattering"), co-discovered Argon.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=101979" target="_blank">John William Strutt (Lord Rayleigh)</a>, Mathematics Genealogy Project (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Edward Routh</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Graduated M.A. in <strong>1857</strong>.</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Cambridge.</span></li>
      <li><strong class="detail-label">Supervisors:</strong><span class="detail-value">William Hopkins, Isaac Todhunter, and Augustus De Morgan.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Cambridge's greatest "Mathematical Coach". Formulated the Routh-Hurwitz theorem.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=101929" target="_blank">Edward John Routh</a>, Mathematics Genealogy Project (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">George Gabriel Stokes</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Graduated BA in <strong>1841</strong>.</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Cambridge.</span></li>
      <li><strong class="detail-label">Supervisor:</strong><span class="detail-value">William Hopkins.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Co-formulated the Navier-Stokes equations governing fluid dynamics.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=102483" target="_blank">George Gabriel Stokes</a>, Mathematics Genealogy Project (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">William Hopkins</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Graduated M.A. in <strong>1830</strong>.</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Cambridge.</span></li>
      <li><strong class="detail-label">Supervisor:</strong><span class="detail-value">Adam Sedgwick.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Famed "Senior-Wrangler Maker". Pioneer of physical geology.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=42016" target="_blank">William Hopkins</a>, Mathematics Genealogy Project (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Adam Sedgwick</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Graduated M.A. in <strong>1811</strong>.</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Cambridge.</span></li>
      <li><strong class="detail-label">Supervisors:</strong><span class="detail-value">Thomas Jones and John Dawson.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Founder of modern geology. Proposed the Cambrian and Devonian periods.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=102043" target="_blank">Adam Sedgwick</a>, Mathematics Genealogy Project (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Thomas Jones</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Graduated M.A. in <strong>1782</strong> (B.A. in 1779).</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Cambridge (Trinity College).</span></li>
      <li><strong class="detail-label">Supervisor:</strong><span class="detail-value">Thomas Postlethwaite.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Head Tutor at Trinity College, Cambridge. Famed for his lectures on mathematics and his influence on many Cambridge scholars including Adam Sedgwick.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=102036" target="_blank">Thomas Jones</a>, Mathematics Genealogy Project (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Thomas Postlethwaite</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Graduated M.A. in <strong>1756</strong> (B.A. in 1753).</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Cambridge (Trinity College).</span></li>
      <li><strong class="detail-label">Supervisor:</strong><span class="detail-value">Stephen Whisson.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Master of Trinity College, Cambridge.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=133301" target="_blank">Thomas Postlethwaite</a>, Mathematics Genealogy Project (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Stephen Whisson</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Graduated M.A. in <strong>1742</strong> (B.A. in 1738).</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Cambridge (Trinity College).</span></li>
      <li><strong class="detail-label">Supervisor:</strong><span class="detail-value">Walter Taylor.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Tutor and Senior Fellow at Trinity College, Cambridge. University Librarian.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=133367" target="_blank">Stephen Whisson</a>, Mathematics Genealogy Project (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Walter Taylor</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Graduated M.A. in <strong>1723</strong>.</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Cambridge (Trinity College).</span></li>
      <li><strong class="detail-label">Supervisor:</strong><span class="detail-value">Robert Smith.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Regius Professor of Greek and Tutor at Trinity College, Cambridge.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=133368" target="_blank">Walter Taylor</a>, Mathematics Genealogy Project (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Robert Smith</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Graduated M.A. in <strong>1715</strong> (B.A. in 1711).</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Cambridge.</span></li>
      <li><strong class="detail-label">Supervisor:</strong><span class="detail-value">Roger Cotes.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Published <em>A Compleat System of Opticks</em> (1738). Succeeded Cotes as Plumian Professor. Founded the Smith's Prizes.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=103068" target="_blank">Robert Smith</a>, Mathematics Genealogy Project (Accessed 2026); and <a href="https://en.wikipedia.org/wiki/Robert_Smith_(mathematician" target="_blank">Robert Smith Biography</a>), Wikipedia (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Roger Cotes</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Graduated M.A. in <strong>1706</strong> (B.A. in 1702).</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Cambridge.</span></li>
      <li><strong class="detail-label">Supervisor:</strong><span class="detail-value">Sir Isaac Newton.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Collaborated with Newton to edit the second edition of the <em>Principia</em>. First Plumian Professor.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=103067" target="_blank">Roger Cotes</a>, Mathematics Genealogy Project (Accessed 2026); and <a href="https://mathshistory.st-andrews.ac.uk/Biographies/Cotes/" target="_blank">Roger Cotes Biography</a>, MacTutor History of Mathematics Archive (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Sir Isaac Newton</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Graduated M.A. in <strong>1668</strong> (B.A. in 1665).</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Cambridge.</span></li>
      <li><strong class="detail-label">Supervisors/Tutors:</strong><span class="detail-value">Isaac Barrow and Benjamin Pulleyn.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Formulated the laws of motion and universal gravitation. Lucasian Professor.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=74313" target="_blank">Isaac Newton</a>, Mathematics Genealogy Project (Accessed 2026); and <a href="https://mathshistory.st-andrews.ac.uk/Biographies/Newton/" target="_blank">Isaac Newton Biography</a>, MacTutor History of Mathematics Archive (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Isaac Barrow</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Graduated M.A. in <strong>1652</strong> (B.A. in 1648).</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Cambridge / Independent study in Italy.</span></li>
      <li><strong class="detail-label">Mentor:</strong><span class="detail-value">Vincenzo Viviani.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Pioneer of calculus. First to state the Fundamental Theorem of Calculus. First Lucasian Professor.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=67643" target="_blank">Isaac Barrow</a>, Mathematics Genealogy Project (Accessed 2026); and <a href="https://mathshistory.st-andrews.ac.uk/Biographies/Barrow/" target="_blank">Isaac Barrow Biography</a>, MacTutor History of Mathematics Archive (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Vincenzo Viviani</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Became a pupil to Galileo in <strong>1639</strong>.</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">Court of the Grand Duke of Tuscany.</span></li>
      <li><strong class="detail-label">Supervisor:</strong><span class="detail-value">Galileo Galilei.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">First to accurately determine the speed of sound. Reconstructed Apollonius's lost work <em>De locis planis</em>. Served as Galileo's last pupil and biographer.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=133302" target="_blank">Vincenzo Viviani</a>, Mathematics Genealogy Project (Accessed 2026); and <a href="https://mathshistory.st-andrews.ac.uk/Biographies/Viviani/" target="_blank">Vincenzo Viviani Biography</a>, MacTutor History of Mathematics Archive (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Galileo Galilei</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Student starting in <strong>1581</strong>.</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">University of Pisa.</span></li>
      <li><strong class="detail-label">Supervisor:</strong><span class="detail-value">Ostilio Ricci.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Championed heliocentrism, discovered the four largest moons of Jupiter, formulated the basic law of falling bodies.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=134975" target="_blank">Galileo Galilei</a>, Mathematics Genealogy Project (Accessed 2026); and <a href="https://mathshistory.st-andrews.ac.uk/Biographies/Galileo/" target="_blank">Galileo Galilei Biography</a>, MacTutor History of Mathematics Archive (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Ostilio Ricci</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Court Mathematician in the late 1500s.</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">Court of Francesco I de' Medici.</span></li>
      <li><strong class="detail-label">Supervisor:</strong><span class="detail-value">Nicolò Tartaglia.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Mathematician and military engineer. Convinced Galileo's father to let him study mathematics.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=136245" target="_blank">Ostilio Ricci</a>, Mathematics Genealogy Project (Accessed 2026); and <a href="https://en.wikipedia.org/wiki/Ostilio_Ricci" target="_blank">Ostilio Ricci Biography</a>, Wikipedia (Accessed 2026).</span></li>
    </ul>
  </div>
</div>

<div class="physics-tree-card">
  <div class="card-content-wrapper">
    <h3 class="researcher-name">Nicolò Tartaglia</h3>
    <ul class="researcher-details">
      <li><strong class="detail-label">Timeline:</strong><span class="detail-value">Active throughout the early to mid-1500s (Died 1557).</span></li>
      <li><strong class="detail-label">Institute:</strong><span class="detail-value">Venice / Verona.</span></li>
      <li><strong class="detail-label">Main research:</strong><span class="detail-value">Discovered the general algebraic solution for cubic equations. Published the first Italian translations of Euclid and Archimedes.</span></li>
      <li><strong class="detail-label">Source:</strong><span class="detail-value"><a href="https://www.mathgenealogy.org/id.php?id=136514" target="_blank">Nicolo Tartaglia</a>, Mathematics Genealogy Project (Accessed 2026); and <a href="https://mathshistory.st-andrews.ac.uk/Biographies/Tartaglia/" target="_blank">Nicolo Tartaglia Biography</a>, MacTutor History of Mathematics Archive (Accessed 2026).</span></li>
    </ul>
  </div>
</div>
  </div>
</div>
