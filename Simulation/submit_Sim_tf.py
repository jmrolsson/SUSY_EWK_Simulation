#! /usr/bin/env python
import subprocess as sp
import re

# <<---- JOB SETUP -------------------------------------------------------------

nFiles = -1
nFilesPerJob = -1
nEventsPerJob = 100
nSkipFiles = -1

maxCpuCount = 252000 # 70 hrs

#tag = '20170516_1.1'
#tag = '20170514_1.2'
#tag = '20170514_1.1'
#tag = '20170506_2.1'
#tag = '20170322_2.3'
#tag = '20170322_2.1_AFII'
#tag = '20170626_1.1'
tag = '20170726_AFII'
user = 'jolsson'

doBuild = True
doBuildAll = False

#### Submitting first 5k jobs

# inDSs = ['user.jolsson.mc15_13TeV.000001.MGPy8EG_A14N23LO_C1N2_WZ_500p0_100p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#          'user.jolsson.mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.EVNT.20170322_30k_2_EXT0']
# 
# outDSs = ['mc15_13TeV.000001.MGPy8EG_A14N23LO_C1N2_WZ_500p0_100p0_bbqq_J10.HITS',
#           'mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.HITS']

# inDSs = ['user.jolsson.mc15_13TeV.000002.MGPy8EG_A14N23LO_C1N2_WZ_500p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#          'user.jolsson.mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#          'user.jolsson.mc15_13TeV.000005.MGPy8EG_A14N23LO_C1N2_WZ_150p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#          'user.jolsson.mc15_13TeV.000007.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#          'user.jolsson.mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#          'user.jolsson.mc15_13TeV.000009.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0' ]
# 
# outDSs = ['mc15_13TeV.000002.MGPy8EG_A14N23LO_C1N2_WZ_500p0_0p0_bbqq_J10.HITS',
#           'mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.HITS',
#           'mc15_13TeV.000005.MGPy8EG_A14N23LO_C1N2_WZ_150p0_0p0_bbqq_J10.HITS',
#           'mc15_13TeV.000007.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.HITS',
#           'mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.HITS',
#           'mc15_13TeV.000009.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.HITS']

#inDSs = ['user.jolsson.mc15_13TeV.000004.MGPy8EG_A14N23LO_C1N2_WZ_300p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000010.MGPy8EG_A14N23LO_C1N2_Wh_150p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0']
#
#outDSs = ['mc15_13TeV.000004.MGPy8EG_A14N23LO_C1N2_WZ_300p0_0p0_bbqq_J10.HITS',
#          'mc15_13TeV.000010.MGPy8EG_A14N23LO_C1N2_Wh_150p0_0p0_bbqq_J10.HITS']

##### Submitting remaining 25k jobs

#inDSs = [#'user.jolsson.mc15_13TeV.000001.MGPy8EG_A14N23LO_C1N2_WZ_500p0_100p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000002.MGPy8EG_A14N23LO_C1N2_WZ_500p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000004.MGPy8EG_A14N23LO_C1N2_WZ_300p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000005.MGPy8EG_A14N23LO_C1N2_WZ_150p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000007.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000009.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000010.MGPy8EG_A14N23LO_C1N2_Wh_150p0_0p0_bbqq_J10.EVNT.20170322_30k_2_EXT0']
#
#outDSs = [#'mc15_13TeV.000001.MGPy8EG_A14N23LO_C1N2_WZ_500p0_100p0_bbqq_J10.HITS',
#          'mc15_13TeV.000002.MGPy8EG_A14N23LO_C1N2_WZ_500p0_0p0_bbqq_J10.HITS',
#          'mc15_13TeV.000003.MGPy8EG_A14N23LO_C1N2_WZ_300p0_100p0_bbqq_J10.HITS',
#          'mc15_13TeV.000004.MGPy8EG_A14N23LO_C1N2_WZ_300p0_0p0_bbqq_J10.HITS',
#          'mc15_13TeV.000005.MGPy8EG_A14N23LO_C1N2_WZ_150p0_0p0_bbqq_J10.HITS',
#          'mc15_13TeV.000006.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.HITS',
#          'mc15_13TeV.000007.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.HITS',
#          'mc15_13TeV.000008.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.HITS',
#          'mc15_13TeV.000009.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.HITS',
#          'mc15_13TeV.000010.MGPy8EG_A14N23LO_C1N2_Wh_150p0_0p0_bbqq_J10.HITS']

