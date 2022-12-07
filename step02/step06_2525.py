A,B=map(int,input().split())
C=int(input())
if B+C>=60:
    A=(A+((B+C)//60))%24
    D=(B+C)%60
   
else:
    D=B+C

print(A,D)