#! /usr/bin/env python
import subprocess as sp
import re

# <<---- JOB SETUP -------------------------------------------------------------

nFiles = -1
nFilesPerJob = 30
maxCpuCount = 252000 # 70 hrs

import datetime
#today = datetime.datetime.today()
#tag = today.strftime('%Y%m%d')+'_30k_1'
#tag = '20170506_2.1'
#tag = '20170514_1.1'
tag = '20170516_1.1'
user = 'jolsson'

doBuild = True
doBuildAll = False

#inDSs = [
#    'user.jolsson.mc15_13TeV.000027.MGPy8EG_A14N23LO_C1N2_Wh_300p0_25p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000028.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p5_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    # 'user.jolsson.mc15_13TeV.000020.MGPy8EG_A14N23LO_C1N2_Wh_400p0_200p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000024.MGPy8EG_A14N23LO_C1N2_Wh_400p0_0p5_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000017.MGPy8EG_A14N23LO_C1N2_Wh_500p0_200p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000026.MGPy8EG_A14N23LO_C1N2_Wh_300p0_50p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    # 'user.jolsson.mc15_13TeV.000023.MGPy8EG_A14N23LO_C1N2_Wh_400p0_25p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000019.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p5_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000032.MGPy8EG_A14N23LO_C1N2_Wh_150p0_0p5_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000021.MGPy8EG_A14N23LO_C1N2_Wh_400p0_100p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000029.MGPy8EG_A14N23LO_C1N2_Wh_200p0_25p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000031.MGPy8EG_A14N23LO_C1N2_Wh_200p0_0p5_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000022.MGPy8EG_A14N23LO_C1N2_Wh_400p0_50p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000018.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    # 'user.jolsson.mc15_13TeV.000030.MGPy8EG_A14N23LO_C1N2_Wh_200p0_50p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000025.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000012.MGPy8EG_A14N23LO_C1N2_WZ_300p0_0p5_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000005.MGPy8EG_A14N23LO_C1N2_WZ_400p0_100p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000010.MGPy8EG_A14N23LO_C1N2_WZ_300p0_50p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000009.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000002.MGPy8EG_A14N23LO_C1N2_WZ_500p0_100p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_WZ_400p0_50p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000001.MGPy8EG_A14N23LO_C1N2_WZ_500p0_200p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_500p0_0p5_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000007.MGPy8EG_A14N23LO_C1N2_WZ_400p0_25p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000013.MGPy8EG_A14N23LO_C1N2_WZ_200p0_25p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000016.MGPy8EG_A14N23LO_C1N2_WZ_150p0_0p5_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000015.MGPy8EG_A14N23LO_C1N2_WZ_200p0_0p5_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000004.MGPy8EG_A14N23LO_C1N2_WZ_400p0_200p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_WZ_400p0_0p5_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000014.MGPy8EG_A14N23LO_C1N2_WZ_200p0_50p0_bbqq_J10.EVNT.20170204_30k_1_EXT0',
#    'user.jolsson.mc15_13TeV.000011.MGPy8EG_A14N23LO_C1N2_WZ_300p0_25p0_bbqq_J10.EVNT.20170204_30k_1_EXT0'
#    ]

#inDSs = ['user.jolsson.mc15_13TeV.000001.MGPy8EG_A14N23LO_C1N2_WZ_500p0_100p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000002.MGPy8EG_A14N23LO_C1N2_WZ_500p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000004.MGPy8EG_A14N23LO_C1N2_WZ_300p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000005.MGPy8EG_A14N23LO_C1N2_WZ_150p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000007.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000009.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000010.MGPy8EG_A14N23LO_C1N2_Wh_150p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000011.MGPy8EG_A14N23LO_C1N2_Wh_800p0_200p0_bbqq_J10.EVNT.20170506_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000012.MGPy8EG_A14N23LO_C1N2_Wh_800p0_0p0_bbqq_J10.EVNT.20170506_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000013.MGPy8EG_A14N23LO_C1N2_Wh_700p0_0p0_bbqq_J10.EVNT.20170506_30k_2_EXT0']
#inDSs = ['user.jolsson.mc15_13TeV.000014.MGPy8EG_A14N23LO_C1N2_Wh_600p0_0p0_bbqq_J10.EVNT.20170506_30k_2_EXT0']

