def add():
	name = input("请输入名字")
	sex = input("请输入性别")
	d = {}
	d["name"] = name
	d["sex"] = sex
	student.append(d)
	
	print(student)
def delete():
	name = input("请输入姓名")
	for i in student:
		if i ["name"] == name:
			student.remove(i)
			print(student)
			break
def change():
	find = input("请输入需要修改的姓名")
	for j in student:
		if find == j["name"]:
			print("学生姓名为:%s\n学生的性别:%s\n"%(j["name"],j["sex"]))
			print("1、修改姓名")
			print("2、修改性别")
			num = int(input("请选择序号:"))
			if num == 1:
				name = input("请输入新名字:")
				j["name"] = name
			elif num == 2:
				sex = input("请输入新的性别:")
				j["sex"] == sex
		for k,v in j.items():
			print(k,v)

def find():
	f = input("请输入你要查找的姓名")
	for o in student:
		if f == o["name"]:
			print("你的姓名是:%s\n你的性别是%s\n"%(o["name"],o["sex"]))

def print_list():
	for i in student:
		print(i)

def print_menu():
	print("欢迎来到学生管理系统".center(30," "))
	while True:
		print("1、添加学生信息")
		print("2、删除学生信息")
		print("3、更改学生信息")
		print("4、查找学生信息")
		print("5、打印学生信息")
		print("6、退出学生信息")
		input_info()

def input_info():
	num = int(input("请输入功能:"))
	if num == 1:
		add()
	elif num == 2:
		delete()
	elif num == 3:
		change()
	elif num == 4:
		find()
	elif num == 5:
		print_list()
	elif num == 6:
		pass

print_menu()

