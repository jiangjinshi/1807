for j in range(2,101):
	flag = 1
	for i in range(2,j):
		if j % i == 0 :
			flag = 0
			break
	if flag == 1:
		print(j)
