age = int(input("请输入年龄"))
learn = input("请输入学历")
if age > 18 and learn > "初中":
	print("入职")
elif age > 18 or learn < "初中":
	print("二次面试")
elif age < 18 and learn < "初中":
	print("拒绝")
