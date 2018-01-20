#!/usr/bin/env bash

#tag=20171020
tag=20171025_AtlProd_19_2_5_15
maxEvents=5000
export JOBCONFIG_PATH=/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID394xxx/

#for i in {394751..394771}; do
for i in 394331; do

  jobConfig=$(ls $JOBCONFIG_PATH/ | grep ${i})
  outDS=user.jolsson.mc15_13TeV.$(echo $jobConfig | sed -r "s/\.py//g")_${tag}.root

  echo pathena --maxCpuCount 252000 --trf "Generate_tf.py --ecmEnergy=13000 --runNumber=${i} --firstEvent=%SKIPEVENTS --maxEvents=${maxEvents} --randomSeed=%RNDM:12749816 --jobConfig=$JOBCONFIG_PATH${jobConfig} --outputEVNTFile=%OUT.${i}.EVNT.pool.root" --outDS ${outDS} 
  pathena --maxCpuCount 252000 --trf "Generate_tf.py --ecmEnergy=13000 --runNumber=${i} --firstEvent=%SKIPEVENTS --maxEvents=${maxEvents} --randomSeed=%RNDM:12749816 --jobConfig=$JOBCONFIG_PATH${jobConfig} --outputEVNTFile=%OUT.${i}.EVNT.pool.root" --outDS ${outDS} 

done;
