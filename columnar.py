
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

start=0
end=lkey

while start in range(0,end) and end in range(start,lpt):
    print(start,end)
    start=end+1
    end=lkey+1
    
