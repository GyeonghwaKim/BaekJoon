import sys
nList=[]
max=0
for i in range(0,9):
    n=int(sys.stdin.readline())
    nList.append(n)
    if max<n:
        max=n

print(max)
print(nList.index(max)+1)
