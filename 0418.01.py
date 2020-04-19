'''
請使用者一直輸入，直到輸入 0 為止
每次使用者輸入一個數字就把他加入 list 中，並且印出目前 list 中排列
過後的所有元素
按照數字大小排列
印出來元素與元素使用逗號隔開

記得型態要轉換才可以使用
'''
#join只能用於字串排列

element=[]
while True:
	a=int(input())
	if a!=0:
		element.append(a)
		element.sort()
		for i in element:
			print(i,end=",")
		print()
	else:
		break