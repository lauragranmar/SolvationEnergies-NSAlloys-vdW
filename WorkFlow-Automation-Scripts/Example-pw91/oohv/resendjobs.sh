#/bin/sh
jobPath=$HOME/apps/marenostrumbatch.sh


#for dir in */ 
for dir in Ag Au Co Cu Ir Ni Pd Pt Rh
do
cd $dir

cp CONTCAR POSCAR
rm WAVECAR CHG

sbatch $jobPath

cd ../



done

cd ../
