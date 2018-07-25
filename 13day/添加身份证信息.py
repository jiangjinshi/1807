i = []
for a in range(3):
	name = input("请输入名字")
	age = input("请输入年龄")
	sex = input("请输入性别")
	d = {}
	d["name"] = name
	d["age"] = age
	d["sex"] = sex
	i.append(d)
print(i)
for j in i:
	for o in j:
		print(j[o])
