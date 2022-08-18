d=list(open("ciphertext.txt"))
prev=[d.pop(0)]

for i in d: 
    if len(i)!=17:print(len(i))
    
    if prev[-1]==i:
        print(i)
    prev.append(i)

    