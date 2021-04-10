import csv
import os.path
from os import path

encoding = 'utf-8'
delimiter = ','
products = []
file='products.csv'

#檢查檔案是否存在
def read_file(file='products.csv', encoding='utf-8', delimiter=','):
	products = []
	if path.exists(file):
		#先讀取原本資料
		with open(file, 'r', newline = '', encoding = encoding) as f:
			rows = csv.reader(f, delimiter = delimiter)
			for row in rows:
				if ['商品', '價格'] == row:
					continue
				print(row)
				products.append(row)
	else:
		print('找不到檔案......')
	return products


def user_input(products):
	#讓使用者輸入商品、價錢
	while True:
		name = input('請輸入商品名稱：')
		if name == 'q':
			break
		price = input('請輸入商品價格：')
		products.append([name,price])
	return products

def print_products(products):
	for p in products:
		print(p)

def writer_file(products, file='products.csv', encoding='utf-8', delimiter=','):
	#寫入檔案
	#使用newline可以讓寫入資料的每一個不要多一行空白行
	with open(file, 'w', newline = '', encoding = encoding) as f:
		writer = csv.writer(f, delimiter=delimiter)
		writer.writerow(['商品', '價格'])
		for p in products:
			writer.writerow([p[0], p[1]])


products = read_file()
products = user_input(products)
print_products(products)
writer_file(products)
