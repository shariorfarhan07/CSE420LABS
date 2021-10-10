import re
numberOfReg=int(input('how many regx you want to enter: '))
reg=[]
string=[]
for i in range(numberOfReg):
    reg.append(input("please enter valid regx: "))
numberOfstr=int(input('how many string do you want to enter: '))
for i in range(numberOfstr):
    string.append(input("please enter valid regx: "))

def patternmatcher(a,b):
    pattern=re.compile(a)
    matches=pattern.finditer(b)
    b=False
    for i in matches:
      b=True
    return b

for i in string:
    t=False
    c=0
    cc=0
    for ii in reg:
        t=t or patternmatcher(ii,i)
        c+=1
        if patternmatcher(ii,i):
            cc=c
    if t:
        print('Yes',cc)
    else:
        print('No',cc)
