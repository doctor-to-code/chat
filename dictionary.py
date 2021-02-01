

words = {
	'wood': '木頭',
	'food': '食物',
	'gold': '黃金'
}

words['tea'] = '茶'
print(words)


p0 = {
	'name': '珍珠紅茶',
	'price': 30,
	'Remarks': '微冰微糖'
}

p1 = {
	'name': '蜂蜜綠',
	'price': 35,
	'Remarks': '微冰半蜜'
}

drinks = [p0, p1]
print(drinks[0])
print(drinks[1]['Remarks'])