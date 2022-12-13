import sys
remains=[]
for i in range(10):
    num=int(sys.stdin.readline())
    remains.append(num%42)

print(len(set(remains)))
