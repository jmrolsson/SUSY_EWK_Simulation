#! /usr/bin/env python
import subprocess as sp
import re

# <<---- JOB SETUP -------------------------------------------------------------

nFiles = -1
nFilesPerJob = -1
nEventsPerJob = 50
#nEventsPerJob = 100
nEventsPerFile = -1
#nSkipFiles = 100
nSkipFiles = -1

maxCpuCount = 252000 # 70 hrs

#tag = '20170516_1.1.1'
#tag = '20170514_1.1.5' 
#tag = '20170514_1.1.3' 
#tag = '20170506_2.1.2' 
#tag = '20170322_2.3.test1b'
#tag = '20170322_2.3.4'
#tag = '20170322_2.1.1_AFII'

tag = '20170726_AFII'
user = 'jolsson'

doBuild = True
doBuildAll = False

#### Submitting first 5k jobs

# inDSs = ['user.jolsson.mc15_13TeV.000005.MGPy8EG_A14N23LO_C1N2_WZ_150p0_0p0_bbqq_J10.HITS.20170322_2.3_EXT0']

# outDSs = ['mc15_13TeV.000005.MGPy8EG_A14N23LO_C1N2_WZ_150p0_0p0_bbqq_J10.AOD']

#inDSs = ['user.jolsson.mc15_13TeV.000001.MGPy8EG_A14N23LO_C1N2_WZ_500p0_100p0_bbqq_J10.HITS.20170322_2.3_EXT0',
#         'user.jolsson.mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.HITS.20170322_2.3_EXT0',
#         'user.jolsson.mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.HITS.20170322_2.3_EXT0',
#         'user.jolsson.mc15_13TeV.000007.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.HITS.20170322_2.3_EXT0',
#         'user.jolsson.mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.HITS.20170322_2.3_EXT0',
#         'user.jolsson.mc15_13TeV.000009.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.HITS.20170322_2.3_EXT0']
#
#outDSs = ['mc15_13TeV.000001.MGPy8EG_A14N23LO_C1N2_WZ_500p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.000007.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.000009.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.AOD']

#inDSs = ['user.jolsson.mc15_13TeV.000002.MGPy8EG_A14N23LO_C1N2_WZ_500p0_0p0_bbqq_J10.HITS.20170322_2.3_EXT0',
#         'user.jolsson.mc15_13TeV.000004.MGPy8EG_A14N23LO_C1N2_WZ_300p0_0p0_bbqq_J10.HITS.20170322_2.3_EXT0',
#         'user.jolsson.mc15_13TeV.000010.MGPy8EG_A14N23LO_C1N2_Wh_150p0_0p0_bbqq_J10.HITS.20170322_2.3_EXT0']
#
#outDSs = ['mc15_13TeV.000002.MGPy8EG_A14N23LO_C1N2_WZ_500p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.000004.MGPy8EG_A14N23LO_C1N2_WZ_300p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.000010.MGPy8EG_A14N23LO_C1N2_Wh_150p0_0p0_bbqq_J10.AOD']

##### Submitting remaining 25k jobs

#inDSs = ['user.jolsson.mc15_13TeV.000001.MGPy8EG_A14N23LO_C1N2_WZ_500p0_100p0_bbqq_J10.HITS.20170322_2.3_EXT0',
#         'user.jolsson.mc15_13TeV.000002.MGPy8EG_A14N23LO_C1N2_WZ_500p0_0p0_bbqq_J10.HITS.20170322_2.3_EXT0',
#         #'user.jolsson.mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.HITS.20170322_2.3_EXT0',
#         'user.jolsson.mc15_13TeV.000004.MGPy8EG_A14N23LO_C1N2_WZ_300p0_0p0_bbqq_J10.HITS.20170322_2.3_EXT0',
#         'user.jolsson.mc15_13TeV.000005.MGPy8EG_A14N23LO_C1N2_WZ_150p0_0p0_bbqq_J10.HITS.20170322_2.3_EXT0',
#         'user.jolsson.mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.HITS.20170322_2.3_EXT0',
#         'user.jolsson.mc15_13TeV.000007.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.HITS.20170322_2.3_EXT0',
#         #'user.jolsson.mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.HITS.20170322_2.3_EXT0',
#         'user.jolsson.mc15_13TeV.000009.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.HITS.20170322_2.3_EXT0',
#         'user.jolsson.mc15_13TeV.000010.MGPy8EG_A14N23LO_C1N2_Wh_150p0_0p0_bbqq_J10.HITS.20170322_2.3_EXT0']
#
#outDSs = ['mc15_13TeV.000001.MGPy8EG_A14N23LO_C1N2_WZ_500p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.000002.MGPy8EG_A14N23LO_C1N2_WZ_500p0_0p0_bbqq_J10.AOD',
#          #'mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.000004.MGPy8EG_A14N23LO_C1N2_WZ_300p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.000005.MGPy8EG_A14N23LO_C1N2_WZ_150p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.000007.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.AOD',
#          #'mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.000009.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.000010.MGPy8EG_A14N23LO_C1N2_Wh_150p0_0p0_bbqq_J10.AOD']

