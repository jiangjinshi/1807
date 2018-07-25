list = ["孟磊","王楠","赵平先"]
for i in list:
	print(i,"我想邀请你共进晚餐")
list[2]="老王"
print("赵平先无法赴约")
for o in list:
	print(o,"我想邀请你共进晚餐")
print("我刚找到了一个更大的餐桌")
list.insert(0,"老王")
list.insert(2,"老宋")
list.append("老李")
for u in list:
	print("%s我想邀请你共进晚餐"%u)
print("我只能邀请两位嘉宾")

