account = "jjs"
passwd = "123456"
i = 0
while True:
	z = input("输入账号")
	m = input("输入密码")
	if z == account and m == passwd:
		print("登陆成功")
		y = int(input("选择英雄范围0,ADC 1,肉 3,法师:"))
		if y == 0:
			print("鲁班大师")
		elif y == 1:
			print("程咬金")
		elif y == 3:
			print("王昭君")
		break
	else:
		i+=1
		print("已经错误%d次"%i)
		if i == 4:
			print("账号已冻结")

			break
