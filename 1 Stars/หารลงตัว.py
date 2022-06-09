# https://www.borntodev.com/devlab/task/356?languageId=71
a=[]
for i in list(map(int, input().split(','))):
  if (i % 7 == 0 and not i % 11 == 0) or i == 1:
    a.append(i)
print(*a,sep=',')