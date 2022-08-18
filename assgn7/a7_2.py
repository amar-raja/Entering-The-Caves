from sys import setrecursionlimit
def check():
    for i in range(len(x)):
        zzz=0
        for a in z:
            zzz=(zzz+((a**i))%127)%127
        if zzz!=x[i]:return False 
    return True
setrecursionlimit(10**6)
found=False 
def func(i,s,p,c):
    global cc , found 
    if found:return    
    if i==20:
        if s==0:
            cc+=1 
            print(cc,end='\r')
            if check():
                found=True 
                password=""
                for i in z:
                    password+=chr(i)
                print("\nFound\nPassword is: "+password)
        return 
    if not dp[i,s,c]:return 
    for j in range(c,118):
        z[i]= j 
        func(i+1,(s - (j**p)%127)%127,p,j)
def f(i,s,p,c):
    if i==20:return True if s==0 else False
    if (i,s,c) in dp:return dp[i,s,c]
    ans=False 
    for j in range(c,118):
        ans=f(i+1,(s - (j**p)%127)%127,p,j) or ans 
    dp[i,s,c]=ans 
    return dp[i,s,c]
cc=0
z=[0 for i in range(20)]
x=[int(i) for i in "20 25 76 83 76 125 27 9 117 41 13 60 114 26 89 103 1 23 13 100 101 2 4 78 39 72 36 90 2 64 49 32".split()]
res=[]
dp={}
f(0,41,9,102)
func(0,41,9,102)