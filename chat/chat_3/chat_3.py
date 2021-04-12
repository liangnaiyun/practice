#實作練習：清單分割法取出人名


def main():
	read_file('3.txt')


def read_file(filename):
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			arr = line.strip().split(' ')
			name = arr[0][5:]
			print(name)

main()
