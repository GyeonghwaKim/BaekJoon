num=int(input())
A=[]
B=[]
for i in range(0,num):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

for j in range(0,num):
    print(A[j]+B[j])