#inDSs = ['user.jolsson.mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.HITS.20170322_2.3_EXT0',
#         'user.jolsson.mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.HITS.20170322_2.3_EXT0']
#
#outDSs = ['mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.AOD']

#### Submitting all AFII jobs

#inDSs = ['user.jolsson.mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.HITS.20170322_2.1_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.000010.MGPy8EG_A14N23LO_C1N2_Wh_150p0_0p0_bbqq_J10.HITS.20170322_2.1_AFII_EXT0']
#
#outDSs = ['mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.000010.MGPy8EG_A14N23LO_C1N2_Wh_150p0_0p0_bbqq_J10.AOD']

#inDSs = ['user.jolsson.mc15_13TeV.000011.MGPy8EG_A14N23LO_C1N2_Wh_800p0_200p0_bbqq_J10.HITS.20170506_2.1_EXT0',
#         'user.jolsson.mc15_13TeV.000014.MGPy8EG_A14N23LO_C1N2_Wh_600p0_0p0_bbqq_J10.HITS.20170506_2.1_EXT0']
#
#outDSs = ['mc15_13TeV.000011.MGPy8EG_A14N23LO_C1N2_Wh_800p0_200p0_bbqq_J10.AOD',
#          'mc15_13TeV.000014.MGPy8EG_A14N23LO_C1N2_Wh_600p0_0p0_bbqq_J10.AOD']

#inDSs = ['user.jolsson.mc15_13TeV.000012.MGPy8EG_A14N23LO_C1N2_Wh_800p0_0p0_bbqq_J10.HITS.20170506_2.1_EXT0',
#         'user.jolsson.mc15_13TeV.000013.MGPy8EG_A14N23LO_C1N2_Wh_700p0_0p0_bbqq_J10.HITS.20170506_2.1_EXT0']
#
#outDSs = ['mc15_13TeV.000012.MGPy8EG_A14N23LO_C1N2_Wh_800p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.000013.MGPy8EG_A14N23LO_C1N2_Wh_700p0_0p0_bbqq_J10.AOD']

#inDSs = ['user.jolsson.mc15_13TeV.000016.MGPy8EG_A14N23LO_C1N2_Wh_300p0_50p0_bbqq_J10.HITS.20170514_1.1_EXT0',
#         'user.jolsson.mc15_13TeV.000017.MGPy8EG_A14N23LO_C1N2_Wh_350p0_50p0_bbqq_J10.HITS.20170514_1.1_EXT0',
#         'user.jolsson.mc15_13TeV.000018.MGPy8EG_A14N23LO_C1N2_Wh_350p0_100p0_bbqq_J10.HITS.20170514_1.1_EXT0',
#         'user.jolsson.mc15_13TeV.000019.MGPy8EG_A14N23LO_C1N2_Wh_400p0_0p0_bbqq_J10.HITS.20170514_1.1_EXT0',
#         'user.jolsson.mc15_13TeV.000021.MGPy8EG_A14N23LO_C1N2_Wh_450p0_50p0_bbqq_J10.HITS.20170514_1.1_EXT0',
#         'user.jolsson.mc15_13TeV.000022.MGPy8EG_A14N23LO_C1N2_Wh_450p0_150p0_bbqq_J10.HITS.20170514_1.1_EXT0']
#
#outDSs = ['mc15_13TeV.000016.MGPy8EG_A14N23LO_C1N2_Wh_300p0_50p0_bbqq_J10.AOD',
#          'mc15_13TeV.000017.MGPy8EG_A14N23LO_C1N2_Wh_350p0_50p0_bbqq_J10.AOD',
#          'mc15_13TeV.000018.MGPy8EG_A14N23LO_C1N2_Wh_350p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.000019.MGPy8EG_A14N23LO_C1N2_Wh_400p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.000021.MGPy8EG_A14N23LO_C1N2_Wh_450p0_50p0_bbqq_J10.AOD',
#          'mc15_13TeV.000022.MGPy8EG_A14N23LO_C1N2_Wh_450p0_150p0_bbqq_J10.AOD']

