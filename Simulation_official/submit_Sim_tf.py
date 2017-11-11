#! /usr/bin/env python
import subprocess as sp
import re

# <<---- JOB SETUP -------------------------------------------------------------

nFiles = -1
nFilesPerJob = -1
nEventsPerJob = 100
nSkipFiles = -1

maxCpuCount = 252000 # 70 hrs

tag = '20171102_AFII'
user = 'jolsson'

doBuild = True
doBuildAll = False

inDSs = ['mc15_13TeV.394338.MGPy8EG_A14N23LO_C1N2_Wh_hbb_500p0_0p0_had.evgen.EVNT.e6234',
         'user.jolsson.mc15_13TeV.100014.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.EVNT.20170726_EXT0']

outDSs = ['mc15_13TeV.394338.MGPy8EG_A14N23LO_C1N2_Wh_hbb_500p0_0p0_had.HITS',
          'mc15_13TeV.100014.MGPy8EG_A14N23LO_C1N2_Wh_500p0_0p0_bbqq_J10.HITS']

# >>---------------------------------------------------------------------------

setup = '--nFiles '+str(nFiles)+' --nFilesPerJob '+str(nFilesPerJob)+' --nEventsPerJob '+str(nEventsPerJob)+' --maxCpuCount '+str(maxCpuCount)+' --useNewTRF --trf "Sim_tf.py --inputEVNTFile %IN --outputHITSFile %OUT.pool.root --maxEvents '+str(nEventsPerJob)+' --DBRelease \'default:current\' --DataRunNumber 222525 --conditionsTag \'default:OFLCOND-RUN12-SDR-19\' --geometryVersion \'default:ATLAS-R2-2015-03-01-00_VALIDATION\' --physicsList FTFP_BERT --postInclude \'default:PyJobTransforms/UseFrontier.py\' --preInclude \'EVNTtoHITS:SimulationJobOptions/preInclude.BeamPipeKill.py\' --simulator ATLFASTII --truthStrategy MC12" --individualOutDS'
print 'setup: '+setup

config = ' '
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
        print command
    else:
        command = comLater.format(setup, outDS, inDS, config)
    sp.call('echo '+command, shell=True)
    sp.call(command, shell=True)
