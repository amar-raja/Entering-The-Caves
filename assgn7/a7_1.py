from sys import setrecursionlimit

setrecursionlimit(10**6)
found=False 
def f(i,s,p,c):
    if i==20:return 1 if s==0 else 0
    if (i,s,c) in dp:return dp[i,s,c]
    ans=0
    for j in range(c,118):
        ans+=f(i+1,(s - (j**p)%127)%127,p,j)
    dp[i,s,c]=ans 
    return ans 
cc=0
z=[]
x=[int(i) for i in "20 25 76 83 76 125 27 9 117 41 13 60 114 26 89 103 1 23 13 100 101 2 4 78 39 72 36 90 2 64 49 32".split()]
res=[]
for i in range(32):
    dp={}
    res.append((i,f(0,x[i],i,102)))
res.sort(reverse=True,key=lambda i:i[1])
print(res)