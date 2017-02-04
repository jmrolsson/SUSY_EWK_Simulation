# SUSY_EWK_Simulation
Generate signal Monte Carlo for ATLAS Run II SUSY electroweak Wh physics search

## Generating EVNT files
All the necessary files for generating event (both locally and on the grid) are available in 'EventGeneration'

### Setup
```
git clone https://github.com/jmrolsson/SUSY_EWK_Simulation
cd EventGeneration
setupATLAS
lsetup panda
asetup AtlasProduction,19.2.5.15
```

### Running locally
Example:
```
Generate_tf.py --ecmEnergy=13000 --runNumber=000001 --maxEvents=1000 --jobConfig=MC15.000001.MGPy8EG_A14N23LO_C1N2_WZ_500p0_200p0_bbqq_J10.py --outputEVNTFile=test.000001.EVNT.root
```

### Submitting jobs to the GRID
python submit_Generate_tf_MG_C1N2_WZ_Wh.py  

## Going from EVNT to TRUTH xAODs

### Running locally
Example:
(Recommend doing this in separate directory from the setup for generating EVNT above)
```
asetup 20.1.8.3,AtlasDerivation,gcc48,here
Reco_tf.py --inputEVNTFile test1.000001.EVNT.root --outputDAODFile test1.000001.TRUTH1.root --reductionConf TRUTH1
```

### Submitting jobs to the GRID
python submit_Reco_tf_TRUTH.py
