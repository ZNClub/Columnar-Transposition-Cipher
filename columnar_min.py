# cook your dish here


#####   Implement Single & Double Columnar Cipher
####    
###     Version 1.0 - Nevil Dsouza
##

### PT
pt="This is a columnar transposition".lower()
#py=input("Enter PLAIN TEXT":)

### Filter whitespaces
pt = pt.replace(" ","")

key="apple"
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

lmat_pt = len(mat_pt)

###  encrypt data

ct=[]

for k in range(1,lkey+1):
    
    ### get current column number
    j=order.index(k)
    temp=[]
    
    for i in range(lmat_pt):
        temp.append(mat_pt[i][j])
    ct.append(temp)
### CT
CIPHER = ""
for i in ct:
    for j in i:
        CIPHER=CIPHER+j
Single=CIPHER
#print("PT=",pt,"\nKEY=",key,"\nCT=",Single)


#### Double Columnar Process


### divide pt into blocks
mat_pt=[]
for i in range(1,rows+1):
    if i==1:
        start=0
        end=lkey
    else:
        start=end
        end=i*lkey
    temp=[]
    temp=list(CIPHER[start:end])
    #print(temp)
    mat_pt.append(temp)

lmat_pt = len(mat_pt)


###  encrypt data

ct=[]

for k in range(1,lkey+1):
    
    ### get current column number
    j=order.index(k)
    temp=[]
    
    for i in range(lmat_pt):
        temp.append(mat_pt[i][j])
    ct.append(temp)
#print(ct)

### CT
CIPHER = ""
for i in ct:
    for j in i:
        CIPHER=CIPHER+j
Double=CIPHER
print("PT=",pt,"\nKEY=",key,"\nSingle CT=",Single,"\nDouble CT=",Double)


'''
PT= thisisacolumnartransposition!! 
KEY= apple 
Single CT= tsutpiilrst!soani!hamrooicnasn 
Double CT= titnmcpsaaintrohossi!irnuls!oa
'''
