import sys
#a,b=map(int,sys.stdin.readline().split())
A=[]
B=[]
num=0

while (True):
    a,b=map(int,sys.stdin.readline().split())
    if a==0 and b==0:
        break
    A.append(a)
    B.append(b)
    num=num+1
for i in range(num):
    print(A[i]+B[i])
