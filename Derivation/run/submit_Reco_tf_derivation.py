#! /usr/bin/env python
import subprocess as sp
import re

# <<---- JOB SETUP -------------------------------------------------------------

nFiles = -1
#nFilesPerJob = 10
nFilesPerJob = 20
nEventsPerJob = -1
nEventsPerFile = -1
#nSkipFiles = 100
nSkipFiles = -1

maxCpuCount = 252000 # 70 hrs

tag = '20170516_1.1.1.1'
#tag = '20170514_1.1.3.1'
#tag = '20170506_2.1.1.1'
#tag = '20170322_2.3.4.4'
#tag = '20170322_2.1.1.1_AFII'
#tag = '20170322_2.1.1.2_AFII'
user = 'jolsson'

doBuild = True
doBuildAll = False

#inDSs = ['user.jolsson.mc15_13TeV.000001.MGPy8EG_A14N23LO_C1N2_WZ_500p0_100p0_bbqq_J10.AOD.20170322_2.3.4_EXT0',
#         'user.jolsson.mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.AOD.20170322_2.3.4_EXT0',
#         'user.jolsson.mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.AOD.20170322_2.3.4_EXT0',
#         'user.jolsson.mc15_13TeV.000007.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.AOD.20170322_2.3.4_EXT0',
#         'user.jolsson.mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.AOD.20170322_2.3.4_EXT0',
#         'user.jolsson.mc15_13TeV.000009.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.AOD.20170322_2.3.4_EXT0']
#
#outDSs = ['mc15_13TeV.000001.MGPy8EG_A14N23LO_C1N2_WZ_500p0_100p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000007.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000009.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.DAOD_SUSY10']

#inDSs = ['user.jolsson.mc15_13TeV.000001.MGPy8EG_A14N23LO_C1N2_WZ_500p0_100p0_bbqq_J10.AOD.20170322_2.3.4_EXT0',
#         'user.jolsson.mc15_13TeV.000002.MGPy8EG_A14N23LO_C1N2_WZ_500p0_0p0_bbqq_J10.AOD.20170322_2.3.4_EXT0',
#         'user.jolsson.mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.AOD.20170322_2.3.4_EXT0',
#         'user.jolsson.mc15_13TeV.000004.MGPy8EG_A14N23LO_C1N2_WZ_300p0_0p0_bbqq_J10.AOD.20170322_2.3.4_EXT0',
#         'user.jolsson.mc15_13TeV.000005.MGPy8EG_A14N23LO_C1N2_WZ_150p0_0p0_bbqq_J10.AOD.20170322_2.3.4_EXT0',
#         'user.jolsson.mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.AOD.20170322_2.3.4_EXT0',
#         'user.jolsson.mc15_13TeV.000007.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.AOD.20170322_2.3.4_EXT0',
#         'user.jolsson.mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.AOD.20170322_2.3.4_EXT0',
#         'user.jolsson.mc15_13TeV.000009.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.AOD.20170322_2.3.4_EXT0',
#         'user.jolsson.mc15_13TeV.000010.MGPy8EG_A14N23LO_C1N2_Wh_150p0_0p0_bbqq_J10.AOD.20170322_2.3.4_EXT0']
#
#outDSs = ['mc15_13TeV.000001.MGPy8EG_A14N23LO_C1N2_WZ_500p0_100p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000002.MGPy8EG_A14N23LO_C1N2_WZ_500p0_0p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000004.MGPy8EG_A14N23LO_C1N2_WZ_300p0_0p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000005.MGPy8EG_A14N23LO_C1N2_WZ_150p0_0p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000007.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000009.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000010.MGPy8EG_A14N23LO_C1N2_Wh_150p0_0p0_bbqq_J10.DAOD_SUSY10']

#inDSs = ['user.jolsson.mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.AOD.20170322_2.3.4_EXT0',
#         'user.jolsson.mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.AOD.20170322_2.3.4_EXT0']
#
#outDSs = ['mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.DAOD_SUSY10']

#inDSs = ['user.jolsson.mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.AOD.20170322_2.1.1_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.000010.MGPy8EG_A14N23LO_C1N2_Wh_150p0_0p0_bbqq_J10.AOD.20170322_2.1.1_AFII_EXT0']
#
#outDSs = ['mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000010.MGPy8EG_A14N23LO_C1N2_Wh_150p0_0p0_bbqq_J10.DAOD_SUSY10']

#inDSs = ['user.jolsson.mc15_13TeV.000011.MGPy8EG_A14N23LO_C1N2_Wh_800p0_200p0_bbqq_J10.AOD.20170506_2.1.1_EXT0',
#         'user.jolsson.mc15_13TeV.000014.MGPy8EG_A14N23LO_C1N2_Wh_600p0_0p0_bbqq_J10.AOD.20170506_2.1.1_EXT0']
#
#outDSs = ['mc15_13TeV.000011.MGPy8EG_A14N23LO_C1N2_Wh_800p0_200p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000014.MGPy8EG_A14N23LO_C1N2_Wh_600p0_0p0_bbqq_J10.DAOD_SUSY10']

#inDSs = ['user.jolsson.mc15_13TeV.000012.MGPy8EG_A14N23LO_C1N2_Wh_800p0_0p0_bbqq_J10.AOD.20170506_2.1.2_EXT0',
#         'user.jolsson.mc15_13TeV.000013.MGPy8EG_A14N23LO_C1N2_Wh_700p0_0p0_bbqq_J10.AOD.20170506_2.1.2_EXT0']
#
#outDSs = ['mc15_13TeV.000012.MGPy8EG_A14N23LO_C1N2_Wh_800p0_0p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000013.MGPy8EG_A14N23LO_C1N2_Wh_700p0_0p0_bbqq_J10.DAOD_SUSY10']

