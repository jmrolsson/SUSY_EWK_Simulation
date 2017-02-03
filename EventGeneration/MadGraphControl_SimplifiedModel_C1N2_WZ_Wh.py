include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPreInclude.py' )

def MassToFloat(s):
  if "p" in s:
    return float(s.replace("p", "."))
  return float(s)

splitConfig = runArgs.jobConfig[0].rstrip('.py').split('_')

# C1/N2 degenerate
masses['1000024'] = MassToFloat(splitConfig[4])
masses['1000023'] = MassToFloat(splitConfig[4])
masses['1000022'] = MassToFloat(splitConfig[5])
if masses['1000022']<0.5: masses['1000022']=0.5

# will be C1N2
gentype = splitConfig[2]
# will be WZ or Wh
decaytype = splitConfig[3]

process = '''
generate p p > x1+ n2 $ susystrong @1
add process p p > x1- n2 $ susystrong @1
add process p p > x1+ n2 j $ susystrong @2
add process p p > x1- n2 j $ susystrong @2
add process p p > x1+ n2 j j $ susystrong @3
add process p p > x1- n2 j j $ susystrong @3
'''
njets = 2
evgenLog.info('Registered generation of ~chi1+/- ~chi20 production, decay via '+decaytype+'; grid point '+str(runArgs.runNumber)+' decoded into mass point ' + str(masses['1000024']) + ' ' + str(masses['1000022']))


evgenConfig.contact  = [ "joakim.olsson@cern.ch" ]
evgenConfig.keywords += ['gaugino', 'chargino', 'neutralino']
evgenConfig.description = '~chi1+/- ~chi20 production, decay via WZ or Wh in simplified model'

genSeq.Pythia8.Commands += [ "24:mMin = 0.2", "23:mMin = 0.2" ]

# WZ
if len(splitConfig)>6 and 'WZ' in decaytype and 'bblv' in splitConfig[6]:
    evgenLog.info('only W(lv)Z(bb) processes will be generated')
    genSeq.Pythia8.Commands += [
        "23:onMode = off", #switch off all Z decays
        "23:onIfAny = 5", # switch on Z->bb
        "24:onMode = off", #switch off all W decays
        "24:onIfAny = 11 12 13 14 15 16" # switch on W->lv
        ]
elif len(splitConfig)>6 and 'WZ' in decaytype and 'bbqq' in splitConfig[6]:
    evgenLog.info('only W(qq)Z(bb) processes will be generated')
    genSeq.Pythia8.Commands += [
        "23:onMode = off", #switch off all Z decays
        "23:onIfAny = 5", # switch on Z->bb
        "24:onMode = off", #switch off all W decays
        "24:onIfAny = 1 2 3 4 5" # switch on W->qqbar
        ]
# Wh
if len(splitConfig)>6 and 'Wh' in decaytype and 'bblv' in splitConfig[6]:
    evgenLog.info('only W(lv)h(bb) processes will be generated')
    genSeq.Pythia8.Commands += [
        "25:onMode = off", #switch off all h decays
        "25:onIfAny = 5", # switch on h->bb
        "24:onMode = off", #switch off all W decays
        "24:onIfAny = 11 12 13 14 15 16" # switch on W->lv
        ]
elif len(splitConfig)>6 and 'Wh' in decaytype and 'bbqq' in splitConfig[6]:
    evgenLog.info('only W(qq)h(bb) processes will be generated')
    genSeq.Pythia8.Commands += [
        "25:onMode = off", #switch off all h decays
        "25:onIfAny = 5", # switch on h->bb
        "24:onMode = off", #switch off all W decays
        "24:onIfAny = 1 2 3 4 5" # switch on W->qqbar
        ]
else:
    evgenLog.info('inclusive processes will be generated')

#--------------------------------------------------------------
# filters
#--------------------------------------------------------------

# need more events from MG due to filter - this needs to be set before MadGraphControl_SimplifiedModelPostInclude.py is run (it's set at 2 there)
# 3 is only sufficient for large mass splittings
evt_multiplier = 3

