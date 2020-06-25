supported_svg_type = [
    'line', 'circle', 'rect'    
]

#def render_sdef(slef_dict, sdef_dict):
def get_svg_from_sdef(slef_dict, sdef_dict):
	#print 'dbg5'
	#print slef_dict
	svg_list = []
	for instance in sdef_dict:
		print '\nrender:'+instance
		if 'layout' in sdef_dict[instance]:
			for svg_type_dict in sdef_dict[instance]['layout']:
				svg_type = svg_type_dict['type']
				if svg_type in supported_svg_type:
					print 'svg native cmd: ' + svg_type
		#			#print(render_svg(svg_type, sdef_dict[instance]['layout'][svg_type]))
		#			#svg_list.append(render_svg(sdef_dict[instance]['layout'][svg_type]))
					svg_list.append(render_svg(svg_type_dict))
				elif svg_type in slef_dict:
					print 'render slef cmd: ' + svg_type
		#			print slef_dict[svg_type]
					for svg_element in slef_dict[svg_type]['layout']:
						svg_list.append(render_svg(svg_element, def_dict = svg_type_dict))
						#render_svg(svg_element, def_dict=svg_type_dict)
						continue
				else:
					print 'cmd not support: ' + svg_type
		print 'render done\n'
		#print 'slef_dict:'
		#print slef_dict
	return svg_list


def render_svg(dict_svg, def_dict = {}):
	print 'dict_svg:'
	print dict_svg
	print 'def_dict:'
	print def_dict
	output_svg = {}
	offset_x = 0; offset_y = 0;
	if 'x' in def_dict:
		offset_x = def_dict['x']
	if 'y' in def_dict:
		offset_y = def_dict['y']
	rotation = 0;
	for each_attribute in dict_svg:
		#print 'attr:'+each_attribute
		if each_attribute == 'type':
			if dict_svg[each_attribute] == 'rect':
				if 'x' in dict_svg:
					output_svg['x'] = str(float(dict_svg['x']) + float(offset_x))
					output_svg['y'] = str(float(dict_svg['y']) + float(offset_y))
				else:
					output_svg['x'] = str(float(offset_x))
					output_svg['y'] = str(float(offset_y))
			elif dict_svg[each_attribute] == 'circle':
				output_svg['cx'] = str(float(dict_svg['cx']) + float(offset_x))
				output_svg['cy'] = str(float(dict_svg['cy']) + float(offset_y))
			elif dict_svg[each_attribute] == 'line':
				output_svg['x1'] = str(float(dict_svg['x1']) + float(offset_x))
				output_svg['x2'] = str(float(dict_svg['x2']) + float(offset_x))
				output_svg['y1'] = str(float(dict_svg['y1']) + float(offset_y))
				output_svg['y2'] = str(float(dict_svg['y2']) + float(offset_y))
		elif each_attribute == 'width' or each_attribute == 'stroke-width' or each_attribute == 'fill' or each_attribute == 'stroke' or each_attribute == 'height' or each_attribute == 'r':
			output_svg[each_attribute] = dict_svg[each_attribute]
		else:
			print each_attribute + ' is not supported in this svg type. (' + dict_svg['type'] + ')'
			
		
	svg_type = dict_svg['type']
	svg_raw = '<' + svg_type
	for element_svg in output_svg:
		svg_raw = svg_raw + ' ' + element_svg + '="' + output_svg[element_svg] + '"'
	#svg_raw = svg_raw + ' rotation=' + str(rotation)
	svg_raw = svg_raw + " />"
	#print 'svg_raw:'
	#print svg_raw
	return svg_raw
			
		