#inDSs = ['user.jolsson.mc15_13TeV.000016.MGPy8EG_A14N23LO_C1N2_Wh_300p0_50p0_bbqq_J10.AOD.20170514_1.1.3_EXT0',
#         'user.jolsson.mc15_13TeV.000017.MGPy8EG_A14N23LO_C1N2_Wh_350p0_50p0_bbqq_J10.AOD.20170514_1.1.3_EXT0',
#         'user.jolsson.mc15_13TeV.000018.MGPy8EG_A14N23LO_C1N2_Wh_350p0_100p0_bbqq_J10.AOD.20170514_1.1.3_EXT0',
#         'user.jolsson.mc15_13TeV.000019.MGPy8EG_A14N23LO_C1N2_Wh_400p0_0p0_bbqq_J10.AOD.20170514_1.1.3_EXT0']
#
#outDSs = ['mc15_13TeV.000016.MGPy8EG_A14N23LO_C1N2_Wh_300p0_50p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000017.MGPy8EG_A14N23LO_C1N2_Wh_350p0_50p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000018.MGPy8EG_A14N23LO_C1N2_Wh_350p0_100p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000019.MGPy8EG_A14N23LO_C1N2_Wh_400p0_0p0_bbqq_J10.DAOD_SUSY10']

#inDSs = ['user.jolsson.mc15_13TeV.000015.MGPy8EG_A14N23LO_C1N2_Wh_200p0_0p0_bbqq_J10.AOD.20170514_1.1.3_EXT0',
#         'user.jolsson.mc15_13TeV.000021.MGPy8EG_A14N23LO_C1N2_Wh_450p0_50p0_bbqq_J10.AOD.20170514_1.1.3_EXT0']

#outDSs = ['mc15_13TeV.000015.MGPy8EG_A14N23LO_C1N2_Wh_200p0_0p0_bbqq_J10.DAOD_SUSY10',
#          'mc15_13TeV.000021.MGPy8EG_A14N23LO_C1N2_Wh_450p0_50p0_bbqq_J10.DAOD_SUSY10']

#inDSs = ['user.jolsson.mc15_13TeV.000022.MGPy8EG_A14N23LO_C1N2_Wh_450p0_150p0_bbqq_J10.AOD.20170514_1.1.3_EXT0']
#outDSs = ['mc15_13TeV.000022.MGPy8EG_A14N23LO_C1N2_Wh_450p0_150p0_bbqq_J10.DAOD_SUSY10']

inDSs = ['user.jolsson.mc15_13TeV.000023.MGPy8EG_A14N23LO_C1N2_WZ_1000p0_0p0_bbqq_J10.AOD.20170516_1.1.1_EXT0',
         'user.jolsson.mc15_13TeV.000024.MGPy8EG_A14N23LO_C1N2_WZ_800p0_200p0_bbqq_J10.AOD.20170516_1.1.1_EXT0',
         'user.jolsson.mc15_13TeV.000025.MGPy8EG_A14N23LO_C1N2_WZ_800p0_0p0_bbqq_J10.AOD.20170516_1.1.1_EXT0',
         'user.jolsson.mc15_13TeV.000026.MGPy8EG_A14N23LO_C1N2_WZ_600p0_0p0_bbqq_J10.AOD.20170516_1.1.1_EXT0']

outDSs = ['mc15_13TeV.000023.MGPy8EG_A14N23LO_C1N2_WZ_1000p0_0p0_bbqq_J10.DAOD_SUSY10',
          'mc15_13TeV.000024.MGPy8EG_A14N23LO_C1N2_WZ_800p0_200p0_bbqq_J10.DAOD_SUSY10',
          'mc15_13TeV.000025.MGPy8EG_A14N23LO_C1N2_WZ_800p0_0p0_bbqq_J10.DAOD_SUSY10',
          'mc15_13TeV.000026.MGPy8EG_A14N23LO_C1N2_WZ_600p0_0p0_bbqq_J10.DAOD_SUSY10']

# >>---------------------------------------------------------------------------

reco_setup = 'Reco_tf.py --inputAODFile %IN --outputDAODFile test.pool.root --reductionConf SUSY10 \
    --preExec \'default:from BTagging.BTaggingFlags import BTaggingFlags;BTaggingFlags.CalibrationTag = \\\"BTagCalibRUN12-08-18\\\"\'' 

pathena_setup = ' --useNewTRF --nSkipFiles '+str(nSkipFiles)+' --nFiles '+str(nFiles)+' --nFilesPerJob '+str(nFilesPerJob)+' --nEventsPerJob '+str(nEventsPerJob)+ \
    ' --nEventsPerFile '+str(nEventsPerFile)+' --maxCpuCount '+str(maxCpuCount)+' ' 

config = ''

comFirst = 'pathena --extOutFile DAOD_SUSY10.test.pool.root --outDS {} --inDS {} {} --trf "{}" {}'
comLater = 'pathena --extOutFile DAOD_SUSY10.test.pool.root --outDS {} --inDS {} {} --trf "{}" --libDS LAST {}'

# Submit jobs to the grid with pathena
# https://twiki.cern.ch/twiki/bin/view/PanDA/PandaAthena
for i,inDS in enumerate(inDSs):
    outDS = 'user.'+user+'.'+outDSs[i]+'.'+tag
    print 'Input dataset: '+inDS
    print 'Output dataset: '+outDS
    if (i==0 and doBuild) or doBuildAll:
        command = comFirst.format(outDS, inDS, pathena_setup, reco_setup, config)
    else:
        command = comLater.format(outDS, inDS, pathena_setup, reco_setup, config)
    sp.call('echo '+command, shell=True)
    sp.call(command, shell=True)
