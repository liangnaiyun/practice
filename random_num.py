# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複去猜數字
# 猜對的話 印出 "終於猜對了！"
# 猜錯的話 要告訴他 比答案大/小
# 延伸一：印出猜了幾次

import random

answer = random.randint(1, 100)
total_guest_count = 0
while True:
	user_guest_number = input("請輸入1~100數字：")
	user_guest_number = int(user_guest_number)
	total_guest_count = total_guest_count + 1	
	if answer != user_guest_number:
		if answer > user_guest_number:
			print("比答案小")
		elif answer < user_guest_number:
			print("比答案大")
	else:
		print("終於猜對了！")
		print("共猜了", total_guest_count, "次！")
		break
