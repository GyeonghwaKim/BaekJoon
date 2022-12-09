a=int(input())
num=a
cnt=0
while (True):
    b=num//10
    c=num%10
    d=(b+c)%10
    num=(b*10)+d
    cnt=cnt+1
    if(num==a):
        break

print(cnt)



