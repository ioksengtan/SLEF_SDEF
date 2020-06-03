svg_cmd_dict = [
    'line', 'circle', 'rect'    
]

#def render_sdef(slef_dict, sdef_dict):
def get_svg_from_sdef(slef_dict, sdef_dict):
	svg_list = []
	for instance in sdef_dict:
		print '\nrender:'+instance
		if 'layout' in sdef_dict[instance]:
			for svg_type_dict in sdef_dict[instance]['layout']:
				svg_type = svg_type_dict['type']
				if svg_type in svg_cmd_dict:
					print 'svg native cmd: ' + svg_type
					#print(render_svg(svg_type, sdef_dict[instance]['layout'][svg_type]))
					#svg_list.append(render_svg(sdef_dict[instance]['layout'][svg_type]))
					svg_list.append(render_svg(svg_type_dict))
				elif svg_type in slef_dict:
					#print 'render slef cmd: ' + svg_type
					for svg_element in slef_dict[svg_type]['layout']:
						svg_list.append(render_svg(svg_element, def_dict = svg_type_dict))
				else:
					print 'cmd not support: ' + svg_type
		print 'render done\n'
	return svg_list


def render_svg(dict_svg, def_dict = {}):
	offset_x = 0; offset_y = 0;
	if 'x' in def_dict:
		offset_x = def_dict['x']
	if 'y' in def_dict:
		offset_y = def_dict['y']
	rotation = 0;
	if dict_svg['type'] == 'rect':
		if 'x' in dict_svg:
			dict_svg['x'] = str(float(dict_svg['x']) + float(offset_x))
			dict_svg['y'] = str(float(dict_svg['y']) + float(offset_y))
		else:
			dict_svg['x'] = str(float(offset_x))
			dict_svg['y'] = str(float(offset_y))
	elif dict_svg['type'] == 'circle':
		dict_svg['cx'] = str(float(dict_svg['cx']) + float(offset_x))
		dict_svg['cy'] = str(float(dict_svg['cy']) + float(offset_y))
	elif dict_svg['type'] == 'line':
		dict_svg['x1'] = str(float(dict_svg['x1']) + float(offset_x))
		dict_svg['x2'] = str(float(dict_svg['x2']) + float(offset_x))
		dict_svg['y1'] = str(float(dict_svg['y1']) + float(offset_y))
		dict_svg['y2'] = str(float(dict_svg['y2']) + float(offset_y))
	svg_type = dict_svg['type']
	svg_raw = '<' + svg_type
	for element_svg in dict_svg:
		svg_raw = svg_raw + ' ' + element_svg + '="' + dict_svg[element_svg] + '"'
	#svg_raw = svg_raw + ' rotation=' + str(rotation)
	svg_raw = svg_raw + " />"
	return svg_raw
			
		
