pc2 = [                
  14, 17, 11, 24,  1, 5,
  3, 28 ,15,  6, 21, 10,
  23, 19, 12,  4, 26, 8,
  16,  7, 27, 20, 13, 2,
  41, 52, 31, 37, 47, 55,
  30, 40, 51, 45, 33, 48,
  44, 49, 39, 56, 34, 53,
  46, 42, 50, 36, 29, 32
]


s="101101110011XXXXXXXXXXXX001111010000001001111101"#hardcoded key from key frequencies. X means we do not know that particular bit. 
key=['X']*56
for i in range(len(s)):
    key[pc2[i]-1]=s[i]
          
shifts=[1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]     
for i in range(6): 
    for j in range(shifts[i]):
        le,ri=key[:28],key[28:]
        le=[le[-1]]+le[:-1]
        ri=[ri[-1]]+ri[:-1]
        key=le+ri
key="".join(key)#original 56bit key.
print(key)
def f(i,s):
    if i==l:
        file.write(s+"\n")
        return 
    if key[i]=='X':
        f(i+1,s+'0')
        f(i+1,s+'1')
    else:
        f(i+1,s+key[i])
file=open("allkeys.txt",'w')
l=len(key)
f(0,'')#generating all the 2^20 keys to be bruteforced. 