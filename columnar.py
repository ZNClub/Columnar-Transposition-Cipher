
#####   Implement Single & Double Columnar Cipher
####    
###     Version 1.0 - Nevil Dsouza
##

pt="Cryptography"
#py=input("Enter PLAIN TEXT":)

key="znevzz"
#key=input("Enter CIPHER KEY":)

chars=list(key)

s_chars=sorted(chars)

#print(chars,s_chars)


order=[]

for i in chars:
    if i==-1:
        continue
    ind=s_chars.index(i)
    del s_chars[ind]
    s_chars.insert(ind,-1)
    order.append(ind+1)
#    print(chars)
#print(order)

