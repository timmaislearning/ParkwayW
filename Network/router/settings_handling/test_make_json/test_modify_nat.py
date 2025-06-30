import json
import socket
import os

def get_config_object(s_config):
	s_out = '{'
	i_current_indent = -1
	i_multiplyer = 4
	for s_line in s_config.splitlines():
		s_striped_line = s_line.strip(' ')
		i_spaces = len(s_line) - len(s_striped_line)
		i_loop_indent = i_spaces / i_multiplyer

		if i_loop_indent == i_current_indent and b_object_has_data:
			s_out += ','

		if s_striped_line[-1:] == '{': #is object start
			b_object_has_data = False
			s_out += '"'+s_striped_line[:-2].strip('"')+'":{'

		elif s_striped_line[-1:] == '}': #is object end
			b_object_has_data = True
			s_out += '}'

		else :# is property#
			b_object_has_data = True
			tmp = s_striped_line.split(' ', 1)
			if len(tmp) == 1:
				tmp.append('"true"')
			s_out += '"'+tmp[0]+'":'+json.dumps(tmp[1].strip('"'))

		i_current_indent = i_loop_indent
	s_out += '}'
	#print out
	return json.loads(s_out)

#s_cfg_path = '/opt/vyatta/sbin/vyatta-cfg-cmd-wrapper'
#f_handle = os.popen(s_cfg_path+ ' show')

raw_file = open("config.boot","rt")
s_config = raw_file.read()
o_config = get_config_object(s_config)
#print(o_config)

file = open("config.boot.json", "w")
#print(type(o_config))
## determined that the o_config is a dict, yet write accepts strings, so while I could use str(o_config), links 1 and 2 show json.dumps.  Link 3 shows it needed indent to make it pretty json.
#1# https://duckduckgo.com/?q=convert+dict+to+string&ia=web
#2# https://stackoverflow.com/questions/4547274/convert-a-python-dict-to-a-string-and-back#4547331
#3# http://stackoverflow.com/questions/12943819/ddg#12944035
file.write(json.dumps(o_config, indent=4))
file.close()
