for i in range(1, 10):  # 被乘數
	for m in range(1,10):  # 乘數
		# 個位數的話要考慮對齊的問題
		if i * m >= 10:
			print(i, "*", m, "=", i*m, end=" ")
		else:  # 個位數
			print(i, "*", m, "=", i*m, end="  ")  # 只有個位數的話，十位數的位置要補空格
	print()  # 算完一輪後換行，再繼續算下一個被乘數