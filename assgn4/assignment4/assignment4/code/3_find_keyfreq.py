
subbox = [
[14, 0, 4, 15, 13, 7, 1, 4, 2, 14, 15, 2, 11, 13, 8, 1, 
 3, 10, 10, 6, 6, 12, 12, 11, 5, 9, 9, 5, 0, 3, 7, 8, 
 4, 15, 1, 12, 14, 8, 8, 2, 13, 4, 6, 9, 2, 1, 11, 7,
 15, 5, 12, 11, 9, 3, 7, 14, 3, 10, 10, 0, 5, 6, 0, 13],

[15, 3, 1, 13, 8, 4, 14, 7, 6, 15, 11, 2, 3, 8, 4, 14,
9, 12, 7, 0, 2, 1, 13, 10, 12, 6, 0, 9, 5, 11, 10, 5,
0, 13, 14, 8, 7, 10, 11, 1, 10, 3, 4, 15, 13, 4, 1, 2,
5, 11, 8, 6, 12, 7, 6, 12, 9, 0, 3, 5, 2, 14, 15, 9],

[10, 13, 0, 7, 9, 0, 14, 9, 6, 3, 3, 4, 15, 6, 5, 10,
1, 2, 13, 8, 12, 5, 7, 14, 11, 12, 4, 11, 2, 15, 8, 1,
13, 1, 6, 10, 4, 13, 9, 0, 8, 6, 15, 9, 3, 8, 0, 7,
11, 4, 1, 15, 2, 14, 12, 3, 5, 11, 10, 5, 14, 2, 7, 12],

[7, 13, 13, 8, 14, 11, 3, 5, 0, 6, 6, 15, 9, 0, 10, 3,
1, 4, 2, 7, 8, 2, 5, 12, 11, 1, 12, 10, 4, 14, 15, 9,
10, 3, 6, 15, 9, 0, 0, 6, 12, 10, 11, 1, 7, 13, 13, 8,
15, 9, 1, 4, 3, 5, 14, 11, 5, 12, 2, 7, 8, 2, 4, 14],

[2, 14, 12, 11, 4, 2, 1, 12, 7, 4, 10, 7, 11, 13, 6, 1,
8, 5, 5, 0, 3, 15, 15, 10, 13, 3, 0, 9, 14, 8, 9, 6,
4, 11, 2, 8, 1, 12, 11, 7, 10, 1, 13, 14, 7, 2, 8, 13,
15, 6, 9, 15, 12, 0, 5, 9, 6, 10, 3, 4, 0, 5, 14, 3],

[12, 10, 1, 15, 10, 4, 15, 2, 9, 7, 2, 12, 6, 9, 8, 5,
0, 6, 13, 1, 3, 13, 4, 14, 14, 0, 7, 11, 5, 3, 11, 8,
9, 4, 14, 3, 15, 2, 5, 12, 2, 9, 8, 5, 12, 15, 3, 10,
7, 11, 0, 14, 4, 1, 10, 7, 1, 6, 13, 0, 11, 8, 6, 13],

[4, 13, 11, 0, 2, 11, 14, 7, 15, 4, 0, 9, 8, 1, 13, 10,
3, 14, 12, 3, 9, 5, 7, 12, 5, 2, 10, 15, 6, 8, 1, 6,
1, 6, 4, 11, 11, 13, 13, 8, 12, 1, 3, 4, 7, 10, 14, 7,
10, 9, 15, 5, 6, 0, 8, 15, 0, 14, 5, 2, 9, 3, 2, 12],

[13, 1, 2, 15, 8, 13, 4, 8, 6, 10, 15, 3, 11, 7, 1, 4,
10, 12, 9, 5, 3, 6, 14, 11, 5, 0, 0, 14, 12, 9, 7, 2,
7, 2, 11, 1, 4, 14, 1, 7, 9, 4, 12, 10, 14, 8, 2, 13,
0, 15, 6, 12, 10, 9, 13, 0, 15, 3, 3, 5, 5, 6, 8, 11]
]
expan = [32, 1, 2, 3, 4, 5,
      4, 5, 6, 7, 8, 9,
      8, 9, 10, 11, 12, 13,
      12, 13, 14, 15, 16, 17,
      16, 17, 18, 19, 20, 21,
      20, 21, 22, 23, 24, 25,
      24, 25, 26, 27, 28, 29,
      28, 29, 30, 31, 32, 1]
