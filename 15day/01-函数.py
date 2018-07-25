def showSum(end):
	sum = 0
	for i in range(1,end+1):
		sum+=i
	print(sum)

num = int(input("请输入终止值"))
showSum(end)
