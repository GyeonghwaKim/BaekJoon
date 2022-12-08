import sys
num=int(input())
A=[]
B=[]
for i in range(num):
    a,b=map(int,sys.stdin.readline().split())
    A.append(a)
    B.append(b)

for j in range(num):
    print("Case #{}: {}".format(j+1,A[j]+B[j]) )