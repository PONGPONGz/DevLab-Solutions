# https://www.borntodev.com/devlab/task/617?languageId=71
from re import findall
s,a=input(),0
n=list(map(int,findall('[0-9]+',s)))
if'+'in s:a=sum(n)
elif'-'in s:a=n[0]-n[1]
elif'*'in s:a=n[0]*n[1]
else:a=n[0]/n[1]

print(s + ' = ' + str(a))

