height = input ('請輸入您的身高: ')
weight = input ('請輸入您的體重: ')
height = int(height)
weight = int(weight)
height2 = (height * 0.01) ** 2
bmi = weight / height2

if bmi < 18.5:
	print('體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('體重正常')
elif bmi >= 24 and bmi < 27:
	print('體重過重')
elif bmi >= 27 and bmi < 30:
	print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('中度肥胖')
else:
	print('重度肥胖')
