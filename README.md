---
title: Overview of "Featural Relations and Identicality in Concept Learning"
---

If you have any questions about any of this, I can be contacted at mwetzel2 -at- binghamton.edu. 

UNLICENSE: Any of the figures, materials, & experiment code may be used/edited without permission, though credit is always welcomed :)


# Basic Organization

<!-- - `manuscript.md` paper as a markdown file -->
- `.bib` bibtex of all the references used in the paper (with duplicates and orphans)
- `figures` contains all the figures used for the manuscript. 
- `materials & analysis`: each experiment contains a `analysis` folder and a `materials` folder
    - `analysis`: everything needed to replicate the analyses and reproduce the figures (all of it written in python)
        - each experiment contains a `scrape` file that aggregates data from the `materials` folder into an easier-to-manage set of datafiles
        - scripts to reproduce the specific inferential analysis in the paper are labeled "inferential - "
    - `materials`: everything needed to run the experiments + stimuli & the scripts to generate them
        - experiments 1, 2, and 3 are written in html/javascript (using the [oCanvas Library](http://ocanvas.org/)) that can be run as standalone experiment with a browser or embedded in a webserver to run online
        - experiment 4 is written in python using the [PsychoPy](https://www.psychopy.org/) library <-- it was conducted a year prior to experiments 1, 2, and 3, for a different project

# Software & Dependencies

For running the analyses & plots:
    - Python +:
        - numpy
        - scipy
        - matplotlib

For running the experiments:
    - HTML/Javascript [experiments 1, 2, & 3]
    - Python + Psychopy [experiment 4]
        - plus matplotlib for stimulus generation

---

If something breaks feel free to reach out