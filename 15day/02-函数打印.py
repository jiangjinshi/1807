list = []
import random
for i in range(10):
	j = random.randint(1,100)
	list.append(j)
	for i in list:
		if j in list:
			continue
		list.append(i)
print(list)
