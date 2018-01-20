#! /usr/bin/env python
import subprocess as sp
import re

# <<---- JOB SETUP -------------------------------------------------------------

nFiles = -1
nFilesPerJob = 10
maxCpuCount = 252000 # 70 hrs

import datetime
tag='20180116'
user = 'jolsson'

doBuild = True
doBuildAll = False

inDSs = [
'mc15_13TeV.394330.MGPy8EG_A14N23LO_C1N2_Wh_hbb_350p50_0p0_had.evgen.EVNT.e6234',
'mc15_13TeV.394331.MGPy8EG_A14N23LO_C1N2_Wh_hbb_400p0_0p0_had.evgen.EVNT.e6234',
'mc15_13TeV.394338.MGPy8EG_A14N23LO_C1N2_Wh_hbb_500p0_0p0_had.evgen.EVNT.e6234',
'mc15_13TeV.394346.MGPy8EG_A14N23LO_C1N2_Wh_hbb_550p0_150p0_had.evgen.EVNT.e6234',
'mc15_13TeV.394348.MGPy8EG_A14N23LO_C1N2_Wh_hbb_600p0_0p0_had.evgen.EVNT.e6234',
'mc15_13TeV.394350.MGPy8EG_A14N23LO_C1N2_Wh_hbb_600p0_100p0_had.evgen.EVNT.e6234',
'mc15_13TeV.394357.MGPy8EG_A14N23LO_C1N2_Wh_hbb_700p0_0p0_had.evgen.EVNT.e6234',
'mc15_13TeV.394766.MGPy8EG_A14N23LO_C1N2_Wh_hbb_800p0_0p0_had.evgen.EVNT.e6340',
]

outDSs = [
'mc15_13TeV.394330.MGPy8EG_A14N23LO_C1N2_Wh_hbb_350p50_0p0_had.DAOD_TRUTH3.e6234',
'mc15_13TeV.394331.MGPy8EG_A14N23LO_C1N2_Wh_hbb_400p0_0p0_had.DAOD_TRUTH3.e6234',
'mc15_13TeV.394338.MGPy8EG_A14N23LO_C1N2_Wh_hbb_500p0_0p0_had.DAOD_TRUTH3.e6234',
'mc15_13TeV.394346.MGPy8EG_A14N23LO_C1N2_Wh_hbb_550p0_150p0_had.DAOD_TRUTH3.e6234',
'mc15_13TeV.394348.MGPy8EG_A14N23LO_C1N2_Wh_hbb_600p0_0p0_had.DAOD_TRUTH3.e6234',
'mc15_13TeV.394350.MGPy8EG_A14N23LO_C1N2_Wh_hbb_600p0_100p0_had.DAOD_TRUTH3.e6234',
'mc15_13TeV.394357.MGPy8EG_A14N23LO_C1N2_Wh_hbb_700p0_0p0_had.DAOD_TRUTH3.e6234',
'mc15_13TeV.394766.MGPy8EG_A14N23LO_C1N2_Wh_hbb_800p0_0p0_had.DAOD_TRUTH3.e6340',
]

setup = '--nFiles '+str(nFiles)+' --nFilesPerJob '+str(nFilesPerJob)+' --maxCpuCount '+str(maxCpuCount) \
    +' --trf "Reco_tf.py --inputEVNTFile=%IN --outputDAODFile=%OUT.TRUTH.pool.root --reductionConf TRUTH3"'
print 'setup: '+setup

config = ''
print 'config: '+config

comFirst = 'pathena {} --outDS {} --inDS {} {}'
comLater = 'pathena {} --outDS {} --inDS {} --libDS LAST {}'

# Submit jobs to the grid with pathena
# https://twiki.cern.ch/twiki/bin/view/PanDA/PandaAthena
for i,inDS in enumerate(inDSs):
    outDS = 'user.{:s}.{:s}_{:s}'.format(user, outDSs[i], tag)
    print 'Input dataset: '+inDS
    print 'Output dataset: '+outDS
    if (i==0 and doBuild) or doBuildAll:
        command = comFirst.format(setup, outDS, inDS, config)
    else:
        command = comLater.format(setup, outDS, inDS, config)
    print command
    sp.call(command, shell=True)
