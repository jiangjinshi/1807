a = int(input("请输入成绩"))
b = int(input("请输入成绩"))
if a > 60:
	print("通过")
elif a < 60:
	print("未通过")
elif (a > 60) or (b < 60):
	print("补考")
