n=int(input())
m=input()
list=m.split(' ')
v=input()
cnt=0
for i in range(0,n):
    if v==list[i]:
        cnt=cnt+1


print(cnt)