x=open("logs_cipher.txt")#extracting ciphertext from logs.
file=open("ciphertext.txt",'w')
count=0
for i in x:
    if "\t" in i:
        i=i.replace("\n","").replace("\t","").strip()
        if len(i)==16:
            file.write(i+"\n")
            count+=1
            print(count,end='\r')

