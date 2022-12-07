H,M=map(int,input().split())
if M-45<0:
    H=H-1
    if H<0:
        H=H+24
    M=15+M
else:
    M=M-45
print(H,M)