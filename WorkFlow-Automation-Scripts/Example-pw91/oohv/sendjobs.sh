#/bin/sh
jobPath=$HOME/apps/marenostrumbatch.sh


for dir in */ 
do
cd $dir


sbatch $jobPath

cd ../



done

cd ../
