height=[176.5,177,154,165.8,156.4]
weight=[86.7,72.3,52.3,58.6,67.2]
bmi=[0,0,0,0,0]
for i in range(0,len(height)):#抽取出height的資料再放進去
    height[i]=height[i]/100
for i in range(0,len(bmi)):
    bmi[i]=weight[i]/(height[i]**2)#大家都要抽出第i個來計算
print(bmi)