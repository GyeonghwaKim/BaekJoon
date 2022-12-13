import sys
n=int(sys.stdin.readline())
scores=list(map(int,sys.stdin.readline().split()))
max=max(scores)


print((sum(scores)/max*100)/n)