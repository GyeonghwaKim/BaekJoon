#주사위3개, 경우의 수 3개
a,b,c=map(int,input().split())
dice=[a,b,c]
d=0
if a==b:
    if a==c:
        print(10000+a*1000)
    else:
        print(1000+a*100)
elif b==c:
    print(1000+b*100)
elif a==c:
    print(1000+a*100)
else:
    for i in dice:
        if i>d:
            d=i
    print(d*100)