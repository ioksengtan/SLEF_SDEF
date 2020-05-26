def render_svg(slef_dict, sdef_dict):
	for instance in sdef_dict:
		if 'layout' in sdef_dict[instance]:
			for module in sdef_dict[instance]['layout']:
				if module == 'line':
					print sdef_dict[instance]['layout']['line']
		
