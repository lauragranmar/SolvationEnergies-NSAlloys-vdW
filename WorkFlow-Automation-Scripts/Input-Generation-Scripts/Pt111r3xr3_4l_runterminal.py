#! /usr/bin/env python
__author__ = 'lauragranda'
""" 
Creates a  slab of root3xroot3 R30  with fcc  111 plane. See ASE doucmentation for more info.
Generates the POSCAR INCAR KPOINT POTCAR files.
This script takes two arguments 1. optimized lattice cosntant 2.xc= exchange correlation functional 
script.py latticeconstant(int) xc
"""

from ase import Atoms, Atom
import numpy as np
from ase.io import write, read
from ase.calculators.vasp import *
from ase.constraints import *
from ase.build import fcc111, root_surface
import sys

#Info for POSCAR
latticeconstant= float(sys.argv[1])

slab = fcc111('Pt', size=(1,1,4), a=latticeconstant, vacuum=7.6)
slab = root_surface(slab, 3)
slab.center(about=3.5)

#Setting constraints for the optimization. The two bottom layers of the slab are fixed r3xr3 = 3 atoms per layer.
slab.set_constraint(FixAtoms(indices=range( 6 ) ) )
#Info for kpoints
lenghts= slab.get_cell_lengths_and_angles()
#To determine the kpoints a rule of thumb is to say that the normal of the lattice vector * Kpoint (>=) 30
#However in reality kpoint shoulb be tested through convergence tests.
#KPOINTS are set to be 8x8x1 
#the following code is left as an example.
kpoint = 30.0/lenghts[0:2]
kpointx = round(30.0/lenghts[0],0)
kpointy = round(30.0/lenghts[1],0)

##INPUT CREATOR PARAMETERS##
xc = str(sys.argv[2])
calc = Vasp (xc= xc, gamma=False, kpts=(8, 8, 1),
             istart=0,
             iniwav=1,
             icharg=2,
             encut=450,
             ldipol=True,
             idipol=3,
             lcharg=True, # this is important for postprocessing of bader partiacl charges with vtst bader program.
             ncore= 8,
             ibrion=1,
             potim=0.2,
             algo='NORMAL',
             ismear=2,
             sigma=0.2,
             nelmin=8,
             nsw=1500,
             ediff=1.0e-6,
             ediffg= -0.01)
calc.calculate(slab)
calc.write_potcar()


