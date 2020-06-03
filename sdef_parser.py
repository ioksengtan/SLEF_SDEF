import sys
		
def get_indent_data(string_in):
	string = string_in.split('\n')[0]
	num_indent = 0
	if string.count('\t') == len(string):
		return [0,None]
	for i in range(0, len(string)):
		if string[i] == '\t':
			num_indent = num_indent + 1
		else:
			return [num_indent, '\t'.join(string.split())]

def sdef_parser(lines):
	print 'sdef_parser start.'
	state = 'idle'
	curr_instance = None
	instance_dict = {}
	for line in lines:
		if line[0] == '#':
			continue
		[num_indent, cmd] = get_indent_data(line)	
		#print '[dbg]cmd:',str(num_indent),cmd
		if state == 'idle':
			if num_indent == 0 and cmd != None:
				state = 'instance' 
				curr_instance = cmd
				instance_dict[cmd] = {}
				continue
		elif state == 'instance':
			if num_indent == 0 :
				if cmd == None:
					state = 'idle'
					continue
				else:
					instance_dict[cmd] = {}
					continue
			elif num_indent == 1:
				instance_dict[curr_instance]['attributes'] = {}
				if cmd.split()[0] == 'class':
					instance_dict[curr_instance]['class'] = 'class'
				elif cmd == 'port':
					state = 'instance_port'
					instance_dict[curr_instance]['port'] = {}
				elif cmd == 'layout':
					state = 'instance_layout'
					instance_dict[curr_instance]['layout'] = []
				elif cmd[0] == '.':
					instance_dict[curr_instance]['attributes'][cmd.split()[0].split('.')[1]] = cmd.split()[1]
				else:
					print 'exec:'+cmd
					print 'error! now only support (1) port, (2) layout'
				continue
		elif state == 'instance_port':
			if num_indent == 2 :
				instance_dict[curr_instance]['port'][cmd] = {}
				curr_port_name = cmd
				continue
			elif num_indent == 3 :
				if len(cmd.split()) == 1:
					instance_dict[curr_instance]['port'][curr_port_name][cmd.split()[0]] = None 
				elif len(cmd.split()) == 2:
					instance_dict[curr_instance]['port'][curr_port_name][cmd.split()[0]] = cmd.split()[1]
				continue
			elif num_indent == 1: 
				if cmd == 'layout':
					state = 'instance_layout'
					instance_dict[curr_instance]['layout'] = []
				continue
			elif num_indent == 0:
				if cmd == None :
					state = 'idle'
					continue
				else:
					state = 'instance'
					curr_instance = cmd
					instance_dict[curr_instance] = {}
					continue
			else:
				print 'error!'
				print 'num_indent:' + str(num_indent)
				print cmd
				return
		elif state == 'instance_layout':
			if num_indent == 2 :
				state = 'instance_layout_svg'
				curr_svg_type = cmd
				curr_svg_dict = { 'type': curr_svg_type }
				continue
			elif num_indent == 3 :
				if len(cmd.split()) == 1:
					instance_dict[curr_instance]['layout'][curr_svg_type][cmd.split()[0]] = None 
				elif len(cmd.split()) == 2:
					instance_dict[curr_instance]['layout'][curr_svg_type][cmd.split()[0]] = cmd.split()[1]
				continue
			elif num_indent == 1: 
				if cmd == 'port':
					state = 'instance_port'
				continue
			elif num_indent == 0:
				if cmd == None :
					state = 'idle'
					continue
				else:
					state = 'instance'
					curr_instance = cmd
					instance_dict[curr_instance] = {}
					continue
			else:
				print 'error!'
				print 'num_indent:' + str(num_indent)
				print cmd
				return
			continue
		elif state == 'instance_layout_svg':
			if num_indent == 3:
				svg_property = cmd.split()[0]
				svg_property_value = cmd.split()[1]
				curr_svg_dict[svg_property] = svg_property_value
			elif num_indent == 2:
				instance_dict[curr_instance]['layout'].append(curr_svg_dict)
				curr_svg_type = cmd
				curr_svg_dict = {}
				curr_svg_dict['type'] = curr_svg_type
			elif num_indent == 0:
				if cmd == None:
					state = 'idle'
					instance_dict[curr_instance]['layout'].append(curr_svg_dict)
					curr_svg_dict = {}
					continue
				else:
					state = 'instance'
					instance_dict[curr_instance]['layout'].append(curr_svg_dict)
					curr_instance = cmd
					instance_dict[cmd] = {}
					continue
				
		#print 'state:'+state+', curr_comp:',curr_instance
	print 'sdef_parser done.'
	return instance_dict


if __name__ == '__main__':
	f = open(sys.argv[1],'r')
	lines = f.readlines()
	slef_parser(lines)

