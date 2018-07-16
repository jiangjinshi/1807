import random
i = 0
num = random.randint(1,100)
#while i > 9:
for i in range(1,11):
	u_num = int(input("请输入猜的数字"))
	if u_num > num:
		print("你猜大了，兄弟")
	elif u_num < num:
		print("你猜小了，兄弟")
	else:
		print("你真厉害，兄弟")	
		break
	i +=1

