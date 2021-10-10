f= open("input.txt","r")
keywords=['public','static','private']
def keycheck(a):
    t=False
    for i in keywords:
        if i in a:
            t=True
            c.remove(i)
    if not t:
        while c:
            c.pop()
def listtostring(a):
    s=""
    for i in a:
        s+=i+' '
    return s



while c:=f.readline():
    if ('(' in c or ')' in c) and not ('main' in c or 'class' in c):
        c=c.split()
        keycheck(c)
        if len(c):
            type=c.pop(0)
            print(listtostring(c)+',return type:'+type)
