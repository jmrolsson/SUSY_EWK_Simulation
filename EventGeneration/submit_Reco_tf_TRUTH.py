#! /usr/bin/env python
import subprocess as sp
import re

# <<---- JOB SETUP -------------------------------------------------------------

nFiles = -1
nFilesPerJob = 10
maxCpuCount = 252000 # 70 hrs

import datetime
today = datetime.datetime.today()
tag = today.strftime('%Y%m%d')+'_10k_alpha1_1'
user = 'jolsson'

doBuild = True
doBuildAll = False

inDSs = [
'user.jolsson.mc15_13TeV.000018.MGPy8EG_A14N23LO_C1N2_WZ_500p0_100p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000023.MGPy8EG_A14N23LO_C1N2_WZ_400p0_150p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000068.MGPy8EG_A14N23LO_C1N2_Wh_700p0_300p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000004.MGPy8EG_A14N23LO_C1N2_WZ_700p0_0p5_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0 ',
'user.jolsson.mc15_13TeV.000047.MGPy8EG_A14N23LO_C1N2_WZ_500p0_350p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000066.MGPy8EG_A14N23LO_C1N2_WZ_200p0_0p5_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0 ',
'user.jolsson.mc15_13TeV.000070.MGPy8EG_A14N23LO_C1N2_Wh_700p0_0p5_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0 ',
'user.jolsson.mc15_13TeV.000002.MGPy8EG_A14N23LO_C1N2_WZ_700p0_300p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000021.MGPy8EG_A14N23LO_C1N2_WZ_400p0_250p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000044.MGPy8EG_A14N23LO_C1N2_WZ_600p0_100p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000020.MGPy8EG_A14N23LO_C1N2_WZ_400p0_300p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000022.MGPy8EG_A14N23LO_C1N2_WZ_400p0_200p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000069.MGPy8EG_A14N23LO_C1N2_Wh_700p0_100p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000060.MGPy8EG_A14N23LO_C1N2_WZ_300p0_150p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_WZ_600p0_450p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000010.MGPy8EG_A14N23LO_C1N2_WZ_600p0_200p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000063.MGPy8EG_A14N23LO_C1N2_WZ_300p0_0p5_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0 ',
'user.jolsson.mc15_13TeV.000026.MGPy8EG_A14N23LO_C1N2_WZ_300p0_200p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000017.MGPy8EG_A14N23LO_C1N2_WZ_500p0_200p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000001.MGPy8EG_A14N23LO_C1N2_WZ_700p0_500p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000007.MGPy8EG_A14N23LO_C1N2_WZ_600p0_400p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000009.MGPy8EG_A14N23LO_C1N2_WZ_600p0_300p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000011.MGPy8EG_A14N23LO_C1N2_WZ_600p0_100p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000013.MGPy8EG_A14N23LO_C1N2_WZ_500p0_400p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000012.MGPy8EG_A14N23LO_C1N2_WZ_600p0_0p5_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0 ',
'user.jolsson.mc15_13TeV.000016.MGPy8EG_A14N23LO_C1N2_WZ_500p0_250p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000019.MGPy8EG_A14N23LO_C1N2_WZ_500p0_0p5_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0 ',
'user.jolsson.mc15_13TeV.000036.MGPy8EG_A14N23LO_C1N2_WZ_700p0_100p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_WZ_600p0_350p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000025.MGPy8EG_A14N23LO_C1N2_WZ_400p0_0p5_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0 ',
'user.jolsson.mc15_13TeV.000027.MGPy8EG_A14N23LO_C1N2_WZ_300p0_150p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000028.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000029.MGPy8EG_A14N23LO_C1N2_WZ_300p0_50p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000031.MGPy8EG_A14N23LO_C1N2_WZ_200p0_100p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000032.MGPy8EG_A14N23LO_C1N2_WZ_200p0_50p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000034.MGPy8EG_A14N23LO_C1N2_WZ_700p0_500p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000035.MGPy8EG_A14N23LO_C1N2_WZ_700p0_300p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000015.MGPy8EG_A14N23LO_C1N2_WZ_500p0_300p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000061.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000005.MGPy8EG_A14N23LO_C1N2_WZ_600p0_500p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000024.MGPy8EG_A14N23LO_C1N2_WZ_400p0_100p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000030.MGPy8EG_A14N23LO_C1N2_WZ_300p0_0p5_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0 ',
'user.jolsson.mc15_13TeV.000037.MGPy8EG_A14N23LO_C1N2_WZ_700p0_0p5_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0 ',
'user.jolsson.mc15_13TeV.000040.MGPy8EG_A14N23LO_C1N2_WZ_600p0_400p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000042.MGPy8EG_A14N23LO_C1N2_WZ_600p0_300p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000041.MGPy8EG_A14N23LO_C1N2_WZ_600p0_350p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000043.MGPy8EG_A14N23LO_C1N2_WZ_600p0_200p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000045.MGPy8EG_A14N23LO_C1N2_WZ_600p0_0p5_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0 ',
'user.jolsson.mc15_13TeV.000046.MGPy8EG_A14N23LO_C1N2_WZ_500p0_400p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000048.MGPy8EG_A14N23LO_C1N2_WZ_500p0_300p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000052.MGPy8EG_A14N23LO_C1N2_WZ_500p0_0p5_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0 ',
'user.jolsson.mc15_13TeV.000056.MGPy8EG_A14N23LO_C1N2_WZ_400p0_150p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000064.MGPy8EG_A14N23LO_C1N2_WZ_200p0_100p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000038.MGPy8EG_A14N23LO_C1N2_WZ_600p0_500p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000039.MGPy8EG_A14N23LO_C1N2_WZ_600p0_450p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000049.MGPy8EG_A14N23LO_C1N2_WZ_500p0_250p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000050.MGPy8EG_A14N23LO_C1N2_WZ_500p0_200p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000051.MGPy8EG_A14N23LO_C1N2_WZ_500p0_100p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000053.MGPy8EG_A14N23LO_C1N2_WZ_400p0_300p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000055.MGPy8EG_A14N23LO_C1N2_WZ_400p0_200p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000057.MGPy8EG_A14N23LO_C1N2_WZ_400p0_100p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000014.MGPy8EG_A14N23LO_C1N2_WZ_500p0_350p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000033.MGPy8EG_A14N23LO_C1N2_WZ_200p0_0p5_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0 ',
'user.jolsson.mc15_13TeV.000058.MGPy8EG_A14N23LO_C1N2_WZ_400p0_0p5_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0 ',
'user.jolsson.mc15_13TeV.000059.MGPy8EG_A14N23LO_C1N2_WZ_300p0_200p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000062.MGPy8EG_A14N23LO_C1N2_WZ_300p0_50p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000065.MGPy8EG_A14N23LO_C1N2_WZ_200p0_50p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000067.MGPy8EG_A14N23LO_C1N2_Wh_700p0_500p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_700p0_100p0_bbqq_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0',
'user.jolsson.mc15_13TeV.000054.MGPy8EG_A14N23LO_C1N2_WZ_400p0_250p0_bblv_1L4andJ10.EVNT.20170112_10k_alpha1_EXT0'
    ]

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
