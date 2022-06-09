# https://www.borntodev.com/devlab/task/551?languageId=71
i=input()
p=sum([ord(x)**len(i)for x in i])%9
print(9 if p==0else p)