#inDSs = ['user.jolsson.mc15_13TeV.000015.MGPy8EG_A14N23LO_C1N2_Wh_200p0_0p0_bbqq_J10.HITS.20170514_1.1_EXT0']
#outDSs = ['mc15_13TeV.000015.MGPy8EG_A14N23LO_C1N2_Wh_200p0_0p0_bbqq_J10.AOD']

#inDSs = ['user.jolsson.mc15_13TeV.000020.MGPy8EG_A14N23LO_C1N2_Wh_400p0_100p0_bbqq_J10.HITS.20170514_1.1_EXT0']
#         # 'user.jolsson.mc15_13TeV.000022.MGPy8EG_A14N23LO_C1N2_Wh_450p0_150p0_bbqq_J10.HITS.20170514_1.1_EXT0']
#
#outDSs = ['mc15_13TeV.000020.MGPy8EG_A14N23LO_C1N2_Wh_400p0_100p0_bbqq_J10.AOD']
#          #'mc15_13TeV.000022.MGPy8EG_A14N23LO_C1N2_Wh_450p0_150p0_bbqq_J10.AOD']

#inDSs = ['user.jolsson.mc15_13TeV.000023.MGPy8EG_A14N23LO_C1N2_WZ_1000p0_0p0_bbqq_J10.HITS.20170516_1.1_EXT0',
#         'user.jolsson.mc15_13TeV.000024.MGPy8EG_A14N23LO_C1N2_WZ_800p0_200p0_bbqq_J10.HITS.20170516_1.1_EXT0',
#         'user.jolsson.mc15_13TeV.000025.MGPy8EG_A14N23LO_C1N2_WZ_800p0_0p0_bbqq_J10.HITS.20170516_1.1_EXT0',
#         'user.jolsson.mc15_13TeV.000026.MGPy8EG_A14N23LO_C1N2_WZ_600p0_0p0_bbqq_J10.HITS.20170516_1.1_EXT0']
#
#outDSs = ['mc15_13TeV.000023.MGPy8EG_A14N23LO_C1N2_WZ_1000p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.000024.MGPy8EG_A14N23LO_C1N2_WZ_800p0_200p0_bbqq_J10.AOD',
#          'mc15_13TeV.000025.MGPy8EG_A14N23LO_C1N2_WZ_800p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.000026.MGPy8EG_A14N23LO_C1N2_WZ_600p0_0p0_bbqq_J10.AOD']

