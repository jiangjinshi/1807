list = ["100","99","98","97","96","95"]
count = 0
for i in list:
	print("索引是%d 索引上的值%s"%(count,i))
	count+=1
for i,j in enumerate(list):
	print(i,j)
