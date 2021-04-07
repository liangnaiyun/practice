# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複去猜數字
# 猜對的話 印出 "終於猜對了！"
# 猜錯的話 要告訴他 比答案大/小

import random

answer = random.randint(1, 100)
while True:
	user_guest_number = input("請輸入1~100數字：")
	user_guest_number = int(user_guest_number)
	if answer != user_guest_number:
		if answer > user_guest_number:
			print("比答案小")
		elif answer < user_guest_number:
			print("比答案大")
	else:
		print("終於猜對了！")
		break