#inDSs = ['user.jolsson.mc15_13TeV.100001.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100002.MGPy8EG_A14N23LO_C1N2_Wh_300p0_50p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100003.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100004.MGPy8EG_A14N23LO_C1N2_Wh_350p0_0p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100005.MGPy8EG_A14N23LO_C1N2_Wh_350p0_50p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100006.MGPy8EG_A14N23LO_C1N2_Wh_350p0_100p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100007.MGPy8EG_A14N23LO_C1N2_Wh_400p0_0p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100008.MGPy8EG_A14N23LO_C1N2_Wh_400p0_50p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100009.MGPy8EG_A14N23LO_C1N2_Wh_400p0_100p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100010.MGPy8EG_A14N23LO_C1N2_Wh_450p0_0p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100011.MGPy8EG_A14N23LO_C1N2_Wh_450p0_50p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100012.MGPy8EG_A14N23LO_C1N2_Wh_450p0_100p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100013.MGPy8EG_A14N23LO_C1N2_Wh_450p0_150p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100014.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100015.MGPy8EG_A14N23LO_C1N2_Wh_500p0_50p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100016.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100017.MGPy8EG_A14N23LO_C1N2_Wh_500p0_150p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100018.MGPy8EG_A14N23LO_C1N2_Wh_500p0_200p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100019.MGPy8EG_A14N23LO_C1N2_Wh_550p0_0p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100020.MGPy8EG_A14N23LO_C1N2_Wh_550p0_50p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100021.MGPy8EG_A14N23LO_C1N2_Wh_550p0_100p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100022.MGPy8EG_A14N23LO_C1N2_Wh_550p0_150p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100023.MGPy8EG_A14N23LO_C1N2_Wh_550p0_200p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100024.MGPy8EG_A14N23LO_C1N2_Wh_600p0_0p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100025.MGPy8EG_A14N23LO_C1N2_Wh_600p0_50p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100026.MGPy8EG_A14N23LO_C1N2_Wh_600p0_100p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100027.MGPy8EG_A14N23LO_C1N2_Wh_600p0_150p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100028.MGPy8EG_A14N23LO_C1N2_Wh_700p0_0p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100029.MGPy8EG_A14N23LO_C1N2_Wh_700p0_50p0_bbqq_J10.HITS.20170726_AFII_EXT0']
#
#outDSs = ['mc15_13TeV.100001.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.100002.MGPy8EG_A14N23LO_C1N2_Wh_300p0_50p0_bbqq_J10.AOD',
#          'mc15_13TeV.100003.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.100004.MGPy8EG_A14N23LO_C1N2_Wh_350p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.100005.MGPy8EG_A14N23LO_C1N2_Wh_350p0_50p0_bbqq_J10.AOD',
#          'mc15_13TeV.100006.MGPy8EG_A14N23LO_C1N2_Wh_350p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.100007.MGPy8EG_A14N23LO_C1N2_Wh_400p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.100008.MGPy8EG_A14N23LO_C1N2_Wh_400p0_50p0_bbqq_J10.AOD',
#          'mc15_13TeV.100009.MGPy8EG_A14N23LO_C1N2_Wh_400p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.100010.MGPy8EG_A14N23LO_C1N2_Wh_450p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.100011.MGPy8EG_A14N23LO_C1N2_Wh_450p0_50p0_bbqq_J10.AOD',
#          'mc15_13TeV.100012.MGPy8EG_A14N23LO_C1N2_Wh_450p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.100013.MGPy8EG_A14N23LO_C1N2_Wh_450p0_150p0_bbqq_J10.AOD',
#          'mc15_13TeV.100014.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.100015.MGPy8EG_A14N23LO_C1N2_Wh_500p0_50p0_bbqq_J10.AOD',
#          'mc15_13TeV.100016.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.100017.MGPy8EG_A14N23LO_C1N2_Wh_500p0_150p0_bbqq_J10.AOD',
#          'mc15_13TeV.100018.MGPy8EG_A14N23LO_C1N2_Wh_500p0_200p0_bbqq_J10.AOD',
#          'mc15_13TeV.100019.MGPy8EG_A14N23LO_C1N2_Wh_550p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.100020.MGPy8EG_A14N23LO_C1N2_Wh_550p0_50p0_bbqq_J10.AOD',
#          'mc15_13TeV.100021.MGPy8EG_A14N23LO_C1N2_Wh_550p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.100022.MGPy8EG_A14N23LO_C1N2_Wh_550p0_150p0_bbqq_J10.AOD',
#          'mc15_13TeV.100023.MGPy8EG_A14N23LO_C1N2_Wh_550p0_200p0_bbqq_J10.AOD',
#          'mc15_13TeV.100024.MGPy8EG_A14N23LO_C1N2_Wh_600p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.100025.MGPy8EG_A14N23LO_C1N2_Wh_600p0_50p0_bbqq_J10.AOD',
#          'mc15_13TeV.100026.MGPy8EG_A14N23LO_C1N2_Wh_600p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.100027.MGPy8EG_A14N23LO_C1N2_Wh_600p0_150p0_bbqq_J10.AOD',
#          'mc15_13TeV.100028.MGPy8EG_A14N23LO_C1N2_Wh_700p0_0p0_bbqq_J10.AOD',
#          'mc15_13TeV.100029.MGPy8EG_A14N23LO_C1N2_Wh_700p0_50p0_bbqq_J10.AOD']

