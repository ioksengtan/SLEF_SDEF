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
slef_dict = slef_parser(lines_slef)
with open('slef.json','w') as file:
	file.write(json.dumps(slef_dict, ensure_ascii = True, encoding = 'utf-8'))

from sdef_parser import *
f_sdef = open(sdef_file,'r')
lines_sdef = f_sdef.readlines()
sdef_dict = sdef_parser(lines_sdef)
with open('sdef.json','w') as file:
	file.write(json.dumps(sdef_dict, encoding = 'utf-8'))
f_slef.close()

#f_slef = open('slef.json')
#tmp = str(f_slef.read())
#slef_dict = json.loads(tmp, encoding = 'utf-8')

from render import *
svg_list = get_svg_from_sdef(slef_dict, sdef_dict)

f = open(output_file,'w')
for svg_ in svg_list:
	f.write(svg_+'\n')
f.close()