inversefinalperm = [57,49,41,33,25,17,9,1,
          59,51,43,35,27,19,11,3,
          61,53,45,37,29,21,13,5,
          63,55,47,39,31,23,15,7,
          58,50,42,34,26,18,10,2,
          60,52,44,36,28,20,12,4,
          62,54,46,38,30,22,14,6,
          64,56,48,40,32,24,16,8]
inverperm = [9, 17, 23, 31,
       13, 28, 2, 18,
       24, 16, 30, 6,
       26, 20, 10, 1,
       8, 14, 25, 3,
       4, 29, 11, 19,
       32, 12, 22, 7,
       5, 27, 15, 21]
def inverse_permutation(a):
    res=""
    for i in range(len(a)):
        res+=a[inverperm[i]-1]
    return res
def inverse_finalpermutation(a):
    res=""
    
    for i in range(len(a)):
        res+=a[inversefinalperm[i]-1]
    return res

def expansion(a):
    res=''
    for i in range(len(expan)):
        res+=a[expan[i]-1]
    return res 
def hexbin(a):
    res=''
    for i in a:
        i=bin(int(i,16))[2:]
        res+='0'*(4-len(i))+i
    return res
def strbin(a):
    a=a.replace("\n","")
    res=""
    for i in a:
        i=bin(ord(i)-ord('d'))[2:]
        res+='0'*(4-len(i))+i
    
    return res

l15=hexbin("04000000")
def xor(a,b):
    
    return "".join(str(int(a[i])^int(b[i])) for i in range(len(a)))
def left_right(j):
    i=x[j]
    i=i.replace("\n","")
    return expansion(i[:32]),i[32:]
def sbox(a,ind):
    res=[]
    a=int(a,2)
    for i in range(len(subbox)):
        if subbox[i]==a:
            res.append(i)
    row=int(a[0]+a[-1],2)
    col=int(a[1:-1],2)
    
    
    i=bin(subbox[ind][row][col])[2:]
    return '0'*(4-len(i))+i

def key(sbox_in,sbox_out,exp,ind):
    sbox_out=int(sbox_out,2)
    sbox_in=int(sbox_in,2)
    exp=int(exp,2)
    for sboxout1 in range(16):
        sboxout2=sbox_out^sboxout1
        for i in (kk for kk in range(len(subbox[ind])) if subbox[ind][kk]==sboxout1):
            for j in (ll for ll in range(len(subbox[ind])) if subbox[ind][ll]==sboxout2):
                if i^j==sbox_in:
                    zz=i^exp                
                    if zz in ke[ind]:
                        ke[ind][zz]+=1
                    else:
                        ke[ind][zz]=1
ke=[dict() for i in range(8)]
x=list(open("ciphertext2.txt",encoding='utf-8'))
for j in range(0,len(x),2):
    print(j,end='\r')
    if j+1>=len(x):break
    x[j]=inverse_finalpermutation(strbin(x[j]))
    x[j+1]=inverse_finalpermutation(strbin(x[j+1]))
    left1,right1=x[j][:32],x[j][32:]
    left2,right2=x[j+1][:32],x[j+1][32:]
    right=xor(right1,right2)
    right=xor(right,l15)
    sbox_out=inverse_permutation(right)
    sbox_in=expansion(xor(left1,left2))
    left1=expansion(left1)
    ccc=0
    for i in range(0,48,6):
        key(sbox_in[i:i+6],sbox_out[ccc:ccc+4],left1[i:i+6],i//6)
        ccc+=4


for i in range(8):
    print(i,ke[i])
ff=open("keys.txt",'w')
for i in range(8):
    zz=sorted(ke[i].items(),key=lambda j:(j[1],j[0]),reverse=True)
    ff.write(str(zz)+"\n")