#inDSs = ['user.jolsson.mc15_13TeV.000011.MGPy8EG_A14N23LO_C1N2_Wh_800p0_200p0_bbqq_J10.EVNT.20170506_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000012.MGPy8EG_A14N23LO_C1N2_Wh_800p0_0p0_bbqq_J10.EVNT.20170506_30k_2_EXT0',
#         'user.jolsson.mc15_13TeV.000013.MGPy8EG_A14N23LO_C1N2_Wh_700p0_0p0_bbqq_J10.EVNT.20170506_30k_2_EXT0']
#outDSs = ['mc15_13TeV.000011.MGPy8EG_A14N23LO_C1N2_Wh_800p0_200p0_bbqq_J10.HITS',
#          'mc15_13TeV.000012.MGPy8EG_A14N23LO_C1N2_Wh_800p0_0p0_bbqq_J10.HITS',
#          'mc15_13TeV.000013.MGPy8EG_A14N23LO_C1N2_Wh_700p0_0p0_bbqq_J10.HITS']

#inDSs = ['user.jolsson.mc15_13TeV.000014.MGPy8EG_A14N23LO_C1N2_Wh_600p0_0p0_bbqq_J10.EVNT.20170506_30k_2_EXT0']
#outDSs = ['mc15_13TeV.000014.MGPy8EG_A14N23LO_C1N2_Wh_600p0_0p0_bbqq_J10.HITS']

#inDSs = ['user.jolsson.mc15_13TeV.000015.MGPy8EG_A14N23LO_C1N2_Wh_200p0_0p0_bbqq_J10.EVNT.20170514_30k_1_EXT0',
#         'user.jolsson.mc15_13TeV.000016.MGPy8EG_A14N23LO_C1N2_Wh_300p0_50p0_bbqq_J10.EVNT.20170514_30k_1_EXT0',
#         'user.jolsson.mc15_13TeV.000017.MGPy8EG_A14N23LO_C1N2_Wh_350p0_50p0_bbqq_J10.EVNT.20170514_30k_1_EXT0',
#         'user.jolsson.mc15_13TeV.000018.MGPy8EG_A14N23LO_C1N2_Wh_350p0_100p0_bbqq_J10.EVNT.20170514_30k_1_EXT0',
#         'user.jolsson.mc15_13TeV.000019.MGPy8EG_A14N23LO_C1N2_Wh_400p0_0p0_bbqq_J10.EVNT.20170514_30k_1_EXT0',
#         'user.jolsson.mc15_13TeV.000020.MGPy8EG_A14N23LO_C1N2_Wh_400p0_100p0_bbqq_J10.EVNT.20170514_30k_1_EXT0',
#         'user.jolsson.mc15_13TeV.000021.MGPy8EG_A14N23LO_C1N2_Wh_450p0_50p0_bbqq_J10.EVNT.20170514_30k_1_EXT0',
#         'user.jolsson.mc15_13TeV.000022.MGPy8EG_A14N23LO_C1N2_Wh_450p0_150p0_bbqq_J10.EVNT.20170514_30k_1_EXT0']
#
#outDSs = ['mc15_13TeV.000015.MGPy8EG_A14N23LO_C1N2_Wh_200p0_0p0_bbqq_J10.HITS',
#          'mc15_13TeV.000016.MGPy8EG_A14N23LO_C1N2_Wh_300p0_50p0_bbqq_J10.HITS',
#          'mc15_13TeV.000017.MGPy8EG_A14N23LO_C1N2_Wh_350p0_50p0_bbqq_J10.HITS',
#          'mc15_13TeV.000018.MGPy8EG_A14N23LO_C1N2_Wh_350p0_100p0_bbqq_J10.HITS',
#          'mc15_13TeV.000019.MGPy8EG_A14N23LO_C1N2_Wh_400p0_0p0_bbqq_J10.HITS',
#          'mc15_13TeV.000020.MGPy8EG_A14N23LO_C1N2_Wh_400p0_100p0_bbqq_J10.HITS',
#          'mc15_13TeV.000021.MGPy8EG_A14N23LO_C1N2_Wh_450p0_50p0_bbqq_J10.HITS',
#          'mc15_13TeV.000022.MGPy8EG_A14N23LO_C1N2_Wh_450p0_150p0_bbqq_J10.HITS']