#inDSs = ['user.jolsson.mc15_13TeV.000015.MGPy8EG_A14N23LO_C1N2_Wh_200p0_0p0_bbqq_J10.EVNT.20170514_30k_1_EXT0',
#         'user.jolsson.mc15_13TeV.000016.MGPy8EG_A14N23LO_C1N2_Wh_300p0_50p0_bbqq_J10.EVNT.20170514_30k_1_EXT0',
#         'user.jolsson.mc15_13TeV.000017.MGPy8EG_A14N23LO_C1N2_Wh_350p0_50p0_bbqq_J10.EVNT.20170514_30k_1_EXT0',
#         'user.jolsson.mc15_13TeV.000018.MGPy8EG_A14N23LO_C1N2_Wh_350p0_100p0_bbqq_J10.EVNT.20170514_30k_1_EXT0',
#         'user.jolsson.mc15_13TeV.000019.MGPy8EG_A14N23LO_C1N2_Wh_400p0_0p0_bbqq_J10.EVNT.20170514_30k_1_EXT0',
#         'user.jolsson.mc15_13TeV.000020.MGPy8EG_A14N23LO_C1N2_Wh_400p0_100p0_bbqq_J10.EVNT.20170514_30k_1_EXT0',
#         'user.jolsson.mc15_13TeV.000021.MGPy8EG_A14N23LO_C1N2_Wh_450p0_50p0_bbqq_J10.EVNT.20170514_30k_1_EXT0',
#         'user.jolsson.mc15_13TeV.000022.MGPy8EG_A14N23LO_C1N2_Wh_450p0_150p0_bbqq_J10.EVNT.20170514_30k_1_EXT0']

inDSs = ['user.jolsson.mc15_13TeV.000023.MGPy8EG_A14N23LO_C1N2_WZ_1000p0_0p0_bbqq_J10.EVNT.20170516_30k_1_EXT0',
         'user.jolsson.mc15_13TeV.000024.MGPy8EG_A14N23LO_C1N2_WZ_800p0_200p0_bbqq_J10.EVNT.20170516_30k_1_EXT0',
         'user.jolsson.mc15_13TeV.000025.MGPy8EG_A14N23LO_C1N2_WZ_800p0_0p0_bbqq_J10.EVNT.20170516_30k_1_EXT0',
         'user.jolsson.mc15_13TeV.000026.MGPy8EG_A14N23LO_C1N2_WZ_600p0_0p0_bbqq_J10.EVNT.20170516_30k_1_EXT0']

# >>---------------------------------------------------------------------------

outDSs = []
for inDS in inDSs:
    outDS = 'user.'+user+'.'
    outDS += re.search('(?<=user\.jolsson\.).*(?=\.EVNT\.)',inDS).group()
    outDS += '.TRUTH1.'+tag
    outDSs.append(outDS)

setup = '--nFiles '+str(nFiles)+' --nFilesPerJob '+str(nFilesPerJob)+' --maxCpuCount '+str(maxCpuCount) \
    +' --trf "Reco_tf.py --inputEVNTFile=%IN --outputDAODFile=%OUT.TRUTH.pool.root --reductionConf TRUTH1"'
print 'setup: '+setup

config = ''
print 'config: '+config

comFirst = 'pathena {} --outDS {} --inDS {} {}'
comLater = 'pathena {} --outDS {} --inDS {} --libDS LAST {}'

# Submit jobs to the grid with pathena
# https://twiki.cern.ch/twiki/bin/view/PanDA/PandaAthena
for i,inDS in enumerate(inDSs):
    outDS = outDSs[i]
    print 'Input dataset: '+inDS
    print 'Output dataset: '+outDS
    if (i==0 and doBuild) or doBuildAll:
        command = comFirst.format(setup, outDS, inDS, config)
    else:
        command = comLater.format(setup, outDS, inDS, config)
    print command
    sp.call(command, shell=True)
