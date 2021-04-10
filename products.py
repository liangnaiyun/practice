import csv
products = []

#先讀取原本資料
with open('products.csv', 'r', newline = '', encoding = 'utf-8') as f:
	rows = csv.reader(f, delimiter = ',')
	for row in rows:
		if ['商品', '價格'] == row:
			continue
		print(row)

#讓使用者輸入商品、價錢
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append([name,price])

#寫入檔案
#使用newline可以讓寫入資料的每一個不要多一行空白行
with open('products.csv', 'a', newline = '', encoding = 'utf-8') as f:
	writer = csv.writer(f, delimiter=',')
	writer.writerow(['商品', '價格'])
	for p in products:
		writer.writerow([p[0], p[1]])
