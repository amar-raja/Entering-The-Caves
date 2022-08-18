import os

password=""

def func():
    x=open("output.txt")#extracting ciphertext from logs.
    file=open("ciphers.txt",'w')
    c=0
    for i in x:
        if "\t" in i:
        	i=i.replace("\n","").replace("\t","").strip()
        	if len(i)==16:
        		file.write(i+"\n")
        		c+=1

    file.close()
    x.close()

block=1
for cipher_password in ("lhhklqfgiqfhislj","ljipgjfpgmjtktho"):
	
    partial_password=""

    

    for l in range(8):

        file=open('input.txt','w')

        for i in range(8):
	
            for j in range(16):

                z=partial_password+chr(ord('f')+i)+chr(ord('f')+j)+'f'*(16-2*l-2)
                #z='f'*(16-2*l-2)+chr(ord('f')+i)+chr(ord('f')+j)+partial_password
			
                file.write(z+"\n")

        file.close()



        open("output.txt",'w').close()

        #os.system("gnome-terminal -- expect inputs.exp")
        os.system("sh cipher.sh")
        func()
        #break
        file=open("ciphers.txt",encoding='utf-8')

        data=list(file)

        file.close()

        for i in range(8):

            for j in range(16):

                z=data.pop(0).replace("\n","")
		 
                #if z[14-l:16-l]==cipher_password[14-l:16-l]:
                if z[2*l:2*l+2]==cipher_password[2*l:2*l+2]:
                	partial_password+=chr(ord('f')+i)+chr(ord('f')+j)
                    #partial_password=chr(ord('f')+i)+chr(ord('f')+j)+partial_password
        print("Block :",block,", Byte:",l+1) 

    password+=partial_password
    block+=1
passw=""
fi={}
c=0
for i in range(8):
    for j in range(16):
        fi[chr(ord('f')+i)+chr(ord('f')+j)]=c
        c+=1
for i in range(0,len(password),2):
    passw+=chr(fi[password[i:i+2]])
passw="".join(i for i in passw if i!='0')
print("Decrypted Password is:  ",passw)