from yaml import load, dump
from yaml import Loader, Dumper

def openFilesysConfig() -> Dict[str,str]:
	fsconfig = open("fs_config.yaml")
	
	# How to extract data from the config file:
	#
	# data = load(fsconfig, Loader=Loader)
	# pdf_sources = data['pdf_sources']
	# tex_sources = data['tex_sources']
	# notebook_sources = data['notebook_sources']
	
	return load(fsconfig, Loader=Loader)
