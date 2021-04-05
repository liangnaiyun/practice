# 密碼重試練習
# 先在程式碼中，設定好密碼 password = 'a123456'
# 讓使用者【最多輸入３次密碼】
# 不對的話，就印出＂密碼錯誤！　還有＿次機會＂
# 對的話，就印出＂登入成功＂

password = 'a123456'
limit_error_count = 3
while limit_error_count > 0:
	user_input_password = input('請輸入密碼：')
	if user_input_password != password:
		limit_error_count = limit_error_count - 1
		if limit_error_count == 0:
			print('密碼輸入錯誤達3次以上，帳號已被鎖定')
		else:
			print('密碼錯誤！ 還有', limit_error_count, '次機會')
	else:
		print('登入成功')
		break
