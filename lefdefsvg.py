import json

from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("-slef", dest = "slef")
parser.add_argument("-sdef", dest = "sdef")
parser.add_argument("-o", dest = "output")
args = parser.parse_args()
slef_file =  args.slef
sdef_file =  args.sdef
output_file = args.output

from slef_parser import *
f_slef = open(slef_file,'r')
lines_slef = f_slef.readlines()
component_dict = slef_parser(lines_slef)
with open('slef.json','w') as file:
	file.write(json.dumps(component_dict))

f_slef.close()
