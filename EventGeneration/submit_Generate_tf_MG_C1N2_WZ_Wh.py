#! /usr/bin/env python
import subprocess as sp
import os
import re

# <<---- JOB SETUP -------------------------------------------------------------

# Run local or on the grid
runlocal = False

# Resubmit failed jobs (with new tag)
resubmit = False
# resubmitRuns = set([37, 39, 40])
resubmitRuns = set([])

import datetime
today = datetime.datetime.today()
tag = today.strftime('%Y%m%d')+'_30k_1'
# tag = '20161201_10k_1'
user = 'jolsson'
mctag = 'mc15_13TeV'

# 30k events per point
nJobs = 30
nEventsPerJob  = 1000

maxCpuCount = 252000 # 70 hrs
randSeed = 12749816

startRunNumber = 1
ecm = 13000

datasetName = 'MGPy8EG_A14N23LO_C1N2'
# Example: MC15.399100.MGPy8EG_A14N23LO_C1N2_WZ_500p0_0p5_bbqq_noFilter.py

massgrid_file = 'mass_grid.txt'
massgrid = []
if os.path.exists(massgrid_file):
    with open(massgrid_file) as f:
        for line in f:
            if (re.search('^#',line) or line==''): continue
            high_mass = 0.0
            for i,mass in enumerate(line.split()):
                fmass = float(mass)
                if i==0:
                    high_mass = fmass
                else:
                    massgrid.append(re.sub('\.', 'p', '{:.1f}_{:.1f}'.format(high_mass, fmass)))
elif IOError:
    print 'Unable to open file: '+str(massgrid_file)

# print massgrid

massgrid_WZ = massgrid
massgrid_Wh = massgrid
decaytypes = ['WZ', 'Wh']
# finalstates = ['bbqq', 'bblv']
finalstates = ['bbqq']
filters_bbqq = ['J10']
# filters_bblv = ['1L4andJ10']

# >>----------------------------------------------------------------------------


includeStr = 'include( \\\"MadGraphControl_SimplifiedModel_C1N2_WZ_Wh.py\\\" )'

# Generate job config files
jobConfigs = []
runNumbers = []
runNumber = startRunNumber
for decaytype in decaytypes:
    if 'Wh' == decaytype:
        massgrid = massgrid_Wh
    else:
        massgrid = massgrid_WZ
    for finalstate in finalstates:
        if 'bbqq' == finalstate:
            filters = filters_bbqq
        else:
            filters = filters_bblv
        for filt in filters:
            for mass in massgrid:
                if resubmit and (runNumber not in resubmitRuns): continue
                jobConfig = 'MC15.'+'{:0>6d}'.format(runNumber)+'.'+datasetName+'_'+ \
                    decaytype+'_'+mass+'_'+finalstate+'_'+filt+'.py'
                jobConfigs.append(jobConfig)
                sp.call('echo "'+includeStr+'" > '+jobConfig, shell=True)
                runNumbers.append('{:0>6d}'.format(runNumber))
                runNumber += 1

# Submit jobs to the grid
for i,jobConfig in enumerate(jobConfigs):

    runNumber = re.search('(?<=MC15\.)\d+(?=\.)', jobConfig).group()
    logfile = 'log.'+re.search('.*(?=\.py)', jobConfig).group()+'_'+tag+'.txt'
    outputfile = runNumber+".EVNT.pool.root"
    if runlocal:
        command = 'Generate_tf.py --ecmEnergy='+str(ecm)+' --runNumber=' \
            +runNumber+' --maxEvents='+str(nEventsPerJob) \
            +' --randomSeed='+str(randSeed)+' --jobConfig='+jobConfig \
            +' --outputEVNTFile=test1.'+runNumber+'.EVNT.pool.root'
    else:
        command = 'pathena --split '+str(nJobs) \
            +' --maxCpuCount '+str(maxCpuCount) \
            +' --trf "Generate_tf.py --ecmEnergy='+str(ecm) \
            +' --runNumber='+runNumber \
            +' --firstEvent=%SKIPEVENTS --maxEvents='+str(nEventsPerJob) \
            +' --randomSeed=%RNDM:'+str(randSeed)+' --jobConfig='+jobConfig \
            +' --outputEVNTFile=%OUT.'+outputfile+'" --outDS user.'+user+'.'+mctag+'.' \
            +re.search('(?<=MC15\.).*(?=\.py)', jobConfig).group()+'.EVNT.'+tag+' >& '+logfile+' &'

    # print 'outDS: user.'+user+'.'+mctag+'.'+re.search('(?<=MC15\.).*(?=\.py)', jobConfig).group()+'.EVNT.'+tag+'_EXT0'
    print '\nlogfile: '+logfile
    print 'command: '+command+'\n'
    sp.call(command, shell=True)
