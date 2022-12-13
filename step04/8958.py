import sys
n=int(sys.stdin.readline())
ox_list=[]
score=1
sumScores=[]
sumScore=0
for i in range(n):
    ox_list=list(map(str,sys.stdin.readline().strip()))
    for ox in ox_list:
        if ox=='O':
            sumScore=sumScore+score
            score=score+1
        else:
            score=1
    sumScores.append(sumScore)
    sumScore=0
    score=1
    
for sum in sumScores:
    print(sum)
#풀이중