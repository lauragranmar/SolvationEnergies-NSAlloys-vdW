#/bin/sh

add_atoms='/home/hpce17/hpce17250/apps/add_generator_WL.py'
waterxyz='../oohvPt.xyz'
functional=pbe

atoms="Ag Au Cu Ir Pd Pt Rh"

#for i in Ag Au Cu Ir Pd Pt Rh
for i in */
do
cd $i
#cp CONTCAR POSCAR
#rm -r FREQS arxiv BADER
#creates POSCAR with the additional atoms
#USE: [1]:POSCAR [2]:atoms.xyz [3]: No. atoms fixed [4]:xc

#$add_atoms POSCAR $waterxyz 6 $functional 

#cp ../vdw_kernel.bindat ./
cp ../INCAR ./

cd ../



done

cd ../