#inDSs = ['user.jolsson.mc15_13TeV.000022.MGPy8EG_A14N23LO_C1N2_Wh_450p0_150p0_bbqq_J10.EVNT.20170514_30k_1_EXT0']
#outDSs = ['mc15_13TeV.000022.MGPy8EG_A14N23LO_C1N2_Wh_450p0_150p0_bbqq_J10.HITS']

#inDSs = ['user.jolsson.mc15_13TeV.000023.MGPy8EG_A14N23LO_C1N2_WZ_1000p0_0p0_bbqq_J10.EVNT.20170516_30k_1_EXT0',
#         'user.jolsson.mc15_13TeV.000024.MGPy8EG_A14N23LO_C1N2_WZ_800p0_200p0_bbqq_J10.EVNT.20170516_30k_1_EXT0',
#         'user.jolsson.mc15_13TeV.000025.MGPy8EG_A14N23LO_C1N2_WZ_800p0_0p0_bbqq_J10.EVNT.20170516_30k_1_EXT0',
#         'user.jolsson.mc15_13TeV.000026.MGPy8EG_A14N23LO_C1N2_WZ_600p0_0p0_bbqq_J10.EVNT.20170516_30k_1_EXT0']
#
#outDSs = ['mc15_13TeV.000023.MGPy8EG_A14N23LO_C1N2_WZ_1000p0_0p0_bbqq_J10.HITS',
#          'mc15_13TeV.000024.MGPy8EG_A14N23LO_C1N2_WZ_800p0_200p0_bbqq_J10.HITS',
#          'mc15_13TeV.000025.MGPy8EG_A14N23LO_C1N2_WZ_800p0_0p0_bbqq_J10.HITS',
#          'mc15_13TeV.000026.MGPy8EG_A14N23LO_C1N2_WZ_600p0_0p0_bbqq_J10.HITS']


#### NEW  samples (AFII) July 2016

#inDSs = ['user.jolsson.mc15_13TeV.100001.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.EVNT.20170726_EXT0']

#outDSs = ['mc15_13TeV.100001.MGPy8EG_A14N23LO_C1N2_Wh_300p0_0p0_bbqq_J10.HITS']

