from WMCore.Configuration import Configuration
import yaml

key = 'QCD_bEnriched_HT300to500'
input_dataset = '/QCD_bEnriched_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM'

config = Configuration()
config.section_('General')
config.General.transferLogs = True
config.General.requestName = 'GEN_' + key
config.section_('JobType')
config.JobType.psetName = 'genParticles.py'
config.JobType.pluginName = 'Analysis'
config.section_('Data')
config.Data.inputDataset = input_dataset
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = 'CRAB3_GEN_' + key
config.Data.splitting = 'FileBased'
config.Data.publication = False
config.section_('Site')
config.Site.storageSite = 'T3_KR_KISTI'
config.section_('User')
config.section_('Debug')
