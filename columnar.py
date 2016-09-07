
#####   Implement Single & Double Columnar Cipher
####    
###     Version 1.0 - Nevil Dsouza
##

pt="Cryptographys"
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

#rows = lpt // lkey
rows,remain =divmod(lpt,lkey)
#print(rows,remain)
extra=lkey-remain


### append null char '!'
if remain>0:
    rows+=1
    for i in range(extra):
        
        pt=pt+"!"

#print(pt)
mat_pt = []

### divide pt into blocks

for i in range(1,rows+1):
    if i==1:
        start=0
        end=lkey
    else:
        start=end
        end=i*lkey
    temp=[]
    temp=list(pt[start:end])
    #print(temp)
    mat_pt.append(temp)

#print(mat_pt)

    
