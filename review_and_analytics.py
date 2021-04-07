# 讀取一個留言檔(review.txt)
# 讀取檔案的過程中，每一千筆印出長度，才知道讀取進度
# 讀取完畢，顯示總共多少筆留言
# 計算留言的平均長度
# 篩選出長度小於100的留言

data = []
total_char_len = 0
count = 0
total_count = 0
with open('review.txt', 'r') as f:
	for line in f:
		count += 1
		line = line.strip('\n')
		data.append(line)
		if count % 1000 == 0:
			print(len(data))

total_count = len(data)
print('檔案讀取完了，總共有', total_count, '筆資料')

for d in data:
	total_char_len += len(d)

print('留言的平均長度為', total_char_len/total_count)

filter_review_list = []
for d in data:
	if len(d) < 100:
		filter_review_list.append(d)

print('一共有', len(filter_review_list), '筆留言長度小於100')


filter_review_list2 = []
for d in data:
	if 'good' in d:
		filter_review_list2.append(d)

print('一共有', len(filter_review_list2), '筆留言提到good')


# list 快寫法
# 篩選留言包含good
good_list = [d for d in data if 'good' in d]
print('一共有', len(good_list), '筆留言提到good')

bad = ['bad' in d for d in data]
print(bad)