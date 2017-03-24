# Run arguments file auto-generated on Mon Mar 20 20:21:04 2017 by:
# JobTransform: EVNTtoDAOD
# Version: $Id: trfExe.py 697822 2015-10-01 11:38:06Z graemes $
# Import runArgs class
from PyJobTransforms.trfJobOptions import RunArguments
runArgs = RunArguments()
runArgs.trfSubstepName = 'EVNTtoDAOD' 

runArgs.digiSteeringConf = 'StandardSignalOnlyTruth'
runArgs.reductionConf = ['AOD']
runArgs.pileupFinalBunch = 6
runArgs.numberOfHighPtMinBias = 0.12268057
runArgs.conditionsTag = 'OFLCOND-MC15c-SDR-09'
runArgs.postExec = ['CfgMgr.MessageSvc().setError+=["HepMcParticleLink"]']
runArgs.autoConfiguration = ['everything']
runArgs.preExec = ['rec.Commissioning.set_Value_and_Lock(True);from AthenaCommon.BeamFlags import jobproperties;jobproperties.Beam.numberOfCollisions.set_Value_and_Lock(20.0);from LArROD.LArRODFlags import larRODFlags;larRODFlags.NumberOfCollisions.set_Value_and_Lock(20);larRODFlags.nSamples.set_Value_and_Lock(4);larRODFlags.doOFCPileupOptimization.set_Value_and_Lock(True);larRODFlags.firstSample.set_Value_and_Lock(0);larRODFlags.useHighestGainAutoCorr.set_Value_and_Lock(True)']
runArgs.geometryVersion = 'ATLAS-R2-2015-03-01-00'
runArgs.numberOfCavernBkg = 0
runArgs.numberOfLowPtMinBias = 39.8773194
runArgs.postInclude = ['RecJobTransforms/UseFrontier.py']

# Explicitly added to process all events in this step
runArgs.maxEvents = -1

# Input data
runArgs.inputEVNTFile = ['../EventGeneration/test.000001.EVNT.root']
runArgs.inputEVNTFileType = 'EVNT'
runArgs.inputEVNTFileNentries = 1000L

# Output data
runArgs.outputDAOD_AODFile = 'DAOD_AOD.test.000001.AOD.root'
runArgs.outputDAOD_AODFileType = 'AOD'

# Extra runargs

# Extra runtime runargs

# Literal runargs snippets