#inDSs = ['user.jolsson.mc15_13TeV.100009.MGPy8EG_A14N23LO_C1N2_Wh_400p0_100p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100016.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100023.MGPy8EG_A14N23LO_C1N2_Wh_550p0_200p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100025.MGPy8EG_A14N23LO_C1N2_Wh_600p0_50p0_bbqq_J10.HITS.20170726_AFII_EXT0',
#         'user.jolsson.mc15_13TeV.100026.MGPy8EG_A14N23LO_C1N2_Wh_600p0_100p0_bbqq_J10.HITS.20170726_AFII_EXT0']
#
#outDSs = ['mc15_13TeV.100009.MGPy8EG_A14N23LO_C1N2_Wh_400p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.100016.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.AOD',
#          'mc15_13TeV.100023.MGPy8EG_A14N23LO_C1N2_Wh_550p0_200p0_bbqq_J10.AOD',
#          'mc15_13TeV.100025.MGPy8EG_A14N23LO_C1N2_Wh_600p0_50p0_bbqq_J10.AOD',
#          'mc15_13TeV.100026.MGPy8EG_A14N23LO_C1N2_Wh_600p0_100p0_bbqq_J10.AOD']

inDSs = ['user.jolsson.mc15_13TeV.100001.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100002.MGPy8EG_A14N23LO_C1N2_Wh_300p0_50p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100003.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100004.MGPy8EG_A14N23LO_C1N2_Wh_350p0_0p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100005.MGPy8EG_A14N23LO_C1N2_Wh_350p0_50p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100006.MGPy8EG_A14N23LO_C1N2_Wh_350p0_100p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100007.MGPy8EG_A14N23LO_C1N2_Wh_400p0_0p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100008.MGPy8EG_A14N23LO_C1N2_Wh_400p0_50p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100010.MGPy8EG_A14N23LO_C1N2_Wh_450p0_0p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100011.MGPy8EG_A14N23LO_C1N2_Wh_450p0_50p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100012.MGPy8EG_A14N23LO_C1N2_Wh_450p0_100p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100013.MGPy8EG_A14N23LO_C1N2_Wh_450p0_150p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100014.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100015.MGPy8EG_A14N23LO_C1N2_Wh_500p0_50p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100017.MGPy8EG_A14N23LO_C1N2_Wh_500p0_150p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100018.MGPy8EG_A14N23LO_C1N2_Wh_500p0_200p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100019.MGPy8EG_A14N23LO_C1N2_Wh_550p0_0p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100020.MGPy8EG_A14N23LO_C1N2_Wh_550p0_50p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100021.MGPy8EG_A14N23LO_C1N2_Wh_550p0_100p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100022.MGPy8EG_A14N23LO_C1N2_Wh_550p0_150p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100024.MGPy8EG_A14N23LO_C1N2_Wh_600p0_0p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100027.MGPy8EG_A14N23LO_C1N2_Wh_600p0_150p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100028.MGPy8EG_A14N23LO_C1N2_Wh_700p0_0p0_bbqq_J10.HITS.20170726_AFII_EXT0',
         'user.jolsson.mc15_13TeV.100029.MGPy8EG_A14N23LO_C1N2_Wh_700p0_50p0_bbqq_J10.HITS.20170726_AFII_EXT0']

