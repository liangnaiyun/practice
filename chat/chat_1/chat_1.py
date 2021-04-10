import os.path
from os import path

#程式進入點
def  main():
	filename_read = 'input.txt'
	filename_write = 'output.txt'
	if os.path.exists(filename_read):
		print('檔案存在')
		str_arr = read_file(filename_read)
		str_arr = convert(str_arr)
		write_file(str_arr, filename_write)
	else:
		print('找不到', filename_read)
	
def read_file(filename):
	str_arr = []
	#txt有時候會存編碼去除\ufeff，要使用utf-8-sig編碼
	with open(filename, 'r', encoding = 'utf-8-sig', newline = '') as f:
		for line in f:
			str_arr.append(line.strip())
	return str_arr

def convert(str_arr):
	convert_str_arr = []
	current_user_name = ''
	for line in str_arr:
		if line == 'Allen':
			current_user_name = line
		elif line == 'Tom':
			current_user_name = line
		else:
			convert_str_arr.append(current_user_name + '：' + line + '\n')
	return convert_str_arr


def write_file(str_arr, filename):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for s in str_arr:
			f.write(s)


main()