subnum={
    'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,
    'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25
    }

def get_key(val):
    for key, value in subnum.items():
         if val == value:
             return key
 
    return "key doesn't exist"

def caesercipherEncryption(s,k):
    g=""
    for i in s:
        a=subnum[i]
        b=a+k
        c=b%26
        i=get_key(c)
        g+=i
    
    return g

def caesercipherDecryption(s,k):
    g=""
    for i in s:
        a=subnum[i]
        b=a-k
        c=b%26
        i=get_key(c)
        g+=i
    
    return g

def getkey(str,key):
    key=list(key)
    if len(str)==len(key):
        return key
    else:
        for i in range(len(str)-len(key)):
            key.append(key[i%len(key)])
    return ("".join(key))        

def polyalphabeticEncryption(str,key):
    ciphertext=[]
    for i in range(len(str)):
        x=(ord(str[i])+ord(key[i]))%26
        -1
        x+=ord('A')
        ciphertext.append(chr(x))
    return("".join(ciphertext))    

def polyalphabeticDecryption(str,key):
    orig_text = []
    for i in range(len(str)):
        x = (ord(str[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))    
print("enter message to be encrypted: ")
str=str(input())
str=str.replace(" ","")
print("enter key: ")
k=input()
c1=caesercipherEncryption(str,k)
print("the first caeser cipher is: ",c1)
print("enter key for polyalphabetic cipher: ")
k2=input()
key=getkey(c1,k2)
key=key.upper()
c1=c1.upper()
c2=polyalphabeticEncryption(c1,key)
print("the final encrypted message shared is: \n\n")
print(c2)
pt1=polyalphabeticDecryption(c2,key)
print("message after polyalphabetic decryption is: ",pt1)
pt1=pt1.lower()
pt2=caesercipherDecryption(pt1,k)
print("original plain text is: \n\n")
print(pt2)
