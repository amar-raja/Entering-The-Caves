from random import randint
def convert(i):
    s=''
    for j in i:
        j=int(j,16)
        s+=chr(ord('d')+j)
    return s
xor="0000901010005000"#xor for 4 round characteristics
file=open('plaintext.txt','w')
for _ in range(100000):
    i=''
    for __ in range(16):
        i+=hex(randint(0,15))[2:]
    
    j="".join(hex(int(i[k],16)^int(xor[k],16))[2:] for k in range(16))
    i,j=convert(i),convert(j)
    file.write(i+"\n")
    file.write(j+"\n")
    print(_,end="\r")
#generating 100k pairs of plain text with the xor value of 0000901010005000