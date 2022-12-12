import sys

n,x=map(int,sys.stdin.readline().split())
m=sys.stdin.readline()
list=m.split(" ")

xList=[]
for i in range(0,n):
    if x>int(list[i]):
        xList.append(int(list[i]))

for j in range(len(xList)):
    print(xList[j],end=' ')

