i = 1
while i <=9:
	j = 1
	while j <=i:
		a = i * j
		print("%d*%d=%d"%(j,i,a),end=" ")
		j += 1
	print("")
	i +=1