#inDSs = [#'user.jolsson.mc15_13TeV.100002.MGPy8EG_A14N23LO_C1N2_Wh_300p0_50p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100003.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100004.MGPy8EG_A14N23LO_C1N2_Wh_350p0_0p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100005.MGPy8EG_A14N23LO_C1N2_Wh_350p0_50p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100006.MGPy8EG_A14N23LO_C1N2_Wh_350p0_100p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100007.MGPy8EG_A14N23LO_C1N2_Wh_400p0_0p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100008.MGPy8EG_A14N23LO_C1N2_Wh_400p0_50p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100009.MGPy8EG_A14N23LO_C1N2_Wh_400p0_100p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100010.MGPy8EG_A14N23LO_C1N2_Wh_450p0_0p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100011.MGPy8EG_A14N23LO_C1N2_Wh_450p0_50p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100012.MGPy8EG_A14N23LO_C1N2_Wh_450p0_100p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100013.MGPy8EG_A14N23LO_C1N2_Wh_450p0_150p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100014.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100015.MGPy8EG_A14N23LO_C1N2_Wh_500p0_50p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100016.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100017.MGPy8EG_A14N23LO_C1N2_Wh_500p0_150p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100018.MGPy8EG_A14N23LO_C1N2_Wh_500p0_200p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100019.MGPy8EG_A14N23LO_C1N2_Wh_550p0_0p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100020.MGPy8EG_A14N23LO_C1N2_Wh_550p0_50p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100021.MGPy8EG_A14N23LO_C1N2_Wh_550p0_100p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100022.MGPy8EG_A14N23LO_C1N2_Wh_550p0_150p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100023.MGPy8EG_A14N23LO_C1N2_Wh_550p0_200p0_bbqq_J10.EVNT.20170726_EXT0',
#         #'user.jolsson.mc15_13TeV.100024.MGPy8EG_A14N23LO_C1N2_Wh_600p0_0p0_bbqq_J10.EVNT.20170726_EXT0',
#         'user.jolsson.mc15_13TeV.100025.MGPy8EG_A14N23LO_C1N2_Wh_600p0_50p0_bbqq_J10.EVNT.20170726_EXT0',
#         'user.jolsson.mc15_13TeV.100026.MGPy8EG_A14N23LO_C1N2_Wh_600p0_100p0_bbqq_J10.EVNT.20170726_EXT0',
#         'user.jolsson.mc15_13TeV.100027.MGPy8EG_A14N23LO_C1N2_Wh_600p0_150p0_bbqq_J10.EVNT.20170726_EXT0',
#         'user.jolsson.mc15_13TeV.100028.MGPy8EG_A14N23LO_C1N2_Wh_700p0_0p0_bbqq_J10.EVNT.20170726_EXT0',
#         'user.jolsson.mc15_13TeV.100029.MGPy8EG_A14N23LO_C1N2_Wh_700p0_50p0_bbqq_J10.EVNT.20170726_EXT0']
#
#outDSs =  [#'mc15_13TeV.100002.MGPy8EG_A14N23LO_C1N2_Wh_300p0_50p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100003.MGPy8EG_A14N23LO_C1N2_Wh_300p0_100p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100004.MGPy8EG_A14N23LO_C1N2_Wh_350p0_0p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100005.MGPy8EG_A14N23LO_C1N2_Wh_350p0_50p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100006.MGPy8EG_A14N23LO_C1N2_Wh_350p0_100p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100007.MGPy8EG_A14N23LO_C1N2_Wh_400p0_0p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100008.MGPy8EG_A14N23LO_C1N2_Wh_400p0_50p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100009.MGPy8EG_A14N23LO_C1N2_Wh_400p0_100p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100010.MGPy8EG_A14N23LO_C1N2_Wh_450p0_0p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100011.MGPy8EG_A14N23LO_C1N2_Wh_450p0_50p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100012.MGPy8EG_A14N23LO_C1N2_Wh_450p0_100p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100013.MGPy8EG_A14N23LO_C1N2_Wh_450p0_150p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100014.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100015.MGPy8EG_A14N23LO_C1N2_Wh_500p0_50p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100016.MGPy8EG_A14N23LO_C1N2_Wh_500p0_100p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100017.MGPy8EG_A14N23LO_C1N2_Wh_500p0_150p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100018.MGPy8EG_A14N23LO_C1N2_Wh_500p0_200p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100019.MGPy8EG_A14N23LO_C1N2_Wh_550p0_0p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100020.MGPy8EG_A14N23LO_C1N2_Wh_550p0_50p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100021.MGPy8EG_A14N23LO_C1N2_Wh_550p0_100p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100022.MGPy8EG_A14N23LO_C1N2_Wh_550p0_150p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100023.MGPy8EG_A14N23LO_C1N2_Wh_550p0_200p0_bbqq_J10.HITS',
#           #'mc15_13TeV.100024.MGPy8EG_A14N23LO_C1N2_Wh_600p0_0p0_bbqq_J10.HITS',
#           'mc15_13TeV.100025.MGPy8EG_A14N23LO_C1N2_Wh_600p0_50p0_bbqq_J10.HITS',
#           'mc15_13TeV.100026.MGPy8EG_A14N23LO_C1N2_Wh_600p0_100p0_bbqq_J10.HITS',
#           'mc15_13TeV.100027.MGPy8EG_A14N23LO_C1N2_Wh_600p0_150p0_bbqq_J10.HITS',
#           'mc15_13TeV.100028.MGPy8EG_A14N23LO_C1N2_Wh_700p0_0p0_bbqq_J10.HITS',
#           'mc15_13TeV.100029.MGPy8EG_A14N23LO_C1N2_Wh_700p0_50p0_bbqq_J10.HITS']

