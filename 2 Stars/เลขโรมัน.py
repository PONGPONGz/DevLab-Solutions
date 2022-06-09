# https://www.borntodev.com/devlab/task/470?languageId=71
romans={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
n=input()
h1=max([i for i in n], key=lambda x: romans[x])
print(romans[h1]+sum([romans[i]for i in n[n.index(h1)+1:]])-sum([romans[i]for i in n[:n.index(h1)]]))