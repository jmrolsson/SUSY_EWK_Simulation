# SUSY_EWK_Simulation
Scripts for running ATLAS Monte Carlo simulation jobs, locally and on the grid (event generation, detector simulation, reconstruction, and DxAOD derivation). Used for validation of signal samples for the ATLAS Run II SUSY electroweak W h/Z all-hadronic physics search.

## Checking out the code and setting up the infrastructure
```
git clone https://github.com/jmrolsson/SUSY_EWK_Simulation
setupATLAS
lsetup panda
mkdir SUSY_EWK_Simulation/Test
```

## Generating events (creating EVNT files)
All the necessary files for generating event (both locally and on the grid) are available in 'EventGeneration'

### Setup
```
cd SUSY_EWK_Simulation/EventGeneration
asetup AtlasProduction,19.2.5.15,here
```

### Testing locally
Example:
```
Generate_tf.py --ecmEnergy=13000 --runNumber=000001 --maxEvents=1000 --jobConfig=MC15.000001.MGPy8EG_A14N23LO_C1N2_WZ_500p0_200p0_bbqq_J10.py --outputEVNTFile=../Test/test.000001.EVNT.root
```

### Submitting jobs to the GRID
Modify the file 'submit_Generate_tf_MG_C1N2_WZ_Wh.py' according to your needs, then run:
```
python submit_Generate_tf_MG_C1N2_WZ_Wh.py  
```

## Creating 'TRUTH' samples (Going from EVNT to TRUTH xAODs)

### Setup
```
cd SUSY_EWK_Simulation/TRUTH
asetup AtlasDerivation,20.1.8.3,here
```

### Testing locally
Example:
```
Reco_tf.py --inputEVNTFile ../Test/test.000001.EVNT.root --outputDAODFile ../Test/test.000001.TRUTH1.root --reductionConf TRUTH1 # or 'TRUTH3'
```

### Submitting jobs to the GRID
Modify the file 'python submit_Reco_tf_TRUTH.py' to specify what EVNT files you are running over, name of your output datasets, etc... then run:
```
python submit_Reco_tf_TRUTH.py
```

## Running the detector simulation (Going from EVNT to HITS)

### Setup
```
cd SUSY_EWK_Simulation/Simulation
asetup AtlasDerivation,19.2.4.9,here
```

### Testing locally
Example:
```
Sim_tf.py --maxEvents 50 --inputEVNTFile ../Test/test.000001.EVNT.root --outputHITSFile ../Test/test.000001.HITS.root 
```

Example (with AMI-tag s2726 options):
```
Sim_tf.py --maxEvents 50 --inputEVNTFile ../Test/test.000001.EVNT.root --outputHITSFile ../Test/test.000001.HITS.root --DBRelease "default:current" --DataRunNumber 222525 --conditionsTag "default:OFLCOND-RUN12-SDR-19" --geometryVersion "default:ATLAS-R2-2015-03-01-00_VALIDATION" --physicsList FTFP_BERT --postInclude "default:PyJobTransforms/UseFrontier.py" --preInclude "EVNTtoHITS:SimulationJobOptions/preInclude.BeamPipeKill.py,SimulationJobOptions/preInclude.FrozenShowersFCalOnly.py" --simulator MC12G4 --truthStrategy MC15aPlus --AMITag r7772
```

### Submitting jobs to the GRID
Modify the file 'python submit_Sim_tf.py' to specify what EVNT files you are running over, name of your output datasets, etc... then run:
```
python submit_Sim_tf.py
```

## Runing reconstruction (Going from HITS to AOD)

### Setup
```
cd SUSY_EWK_Simulation/Reconstruction
asetup AtlasDerivation,20.7.5.1,here
```

### Testing locally
Example:
```
Reco_tf.py --inputHITSFile ../Test/test.000001.HITS.root --outputAODFile ../Test/test.000001.AOD.root
```

### Submitting jobs to the GRID
Modify the file 'python submit_Reco_tf.py' to specify what HITS files you are running over, name of your output datasets, etc... then run:
```
python submit_Reco_tf.py
```

## Creating the physics derivation (Going from AOD to DxAOD)

### Setup
```
cd SUSY_EWK_Simulation/Derivation
asetup 20.7.X.Y-VAL,rel_n,AtlasDerivation,here --nightliesarea=/afs/cern.ch/atlas/software/builds/nightlies # replace n in rel_n by the number (ex. 2) of the nightly you would like to setup
```

### Testing locally
Example:
```
Reco_tf.py --inputAODFile ../Test/test.000001.AOD.root --outputDAODFile ../Test/test.000001.DAOD.root --reductionConf SUSY10 # replace SUSY10 with whatever derivation you need
```

### Submitting jobs to the GRID
Modify the file 'python submit_Reco_derivation_tf.py' to specify what AOD files you are running over, name of your output datasets, etc... then run:
```
python submit_Reco_derivation_tf.py
```
