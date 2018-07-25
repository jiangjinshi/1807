def shangjia():
	name = input("请输入名字")
	count = input("请输入商品上架数量")
	price = float(input("请输入商品价格"))
	good["name"] = name
	good["count"] = count
	good["price"] = price
	
	list.append(good)

def buy():
	name = input("请输入商品名字")
	for good in list:
		if good["name"] = name:
			mygood = []
			count = int(input("请输入购买的数量"))
			mygood["name"] = name
			mygood["count"] = count
			mygood["price"] = good["price"]
			good["count"] = good["count"] - count
			buylist.append(mygood)
			break

def jisuan():
	money = 0
	for i in buylist:
		money += i["price"]*["count"]

	mymoney = float(input("请输入金额"))

	print(mymoney-money)
while True:
	num = int(input(""))

		
