# https://www.borntodev.com/devlab/task/223?languageId=71
p = input()
t=''
r=0

for i in range(len(p)):
    c = p[i]
    if c.isnumeric():
        t += c
    elif t != '':
        r += int(t)
        t = ''
if t != '':
    r += int(t)
    t = ''
r=str(r)
print(r if len(r)>=4 else '0'*(4-len(r))+r)