outDSs = ['mc15_13TeV.100001.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.AOD',
          'mc15_13TeV.100002.MGPy8EG_A14N23LO_C1N2_Wh_300p0_50p0_bbqq_J10.AOD',
          'mc15_13TeV.100003.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.AOD',
          'mc15_13TeV.100004.MGPy8EG_A14N23LO_C1N2_Wh_350p0_0p0_bbqq_J10.AOD',
          'mc15_13TeV.100005.MGPy8EG_A14N23LO_C1N2_Wh_350p0_50p0_bbqq_J10.AOD',
          'mc15_13TeV.100006.MGPy8EG_A14N23LO_C1N2_Wh_350p0_100p0_bbqq_J10.AOD',
          'mc15_13TeV.100007.MGPy8EG_A14N23LO_C1N2_Wh_400p0_0p0_bbqq_J10.AOD',
          'mc15_13TeV.100008.MGPy8EG_A14N23LO_C1N2_Wh_400p0_50p0_bbqq_J10.AOD',
          'mc15_13TeV.100010.MGPy8EG_A14N23LO_C1N2_Wh_450p0_0p0_bbqq_J10.AOD',
          'mc15_13TeV.100011.MGPy8EG_A14N23LO_C1N2_Wh_450p0_50p0_bbqq_J10.AOD',
          'mc15_13TeV.100012.MGPy8EG_A14N23LO_C1N2_Wh_450p0_100p0_bbqq_J10.AOD',
          'mc15_13TeV.100013.MGPy8EG_A14N23LO_C1N2_Wh_450p0_150p0_bbqq_J10.AOD',
          'mc15_13TeV.100014.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.AOD',
          'mc15_13TeV.100015.MGPy8EG_A14N23LO_C1N2_Wh_500p0_50p0_bbqq_J10.AOD',
          'mc15_13TeV.100017.MGPy8EG_A14N23LO_C1N2_Wh_500p0_150p0_bbqq_J10.AOD',
          'mc15_13TeV.100018.MGPy8EG_A14N23LO_C1N2_Wh_500p0_200p0_bbqq_J10.AOD',
          'mc15_13TeV.100019.MGPy8EG_A14N23LO_C1N2_Wh_550p0_0p0_bbqq_J10.AOD',
          'mc15_13TeV.100020.MGPy8EG_A14N23LO_C1N2_Wh_550p0_50p0_bbqq_J10.AOD',
          'mc15_13TeV.100021.MGPy8EG_A14N23LO_C1N2_Wh_550p0_100p0_bbqq_J10.AOD',
          'mc15_13TeV.100022.MGPy8EG_A14N23LO_C1N2_Wh_550p0_150p0_bbqq_J10.AOD',
          'mc15_13TeV.100024.MGPy8EG_A14N23LO_C1N2_Wh_600p0_0p0_bbqq_J10.AOD',
          'mc15_13TeV.100027.MGPy8EG_A14N23LO_C1N2_Wh_600p0_150p0_bbqq_J10.AOD',
          'mc15_13TeV.100028.MGPy8EG_A14N23LO_C1N2_Wh_700p0_0p0_bbqq_J10.AOD',
          'mc15_13TeV.100029.MGPy8EG_A14N23LO_C1N2_Wh_700p0_50p0_bbqq_J10.AOD']


# >>---------------------------------------------------------------------------

highMinDS = 'mc15_13TeV.361035.Pythia8EvtGen_A2MSTW2008LO_minbias_inelastic_high.merge.HITS.e3581_s2578_s2195'
lowMinDS = 'mc15_13TeV.361034.Pythia8EvtGen_A2MSTW2008LO_minbias_inelastic_low.merge.HITS.e3581_s2578_s2195'
nLowMin = 2
nHighMin = 2

