import os.path
from os import path

#程式進入點
def  main():
	filename_read = 'input.txt'
	filename_write = 'output.txt'
	if os.path.exists(filename_read):
		print('檔案存在')
		str_arr = read_file(filename_read)
		write_file(str_arr, filename_write)
	else:
		print('找不到', filename_read)
	
def read_file(filename):
	str_arr = []
	current_user_name = ''
	with open(filename, 'r', encoding = 'utf-8-sig', newline = '') as f:
		for line in f:
			line = line.strip()
			if line == 'Allen':
				current_user_name = line
			elif line == 'Tom':
				current_user_name = line
			else:
				str_ele = current_user_name + '：' + line + '\n'
				str_arr.append(str_ele)
	return str_arr

def write_file(str_arr, filename):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for s in str_arr:
			f.write(s)


main()