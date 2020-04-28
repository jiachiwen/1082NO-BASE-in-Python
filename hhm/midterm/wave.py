n = int(input())  # 輸入幾組
for i in range(n):
	a = int(input())  # 振幅
	f = int(input())  # 頻率
	if not 1 <= a <= 10 or not 1 <= f <= 100:
		print("無效資料組")
		continue
	
	for j in range(f):
		# 每個波上半
		for k in range(a+1):
			for l in range(k):
				if k == 10:
					print('0', end='')
				else:
					print(k, end="")
			print()
		# 波的下半
		for m in range(a-1, 0, -1):
			for p in range(m):
				print(m, end="")
			if m != 1:
				print()