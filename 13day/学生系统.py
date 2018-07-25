a = []
while True:
	print("欢迎来到学生系统")
	print("1:添加学生信息")
	print("2:查找学生信息")
	print("3:修改学生信息")
	print("4:删除学生信息")
	print("5:退出学生系统")
	i = int(input("请输入序号:"))
	if i == 1:
		name = input("请输入姓名")
		age = input("请输入年龄")
		sex = input("请输入性别")
		d = {}
		d["name"] = name
		d["age"] = age
		d["sex"] = sex
		a.append(d)
		print(a)	

	
