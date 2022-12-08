totalPrice=int(input())
totalNum=int(input())
priceSum=0
for i in range(totalNum):
    price,num=map(int,input().split())
    priceSum=priceSum+(price*num)

if totalPrice==priceSum:
    print("Yes")
else:
    print("No")