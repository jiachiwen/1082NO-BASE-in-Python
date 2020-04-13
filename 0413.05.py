element=[]
while True:
    a=int(input()) #不能規定輸入的種類
    if a!=0:
        element.append(a)
        print(";".join(element)) #join()只能用在串字串
    else:
        break

