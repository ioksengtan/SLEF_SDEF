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
	state_slef_parser = 'idle'
	curr_component = None
	component_dict = {}
	for line in lines:
		[num_indent, cmd] = get_indent_data(line)	
		#print '[dbg]cmd:',str(num_indent),cmd
		if state_slef_parser == 'idle':
			if num_indent == 0 and cmd != None:
				state_slef_parser = 'component' 
				curr_component = cmd
				component_dict[cmd] = {}
				continue
		elif state_slef_parser == 'component':
			if num_indent == 0 :
				if cmd == None:
					state_slef_parser = 'idle'
					continue
				else:
					component_dict[cmd] = {}
					continue
			elif num_indent == 1:
				if cmd == 'port':
					state_slef_parser = 'component_port'
					component_dict[curr_component]['port'] = {}
				elif cmd == 'layout':
					state_slef_parser = 'component_layout'
					component_dict[curr_component]['layout'] = {}
				else:
					print 'error! now only support (1) port, (2) layout'
				continue
		elif state_slef_parser == 'component_port':
			if num_indent == 2 :
				component_dict[curr_component]['port'][cmd] = {}
				curr_port_name = cmd
				continue
			elif num_indent == 3 :
				if len(cmd.split()) == 1:
					component_dict[curr_component]['port'][curr_port_name][cmd.split()[0]] = None 
				elif len(cmd.split()) == 2:
					component_dict[curr_component]['port'][curr_port_name][cmd.split()[0]] = cmd.split()[1]
				continue
			elif num_indent == 1: 
				if cmd == 'layout':
					state_slef_parser = 'component_layout'
					component_dict[curr_component]['layout'] = {}
				continue
			elif num_indent == 0:
				if cmd == None :
					state_slef_parser = 'idle'
					continue
				else:
					state_slef_parser = 'component'
					curr_component = cmd
					component_dict[curr_component] = {}
					continue
			else:
				print 'error!'
				print 'num_indent:' + str(num_indent)
				print cmd
				return
		elif state_slef_parser == 'component_layout':
			if num_indent == 2 :
				svg_type = cmd
				component_dict[curr_component]['layout'][svg_type] = {}
				curr_svg_type = cmd
				continue
			elif num_indent == 3 :
				if len(cmd.split()) == 1:
					component_dict[curr_component]['layout'][curr_svg_type][cmd.split()[0]] = None 
				elif len(cmd.split()) == 2:
					component_dict[curr_component]['layout'][curr_svg_type][cmd.split()[0]] = cmd.split()[1]
				continue
			elif num_indent == 1: 
				if cmd == 'port':
					state_slef_parser = 'component_port'
				continue
			elif num_indent == 0:
				if cmd == None :
					state_slef_parser = 'idle'
					continue
				else:
					state_slef_parser = 'component'
					curr_component = cmd
					component_dict[curr_component] = {}
					continue
			else:
				print 'error!'
				print 'num_indent:' + str(num_indent)
				print cmd
				return
			continue
				
		
				
		#print 'state:'+state_slef_parser+', curr_comp:',curr_component
	print 'slef_parser done.'
	return component_dict

def slef_parser_bak(lines):
	print 'slef_parser start.'
	indent_number_reg = ''
	line_reg = ''
	line_cnt = 0
	components = []
	for line in lines:
		#print line.split()
		line_cnt = line_cnt + 1
		if line[0] == '#':
			continue
		else:
			indent_number = get_indent_number(line)
			#print 'indent:'+str(indent_number)
			#print 'indent_reg:' + str(indent_number_reg)
			if indent_number_reg == '':
				indent_number_reg = indent_number
				line_reg = line
				continue
			else:
				if ( indent_number - indent_number_reg ) > 1:
					print 'indent error:'
					print 'line ',str(line_cnt-1),':', line_reg
					print 'line ',str(line_cnt),':', line
					return 
				else:
					if indent_number == 0 and len(line.split()) > 0 :
						component = line.split('\n')[0]
						components.append(component)
						state = 'component_1'
					if indent_number == 1:
						if line.split()[0] == 'layout':
							print 'layout state'
							state = 'layout'
						elif line.split()[0] == 'port':
							print 'port state'
							state = 'port'
					if indent_number == 2 and state == 'layout':
						svg_type = line.split()[0]
					if indent_number == 2 and state == 'port':
						port_name = line.split()[0]
					if indent_number == 3 and state == 'layout':
						svg_property = line.split()[0]
						svg_property_value = line.split()[1]
						
					indent_number_reg = indent_number
					line_reg = line
		if state == 'layout':
			print 'dbg:layout'
			print line
		if state == 'port':
			print 'dbg:port'
			print line
	
	print 'total ' + str(len(components)) + ' components found'

	print 'slef_parser done.'
	

if __name__ == '__main__':
	f = open(sys.argv[1],'r')
	lines = f.readlines()
	slef_parser(lines)