# filter for bblv final states
if '1L4andJ10or1L7' in splitConfig[-1]:
    evgenLog.info('(1lepton4 and jet10) or 1lepton7 filter')

    from GeneratorFilters.GeneratorFiltersConf import MultiElecMuTauFilter
    filtSeq += MultiElecMuTauFilter("DileptonFilterLow")
    filtSeq += MultiElecMuTauFilter("DileptonFilterHigh")

    MultiElecMuTauFilter1 = filtSeq.DileptonFilterLow
    MultiElecMuTauFilter1.NLeptons  = 1
    MultiElecMuTauFilter1.MinPt = 4000            # low pt-cut on the lepton
    MultiElecMuTauFilter1.MaxEta = 2.8            # stay away from MS 2.7 just in case
    MultiElecMuTauFilter1.IncludeHadTaus = 0      # don't include hadronic taus

    MultiElecMuTauFilter2 = filtSeq.DileptonFilterHigh
    MultiElecMuTauFilter2.NLeptons  = 1
    MultiElecMuTauFilter2.MinPt = 7000             #high pt cut on the lepton
    MultiElecMuTauFilter2.MaxEta = 2.8             # stay away from MS 2.7 just in case
    MultiElecMuTauFilter2.IncludeHadTaus = 0       # don't include hadronic taus

    include( 'MC15JobOptions/AntiKt4TruthWZJets.py')
    include( 'MC15JobOptions/JetFilter_Fragment.py')
    filtSeq.QCDTruthJetFilter.MinPt  = 10000.         # low pt-cut on the jet
    filtSeq.QCDTruthJetFilter.MaxEta = 5.0            # eta-cut on the jet
    filtSeq.QCDTruthJetFilter.TruthJetContainer = "AntiKt4TruthWZJets"

    filtSeq.Expression = "(DileptonFilterLow and QCDTruthJetFilter) or DileptonFilterHigh"

    evt_multiplier = 6

elif '1L4andJ10' in splitConfig[-1]:
    evgenLog.info('(1lepton4 and jet10) filter')

    from GeneratorFilters.GeneratorFiltersConf import MultiElecMuTauFilter
    filtSeq += MultiElecMuTauFilter("DileptonFilterLow")

    MultiElecMuTauFilter = filtSeq.DileptonFilterLow
    MultiElecMuTauFilter.NLeptons  = 1
    MultiElecMuTauFilter.MinPt = 4000            # low pt-cut on the lepton
    MultiElecMuTauFilter.MaxEta = 2.8            # stay away from MS 2.7 just in case
    MultiElecMuTauFilter.IncludeHadTaus = 0      # don't include hadronic taus

    include( 'MC15JobOptions/AntiKt4TruthWZJets.py')
    include( 'MC15JobOptions/JetFilter_Fragment.py')
    filtSeq.QCDTruthJetFilter.MinPt  = 10000.         # low pt-cut on the jet
    filtSeq.QCDTruthJetFilter.MaxEta = 5.0            # eta-cut on the jet
    filtSeq.QCDTruthJetFilter.TruthJetContainer = "AntiKt4TruthWZJets"

    filtSeq.Expression = "(DileptonFilterLow and QCDTruthJetFilter)"

    evt_multiplier = 6

elif re.search('J\d+', splitConfig[-1]):
    jetcut = re.search('(?<=J)\d+', splitConfig[-1]).group()
    jetcut_f = int(jetcut)*1000.
    evgenLog.info('jet'+jetcut+' filter')

    include( 'MC15JobOptions/AntiKt4TruthWZJets.py')
    include( 'MC15JobOptions/JetFilter_Fragment.py')
    filtSeq.QCDTruthJetFilter.MinPt  = jetcut_f       # low pt-cut on the jet
    filtSeq.QCDTruthJetFilter.MaxEta = 5.0            # eta-cut on the jet
    filtSeq.QCDTruthJetFilter.TruthJetContainer = "AntiKt4TruthWZJets"

    filtSeq.Expression = "QCDTruthJetFilter"

include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPostInclude.py' )

if njets>0:
    genSeq.Pythia8.Commands += [ "Merging:Process = pp>{x1+,1000024}{x1-,-1000024}{n2,1000023}",
                                 "1000024:spinType = 1",
                                 "1000023:spinType = 1" ]
