import csv
products = []

while  True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append([name,price])

print(products)

for p in products:
	print(p[0])
	print(p[1])

#使用newline可以讓寫入資料的每一個不要多一行空白行
with open('products.csv', 'w', newline = '') as f:
	writer = csv.writer(f)
	for p in products:
		writer.writerow([p[0], p[1]])