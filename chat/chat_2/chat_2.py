import os.path
from os import path

#程式進入點
def  main():
	filename_read = 'LINE-Viki.txt'
	filename_write = 'output.txt'
	if os.path.exists(filename_read):
		print('檔案存在')
		str_arr = read_file(filename_read)
		str_arr = convert(str_arr)
		#write_file(str_arr, filename_write)
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
	current_user_name = None
	Allen_word_count = []
	Allen_sticker_count = 0
	Allen_image_count = 0
	Viki_word_count = []
	Viki_sticker_count = 0
	Viki_image_count = 0
	for line in str_arr:
		s = line.split(' ')
		current_user_name = s[1]
		if current_user_name == 'Allen':
			if s[2] == '貼圖':
				Allen_sticker_count += 1
			elif s[2] == '圖片':
				Allen_image_count += 1
			else:
				Allen_word_count.append(list_total_character(s[2:]))

		elif current_user_name == 'Viki':
			if s[2] == '貼圖':
				Viki_sticker_count += 1
			elif s[2] == '圖片':
				Viki_image_count += 1
			else:
				Viki_word_count.append(list_total_character(s[2:]))
			
	print('Allen說了', sum(Allen_word_count), '字')
	print('Allen傳了', Allen_sticker_count, '貼圖')
	print('Allen傳了', Allen_image_count, '圖片')
	print('Viki說了', sum(Viki_word_count), '字')
	print('Viki傳了', Viki_sticker_count, '貼圖')
	print('Viki傳了', Viki_image_count, '圖片')
	return convert_str_arr


def write_file(str_arr, filename):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for s in str_arr:
			f.write(s)


def list_total_character(target):
	length = 0
	for line in target:
		length += len(line)
	return length


main()