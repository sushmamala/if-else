sum=0
i=1
while i<=11:
    weight=int(input("enter the weight"))
    sum=sum+weight
    i=i+1
    while (sum/11)%5==0:
        print("divisible")
    else:
        print("not divisible")
       
