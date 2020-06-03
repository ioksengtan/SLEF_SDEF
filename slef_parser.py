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

def slef_parser(lines):
	print 'slef_parser start.'
	component_dict = {}
	curr_component = ''
	state = 'idle'
	curr_svg_dict = {}
	for line in lines:
		if line[0] == '#':
			continue
		else:
			[num_indent, cmd] = get_indent_data(line)	
		if state == 'idle':
			if num_indent == 0 and cmd != None:
				state = 'component'
				curr_component = cmd
				component_dict[curr_component] = {}
			else:
				state = 'idle'
			continue
		elif state == 'component':
			if num_indent == 0:
				state = 'idle'
				continue
			elif num_indent == 1 and cmd == 'layout':
				state = 'component_layout'
				component_dict[curr_component]['layout'] = []
				continue
			else:
				continue
		elif state == 'component_layout':
			if num_indent == 2:
				curr_svg_type = cmd.split()[0]
				curr_svg_dict = { 'type': curr_svg_type}
				state = 'component_layout_svg'
				continue
			elif num_indent == 0:
				continue
		elif state == 'component_layout_svg':
			if num_indent == 3:
				curr_svg_property = cmd.split()[0]
				curr_svg_property_value = cmd.split()[1]
				curr_svg_dict[curr_svg_property] = curr_svg_property_value
			elif num_indent == 2:
				component_dict[curr_component]['layout'].append(curr_svg_dict)
				curr_svg_type = cmd.split()[0]
				curr_svg_dict = { 'type': curr_svg_type}
				state = 'component_layout_svg'
			elif num_indent == 0:
				component_dict[curr_component]['layout'].append(curr_svg_dict)
				curr_svg_type = ''
				curr_svg_dict = {}
				if cmd == None:
					state = 'idle'
				else:
					state = 'component'
					curr_component = cmd
					component_dict[curr_component] = {}
	print 'slef_parser end.'	
	return component_dict

if __name__ == '__main__':
	f = open(sys.argv[1],'r')
	lines = f.readlines()
	slef_parser(lines)

