#! /usr/bin/env python
import subprocess as sp
import re

# <<---- JOB SETUP -------------------------------------------------------------

nFiles = 1
nFilesPerJob = 1
nEventsPerJob = 1

maxCpuCount = 252000 # 70 hrs

tag = '20170322_2.3.test'
user = 'jolsson'

doBuild = True
doBuildAll = False

inDSs = ['user.jolsson.mc15_13TeV.000005.MGPy8EG_A14N23LO_C1N2_WZ_150p0_0p0_bbqq_J10.HITS.20170322_2.3_EXT0']

outDSs = ['mc15_13TeV.000005.MGPy8EG_A14N23LO_C1N2_WZ_150p0_0p0_bbqq_J10.AOD']

# >>---------------------------------------------------------------------------

setup = '--nFiles '+str(nFiles)+' --nFilesPerJob '+str(nFilesPerJob)+' --nEventsPerJob '+str(nEventsPerJob)+' --maxCpuCount '+str(maxCpuCount)+' --useNewTRF --trf "Reco_tf.py --inputHITSFile %IN --outputAODFile %OUT.pool.root --maxEvents '+str(nEventsPerJob)+' --conditionsTag \'default:OFLCOND-MC15c-SDR-09\' --digiSteeringConf \'StandardSignalOnlyTruth\' --geometryVersion \'default:ATLAS-R2-2015-03-01-00\' --ignorePatterns \'Py:TrigConf2COOLLib.py.+ERROR.===================================+\' --inputHighPtMinbiasHitsFile \'mc15_13TeV.361035.Pythia8EvtGen_A2MSTW2008LO_minbias_inelastic_high.merge.HITS.e3581_s2578_s2195\' --inputLowPtMinbiasHitsFile \'mc15_13TeV.361034.Pythia8EvtGen_A2MSTW2008LO_minbias_inelastic_low.merge.HITS.e3581_s2578_s2195\' --numberOfCavernBkg 0 --numberOfHighPtMinBias 0.12268057 --numberOfLowPtMinBias 39.8773194 --pileupFinalBunch 6 --postExec \'\\"all:CfgMgr.MessageSvc().setError+=[\\\\"HepMcParticleLink\\\\"];\\" \\"ESDtoAOD:fixedAttrib=[s if \\\\"CONTAINER_SPLITLEVEL = \\\\\'99\\\\\'\\\\" not in s else \\\\"\\\\" for s in svcMgr.AthenaPoolCnvSvc.PoolAttributes];svcMgr.AthenaPoolCnvSvc.PoolAttributes=fixedAttrib\\"\' --postInclude \'default:RecJobTransforms/UseFrontier.py\' --preExec \'\\"all:rec.Commissioning.set_Value_and_Lock(True);from AthenaCommon.BeamFlags import jobproperties;jobproperties.Beam.numberOfCollisions.set_Value_and_Lock(20.0);from LArROD.LArRODFlags import larRODFlags;larRODFlags.NumberOfCollisions.set_Value_and_Lock(20);larRODFlags.nSamples.set_Value_and_Lock(4);larRODFlags.doOFCPileupOptimization.set_Value_and_Lock(True);larRODFlags.firstSample.set_Value_and_Lock(0);larRODFlags.useHighestGainAutoCorr.set_Value_and_Lock(True)\\" \\"RAWtoESD:from CaloRec.CaloCellFlags import jobproperties;jobproperties.CaloCellFlags.doLArCellEmMisCalib=False\\" \\"ESDtoAOD:TriggerFlags.AODEDMSet=\\\\"AODSLIM\\\\"\\"\' --preInclude \'\\"HITtoRDO:Digitization/ForceUseOfPileUpTools.py,SimulationJobOptions/preInclude.PileUpBunchTrainsMC15_2015_25ns_Config1.py,RunDependentSimData/configLumi_run284500_v2.py\\" \\"RDOtoRDOTrigger:RecExPers/RecoOutputMetadataList_jobOptions.py\\"\' --steering \'doRDO_TRIG\' --triggerConfig \'RDOtoRDOTrigger=MCRECO:DBF:TRIGGERDBMC:2046,20,56\' --AMITag r7772" --individualOutDS'
print 'setup: '+setup

config = ''
print 'config: '+config

comFirst = 'pathena {} --outDS {} --inDS {} {}'
comLater = 'pathena {} --outDS {} --inDS {} --libDS LAST {}'

# Submit jobs to the grid with pathena
# https://twiki.cern.ch/twiki/bin/view/PanDA/PandaAthena
for i,inDS in enumerate(inDSs):
    outDS = 'user.'+user+'.'+outDSs[i]+'.'+tag
    print 'Input dataset: '+inDS
    print 'Output dataset: '+outDS
    if (i==0 and doBuild) or doBuildAll:
        command = comFirst.format(setup, outDS, inDS, config)
    else:
        command = comLater.format(setup, outDS, inDS, config)
    sp.call('echo '+command, shell=True)
    sp.call(command, shell=True)
