a=0
prime=True
while True:
    n=int(input())
    if n!=0:
        a=a+n
        for i in range(2,a):
            if a%i==0:
                prime=False
    else:
        break
if prime==False:#無法解決：印不出來
    print("False")
else:
    print("True")


