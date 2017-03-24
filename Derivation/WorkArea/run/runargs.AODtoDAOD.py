# Run arguments file auto-generated on Tue Mar 21 22:20:31 2017 by:
# JobTransform: AODtoDAOD
# Version: $Id: trfExe.py 791664 2017-01-10 14:11:44Z mavogel $
# Import runArgs class
from PyJobTransforms.trfJobOptions import RunArguments
runArgs = RunArguments()
runArgs.trfSubstepName = 'AODtoDAOD' 

runArgs.reductionConf = ['SUSY10']

# Explicitly added to process all events in this step
runArgs.maxEvents = -1

# Input data
runArgs.inputAODFile = ['../../../Reco/test1.000001.AOD.root']
runArgs.inputAODFileType = 'AOD'
runArgs.inputAODFileNentries = 2L
runArgs.AODFileIO = 'input'

# Output data
runArgs.outputDAOD_SUSY10File = 'DAOD_SUSY10.test1_SUSY10.pool.root'
runArgs.outputDAOD_SUSY10FileType = 'AOD'

# Extra runargs

# Extra runtime runargs

# Literal runargs snippets
