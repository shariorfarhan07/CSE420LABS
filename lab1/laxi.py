#ID18301266
#MD Sharior Hossain Farhan
f = open("input.txt", mode='r')
code=f.readlines()
k=['abstract','assert','boolean','break','byte','case','catch','char','class','continue','default','do','double','else','enum','extends','final','finally','float','for','if','implements','import','instanceof','int','interface','long','native','new','package','private','protected','public','return','short','static','strictfp','super','switch','synchronized','this','throw','throws','transient','try','void','volatile','while']
m=['+','-','*','/','%','=',]
l=['<','>','<=','>=','==','and','or',]
o=[',',';','(',')','{','}','}','}',]
key=set()
math=set()
log=set()
other=set()
number=set()
identifiers=set()
def syntaxchecker(line,syn,store):
    for i in syn:
        if i in line:
            store.add(i)
            line=line.replace(i,' ')
    return line
for i in code:
    i=syntaxchecker(i, k, key)
    i=syntaxchecker(i, m, math)
    i=syntaxchecker(i, l, log)
    i=syntaxchecker(i, o, other)
    i=i.strip().split(' ')
    for n in i:
        if i != '':
          if n.replace('.', '', 1).isnumeric():
              number.add(n)
          else:
              identifiers.add(n)
def p(a,set,c=' '):
    print(a,':',end='')
    s=''
    for i in set:
        if i!='':
            s+=i+c
    print(s[0:len(s)-1])
p('Keywords',key,',')
p('Identifiers',identifiers,',')
p('Math Operators',math,',')
p('Logical Operators',log,',')
p('Numerical Values',number,',')
p('other',other)