reco_setup = 'Reco_tf.py --maxEvents '+str(nEventsPerJob)+' --jobNumber=%RNDM:0  --digiSeedOffset1 %RNDM:0 --digiSeedOffset2 %RNDM:0 \
          --inputHITSFile %IN --outputAODFile %OUT.pool.root --inputHighPtMinbiasHitsFile %HIMBIN --inputLowPtMinbiasHitsFile %LOMBIN \
          --numberOfCavernBkg 0 --numberOfHighPtMinBias 0.12268057 --numberOfLowPtMinBias 39.8773194 --pileupFinalBunch 6 \
          --conditionsTag default:OFLCOND-MC15c-SDR-09 --digiSteeringConf StandardSignalOnlyTruth --geometryVersion default:ATLAS-R2-2015-03-01-00 \
          --ignorePatterns Py:TrigConf2COOLLib.py.+ERROR.===================================+ \
          --postExec \'all:CfgMgr.MessageSvc().setError+=[\\\"HepMcParticleLink\\\"]\' \'ESDtoAOD:fixedAttrib=[s if \\\"CONTAINER_SPLITLEVEL = 99\\\" not in s else \\\"\\\" for s in svcMgr.AthenaPoolCnvSvc.PoolAttributes];svcMgr.AthenaPoolCnvSvc.PoolAttributes=fixedAttrib\' \
          --postInclude \'default:RecJobTransforms/UseFrontier.py\' \
          --preExec \'all:rec.Commissioning.set_Value_and_Lock(True);from AthenaCommon.BeamFlags import jobproperties;jobproperties.Beam.numberOfCollisions.set_Value_and_Lock(20.0);from LArROD.LArRODFlags import larRODFlags;larRODFlags.NumberOfCollisions.set_Value_and_Lock(20);larRODFlags.nSamples.set_Value_and_Lock(4);larRODFlags.doOFCPileupOptimization.set_Value_and_Lock(True);larRODFlags.firstSample.set_Value_and_Lock(0);larRODFlags.useHighestGainAutoCorr.set_Value_and_Lock(True)\' \'RAWtoESD:from CaloRec.CaloCellFlags import jobproperties;jobproperties.CaloCellFlags.doLArCellEmMisCalib=False\' \'ESDtoAOD:TriggerFlags.AODEDMSet=\\\"AODSLIM\\\"\' \
          --preInclude \'HITtoRDO:Digitization/ForceUseOfPileUpTools.py,SimulationJobOptions/preInclude.PileUpBunchTrainsMC15_2015_25ns_Config1.py,RunDependentSimData/configLumi_run284500_v2.py\' \'RDOtoRDOTrigger:RecExPers/RecoOutputMetadataList_jobOptions.py\' \
          --steering doRDO_TRIG --triggerConfig \'RDOtoRDOTrigger=MCRECO:DBF:TRIGGERDBMC:2046,20,56\' --AMITag r7772'

pathena_setup = ' --nSkipFiles '+str(nSkipFiles)+' --individualOutDS --useNewTRF --nLowMin '+str(nLowMin)+' --nHighMin '+str(nHighMin)+\
    ' --randomMin --nFiles '+str(nFiles)+' --nFilesPerJob '+str(nFilesPerJob)+' --nEventsPerJob '+str(nEventsPerJob)+\
    ' --nEventsPerFile '+str(nEventsPerFile)+' --maxCpuCount '+str(maxCpuCount)

#pathena_setup = ' --nSkipFiles '+str(nSkipFiles)+' --individualOutDS --useNewTRF --nLowMin '+str(nLowMin)+' --nHighMin '+str(nHighMin)+\
#    ' --randomMin --nFiles '+str(nFiles)+' --nFilesPerJob '+str(nFilesPerJob)+' --nEventsPerJob '+str(nEventsPerJob)+\
#    ' --nEventsPerFile '+str(nEventsPerFile)+' --maxCpuCount '+str(maxCpuCount)+' --site ANALY_MWT2_MCORE'

config = ''

comFirst = 'pathena --outDS {} --inDS {} --highMinDS {} --lowMinDS {} {} --trf "{}" {}'
comLater = 'pathena --outDS {} --inDS {} --highMinDS {} --lowMinDS {} {} --trf "{}" --libDS LAST {}'

# Submit jobs to the grid with pathena
# https://twiki.cern.ch/twiki/bin/view/PanDA/PandaAthena
for i,inDS in enumerate(inDSs):
    outDS = 'user.'+user+'.'+outDSs[i]+'.'+tag
    print 'Input dataset: '+inDS
    print 'Output dataset: '+outDS
    print ''
    if (i==0 and doBuild) or doBuildAll:
        command = comFirst.format(outDS, inDS, highMinDS, lowMinDS, pathena_setup, reco_setup, config)
    else:
        command = comLater.format(outDS, inDS, highMinDS, lowMinDS, pathena_setup, reco_setup, config)
    sp.call('echo '+command, shell=True)
    sp.call(command, shell=True)