inDSs = ['user.jolsson.mc15_13TeV.100006.MGPy8EG_A14N23LO_C1N2_Wh_350p0_100p0_bbqq_J10.EVNT.20170726_EXT0',
         'user.jolsson.mc15_13TeV.100022.MGPy8EG_A14N23LO_C1N2_Wh_550p0_150p0_bbqq_J10.EVNT.20170726_EXT0']

outDSs = ['mc15_13TeV.100006.MGPy8EG_A14N23LO_C1N2_Wh_350p0_100p0_bbqq_J10.HITS',
          'mc15_13TeV.100022.MGPy8EG_A14N23LO_C1N2_Wh_550p0_150p0_bbqq_J10.HITS']

# >>---------------------------------------------------------------------------

#setup = ' --nSkipFiles '+str(nSkipFiles)+' --nFiles '+str(nFiles)+' --nFilesPerJob '+str(nFilesPerJob)+' --nEventsPerJob '+str(nEventsPerJob)+' --maxCpuCount '+str(maxCpuCount)+' --useNewTRF --trf "Sim_tf.py --inputEVNTFile %IN --outputHITSFile %OUT.pool.root --maxEvents '+str(nEventsPerJob)+' --DBRelease \'default:current\' --DataRunNumber 222525 --conditionsTag \'default:OFLCOND-RUN12-SDR-19\' --geometryVersion \'default:ATLAS-R2-2015-03-01-00_VALIDATION\' --physicsList FTFP_BERT --postInclude \'default:PyJobTransforms/UseFrontier.py\' --preInclude \'EVNTtoHITS:SimulationJobOptions/preInclude.BeamPipeKill.py,SimulationJobOptions/preInclude.FrozenShowersFCalOnly.py\' --simulator MC12G4 --truthStrategy MC15aPlus" --individualOutDS'
setup = '--nFiles '+str(nFiles)+' --nFilesPerJob '+str(nFilesPerJob)+' --nEventsPerJob '+str(nEventsPerJob)+' --maxCpuCount '+str(maxCpuCount)+' --useNewTRF --trf "Sim_tf.py --inputEVNTFile %IN --outputHITSFile %OUT.pool.root --maxEvents '+str(nEventsPerJob)+' --DBRelease \'default:current\' --DataRunNumber 222525 --conditionsTag \'default:OFLCOND-RUN12-SDR-19\' --geometryVersion \'default:ATLAS-R2-2015-03-01-00_VALIDATION\' --physicsList FTFP_BERT --postInclude \'default:PyJobTransforms/UseFrontier.py\' --preInclude \'EVNTtoHITS:SimulationJobOptions/preInclude.BeamPipeKill.py,SimulationJobOptions/preInclude.FrozenShowersFCalOnly.py\' --simulator ATLFASTII --truthStrategy MC15aPlus" --individualOutDS'
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
