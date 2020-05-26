svg_cmd_dict = [
    'line', 'circle', 'rect'    
]

def render_svg(slef_dict, sdef_dict):
	for instance in sdef_dict:
                print 'render:'+instance
		        if 'layout' in sdef_dict[instance]:
			        for module in sdef_dict[instance]['layout']:
				        if module == 'line':
					        print sdef_dict[instance]['layout']['line']
                                        if module in svg_cmd_dict:
                                                print 'svg native cmd: ' + module
				                #print sdef_dict[instance]['layout'][module]
                                        elif module in slef_dict:
                                                print 'slef cmd: ' + module
                                        else:
                                                print 'cmd not support: ' + module
                print 'render done'
		
