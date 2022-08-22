#/bin/sh

createinputs='/home/laura/apps/postprocess-lpg/createinputs_contcar_functional.py'

functional=pbe #creted using pbe but copying INCAR with right functional description for pw91. Lattice consntan = 3.988 at the end of this file. 
#This was done becauese the POTCAR file path is under PBE/POTCAR but changing the parameter xc in the INCAR changes the simulation to the right paramenters accordingly to the xc

atoms="Ag Au Co Cu Ni Ir Pd Pt Rh"

for i in $atoms
do
mkdir $i
cd $i

cat > POSCAR << !
Pt $i
 1.0000000000000000
     4.8842825471096578    0.0000000000000004    0.0000000000000000
     2.4421412735548289    4.2299127650579278    0.0000000000000000
     0.0000000000000000    0.0000000000000000   22.1074186205846814
  9 3
Selective dynamics
Direct
  0.3028641450980831  0.4941068991457977  0.0020938984688560   F   F   F
  0.6361974779028985  0.8274402320805470  0.0020938984688560   F   F   F
  0.9695308121633338  0.1607735650152964  0.0020938984688560   F   F   F
  0.6361974779462100  0.4941068991457977  0.1062432299451289   F   F   F
  0.9695308122066451  0.8274402320805471  0.1062432299451289   F   F   F
  0.3028641450114607  0.1607735650152964  0.1062432299451289   F   F   F
  0.3028641450980831  0.4941068991457977  0.3145418933500113   T   T   T
  0.6361974779028985  0.8274402320805470  0.3145418933500113   T   T   T
  0.9695308121633338  0.1607735650152964  0.3145418933500113   T   T   T
  0.9695308122499563  0.4941068991457978  0.2103925618737385   T   T   T
  0.3028641450547718  0.8274402320805470  0.2103925618737385   T   T   T
  0.6361974778595875  0.1607735650152962  0.2103925618737385   T   T   T
!

$createinputs POSCAR 6 $functional

cp ../INCAR ./

#sbatch -J $name $jobPath


cd ../



done

cd ../
