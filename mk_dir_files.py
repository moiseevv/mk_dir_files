import os,re
path_ishodn = '/home/bitrix/www/upload_2'
path_created = '/home/bitrix/www/upload_4'

def create_log(str_messa):
	with open('log_mk_config.txt','a') as file:
		print(str_messa, file=file)

def create_dir(path):
	if not os.path.isdir(path):
		os.mkdir(path)
		os.chmod(path, 0o777)
		create_log(f'Created directory {path}')
	else:
		create_log(f'Directory has created before - {path}')
def file_copy(path_src):
	path_src_new = path_src.replace(path_ishodn, path_created)
	if not os.path.isfile(path_src_new):
		cmd_copy = f'cp {path_src} {path_src_new}'
		os.popen(cmd_copy)
		cmd_chmod = f'chmod 777 {path_src_new}'
		create_log(f'create file - {path_src_new}')
	

def chech_cicly(mas_dir, path_src_in):
	create_log('		Started cicly')
	create_log(f'	massiv for work --- {mas_dir}')
	create_log(f'	path for work - {path_src_in}')
	for i in mas_dir:
		path_src = os.path.join(path_src_in,i)
		if not os.path.isdir(path_src):
			file_copy(path_src)	
		if os.path.isdir(path_src):
			path_src_new = path_src.replace(path_ishodn, path_created)
			create_dir(path_src_new)
			if (i in ['crm','tmp','tag']) or (not re.search('^[0-9a-wA-W]{3}$',i)):
				mas_dir_include = os.listdir(path_src)
				chech_cicly(mas_dir_include, path_src)
			else:
				create_log('!!!!used continue')
				continue


def make_derictory_files(path_ishodn, path_screated):
	mas_dir = os.listdir(path_ishodn)
	path_src = path_ishodn
	chech_cicly(mas_dir, path_src)


	
create_dir(path_created)
make_derictory_files(path_ishodn, path_created)
