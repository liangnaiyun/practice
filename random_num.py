# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複去猜數字
# 猜對的話 印出 "終於猜對了！"
# 猜錯的話 要告訴他 比答案大/小
# 延伸一：印出猜了幾次
# 延伸二：讓使用者決定隨機數範圍

import random

define_random_start = input("請決定隨機數字範圍開始值：")
define_random_end = input("請決定隨機數字範圍結束值：")
input_title = "請輸入" + define_random_start + "~" + define_random_end + "數字："
define_random_start = int(define_random_start)
define_random_end = int(define_random_end)
answer = random.randint(define_random_start, define_random_end)
total_guest_count = 0

while True:
	user_guest_number = input(input_title)
	user_guest_number = int(user_guest_number)
	total_guest_count = total_guest_count + 1	
	if answer != user_guest_number:
		if answer > user_guest_number:
			print("比答案小")
		elif answer < user_guest_number:
			print("比答案大")
		print("這是你猜的第", total_guest_count, "次！")
	else:
		print("終於猜對了！")
		print("這是你猜的第", total_guest_count, "次！")
		break
