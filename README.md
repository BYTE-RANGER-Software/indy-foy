![Status](https://img.shields.io/badge/status-Pre--Pre--Production-yellow)
![License](https://img.shields.io/badge/license-CC%20BY--SA%204.0-blue)
[![Project Maintenance](https://img.shields.io/maintenance/yes/2025.svg)](https://github.com/BYTE-RANGER-Software/indy-foy 'GitHub Repository')

# Fountain of Youth (FoY)

> **Non-profit fan point-and-click adventure inspired by *Indiana Jones* — continued by BYTE RANGER Software.**

---

## Table of Contents
- [About the Project](#about-the-project)
- [Status](#status)
- [Website](#website)
- [Features](#features)
- [Screenshots](#screenshots)
- [Releases & Nightly Builds](#releases--nightly-builds)
- [Roadmap](#roadmap)
- [Roadmap Progress](#roadmap-progress)
- [Contributing](#contributing)
- [Development Setup](#development-setup)
- [Repository Layout](#repository-layout)
- [License](#license)
- [Legal Notice](#legal-notice)
- [Attribution & Credits](#attribution--credits)
- [Contact](#contact)

---

## About the Project
**Fountain of Youth** is a non-commercial fan adventure in classic LucasArts style.  
This repository hosts the **active continuation by BYTE RANGER Software**: planning, source/assets, builds, and documentation.

📖 For a detailed **project history** see the [Project Website → History](https://BYTE-RANGER-Software.github.io/indy-foy/#history).

## Status
🚧 Early pre-pre-production.  
We are currently focusing on collecting and archiving original materials related to FOY.  
Next step: Creation and completion of the GDD (Game Design Document).

## Website
Project website is published via **GitHub Pages**.
- **URL:** https://BYTE-RANGER-Software.github.io/indy-foy/
- Source for the site lives in `docs/` (see [Repository Layout](#repository-layout)).

## Features
- Classic point-and-click mechanics (verb UI / inventory)
- Story-driven puzzles, exploration, and action
- Original music & SFX
- Chapters include **Bimini, Europe & Asia**
- Over **150 hand-drawn backgrounds** in retro low-res look
- Classic **“Atlantis”-style GUI** & mechanics
- Antiquities, sidekicks & leather jackets!

> *Note:* The exact feature set depends on the current AGS implementation stage.

## Screenshots

<p align="center">
  <a href="docs/assets/screenshot-1.jpg">
    <img src="docs/assets/screenshot-1.jpg" alt="Screenshot 1" width="46%" />
  </a>
  <a href="docs/assets/screenshot-2.jpg">
    <img src="docs/assets/screenshot-2.jpg" alt="Screenshot 2" width="46%" />
  </a>
</p>

> Click to view full size.  
> Files are mirrored on the website under `/indy-foy/assets/`.

## Releases & Nightly Builds
Verified releases appear on the **GitHub Releases** page.

| File | Version | Date | SHA-256 |
|------|---------|------|---------|
|  –   |    –    |  –   |    –    |

*(Nightly builds may be pre-releases and unstable.)*

## Roadmap

- **M00 — Pre-Pre-Production / Discovery & Preservation**  
  Collect prior materials into `originals/` (with SHA-256 + source).  
  Draft `ATTRIBUTION.md` document.  
  Create or complete `docs/GDD.xlsx` (Game Design Document – includes game concept, storyline, mechanics, room design, art & sound, UI, technical aspects, project details).  
  Optionally prepare a dedicated Room Design Document if needed.

- **M01 — Pre-Production / Vertical Slice Tech**  
  AGS project @ 640×400 (nearest-neighbour, aspect lock).  
  One test room (walkable / walk-behind).  
  Verb-UI & inventory stub, one hotspot interaction, short dialog.  
  Packaged build + nightly ZIP.  

- **M02 — Core Gameplay Systems**  
  Implement room transitions & pathfinding.  
  Hotspots, objects & inventory flow.  
  Basic dialog system.  
  Save/load system.  
  Blocking volumes & options menu.  

- **M03 — Content Production I: (Public Demo)**  
  3–6 rooms, 5–8 puzzles.  
  One mini-cutscene.  
  First audio pass (music & SFX).  
  QA & packaging for public demo release.  

- **M04 — Content Production II: Main Chapters**  
  Expand rooms, puzzles & story progression.  
  Implement additional characters & animations.  
  Intermediate builds for internal testing.  

- **M05 — Alpha (Feature Complete)**  
  All core mechanics & chapters implemented.  
  Placeholder graphics/audio replaced by finals.  
  Full playthrough possible (bugs expected).  

- **M06 — Beta (Closed Testing)**  
  Bugfixing, balancing of puzzles & difficulty.  
  Performance optimization.  
  External testers (closed group) with feedback loop.  

- **M07 — Release Candidate (RC)**  
  All assets, features, and texts finalized.  
  Translations/localization where applicable.  
  Packaging & installer.  
  Marketing material (trailer, screenshots).  

- **M08 — Release 1.0**  
  Public launch of the full game.  
  Distribution via GitHub, itch.io, etc.  
  Announcements & community posts.  

- **M09 — Post-Release Support**  
  Patches & hotfixes.  
  Possible bonus content.  
  Documentation & optional open-source release.  

## Roadmap Progress

- 🚧[M00 — Pre-Pre-Production / Discovery & Preservation](https://github.com/BYTE-RANGER-Software/indy-foy/milestone/1)  
- ☐ [M01 — Pre-Production / Vertical Slice Tech](https://github.com/BYTE-RANGER-Software/indy-foy/milestone/2)  
- ☐ [M02 — Core Gameplay Systems](https://github.com/BYTE-RANGER-Software/indy-foy/milestone/3)  
- ☐ [M03 — Content Production I: Bimini Prologue](https://github.com/BYTE-RANGER-Software/indy-foy/milestone/4)  
- ☐ [M04 — Content Production II: Main Chapters](https://github.com/BYTE-RANGER-Software/indy-foy/milestone/5)  
- ☐ [M05 — Alpha (Feature Complete)](https://github.com/BYTE-RANGER-Software/indy-foy/milestone/6)  
- ☐ [M06 — Beta (Closed Testing)](https://github.com/BYTE-RANGER-Software/indy-foy/milestone/7)  
- ☐ [M07 — Release Candidate](https://github.com/BYTE-RANGER-Software/indy-foy/milestone/8)  
- ☐ [M08 — Release 1.0](https://github.com/BYTE-RANGER-Software/indy-foy/milestone/9)  
- ☐ [M09 — Post-Release Support](https://github.com/BYTE-RANGER-Software/indy-foy/milestone/10)  

> Legend:
>- ✅ Done  
>- 🚧 In Progress  
>- ☐ To Do 

👉 See [Issues → Milestones](https://github.com/BYTE-RANGER-Software/indy-foy/milestones) for live progress tracking.

## Contributing
Contributions are possible **after prior coordination**.  
Please open an Issue first and describe your proposal. Uncoordinated PRs may be declined.

1. Open an Issue (goal, scope, sample art/mocks if available)  
2. After approval: branch `feature/<short-description>`  
3. Open PR; link the Issue; attach screenshots/GIFs  
4. Use **Git LFS** for large sources only

## Development Setup
- **Engine/Framework:** **AGS (Adventure Game Studio)**
- **Dependencies:** _TBA_  
- **Build:** AGS Editor → “Build / Rebuild” or “Save compiled game”  
- **Run:** Execute the compiled game

### Rendering & Resolution
- **Native:** 640×400 (16:10), crisp pixels, nearest-neighbour scaling  
- Aspect-preserving integer scaling for 1280×800 / 1920×1200  
- Optional pipeline: draw masters at 1280×800 and downscale for current builds

## Repository Layout
```
design/                     # 
docs/                       # GitHub Pages (Website)
    index.html
    main.js
    assets/
        logo.png
        main.png
        slider_bg.png
        downloads/
originals/
src/                        # new game source code
  ags/
  assets/
```

## License
Unless otherwise noted, all contents are licensed under  
**Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**.  
Full license text: https://creativecommons.org/licenses/by-sa/4.0/

## Legal Notice
This is a **non-commercial fan project**.

“Indiana Jones”™ and related properties are trademarks of **Lucasfilm Ltd.**  
This project is **not affiliated with or endorsed by Lucasfilm, Disney, or Screen 7**.  
All other trademarks are the property of their respective owners.

Unless otherwise noted, repository contents are provided under **CC BY‑SA 4.0**.
If you are a rights holder and have concerns, please contact us: ByteRanger@gmx.de.


## Attribution & Credits
See **[ATTRIBUTION.md](ATTRIBUTION.md)** for sources, acknowledgments, and detailed credits.  
Maintainer: **BYTE RANGER Software (CalDymos)**

## Contact
- **Issues:** https://github.com/BYTE-RANGER-Software/indy-foy/issues  
- **E-mail:** ByteRanger@gmx.de  
- **Project website:** https://BYTE-RANGER-Software.github.io/indy-foy/

