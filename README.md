# SolvationEnergies-NSAlloys-vdW

This repository contains data, plots, and an examples of the calculations associated with the open access paper ["Influence of Van der Waals Interactions on the Solvation Energies of Adsorbates at Pt-Based Electrocatalysts"](<https://t.co/18eeZ6WdTg>)

This manuscript can also be found as the [second chapter of my thesis.](https://scholarlypublications.universiteitleiden.nl/access/item%3A3217524/view)

## Code requirements

Python 2.7

ASE 3.15 ( compatible version for Py2.7)

VTST tools

### DATA

Contains all the data used in .txt format.

### Plots

Each folder contains the data, and python scripts that creates the figures represented as in the thesis.

### Workflow-Automation-Scripts

#### Example 
Folder containing files from one set of simulations. Useful as a reference.

* The output directories, BADER, arxiv, and FREQS are created automatically after running the modified version of the cleaning script from the vtst tools.

* If there is only a file in the FREQS dir, that means that frequency analysis was not run.

#### Input-Generation-Scripts

* Pt111r3xr3_4l_runterminal.py -Prepares the surface slab.

* create_nsas_pw91.sh -Creates working directories accordingly.

#### Postprocessing

* Some example scripts to get the data from the calculations.
