
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


### generate blocks of PT

lkey=len(key)
lpt=len(pt)

rows = lpt // lkey
#print(rows)

mat_pt = []

for i in range(1,rows+1):
    if i==1:
        start=0
        end=lkey
    else:
        start=end
        end=i*lkey
    temp=[]
    temp=pt[start:end]
    print(temp)

    
