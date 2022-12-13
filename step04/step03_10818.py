import sys

n=int(sys.stdin.readline())
x=sys.stdin.readline()
xList=x.split(" ")

min=int(xList[0])
max=int(xList[0])

for i in range(0,n):
    if min>int(xList[i]):
        min=int(xList[i])
    if max<int(xList[i]):
        max=int(xList[i])

print(min,max)
