def f(i,s):
    if i==l:
        file.write(s+"\n")
        return 
    if key[i]=='X':
        f(i+1,s+'0')
        f(i+1,s+'1')
    else:
        f(i+1,s+key[i])
key="XX1XX1XXX10X1X10XXX11XX10X0X1001001X10001100X11X1101X001"
file=open("allkeys.txt",'w')
l=len(key)
f(0,'')