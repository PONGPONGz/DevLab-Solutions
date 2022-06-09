# https://www.borntodev.com/devlab/task/427?languageId=71
t=0
for i in range(int(input()),int(input())+1):
  t+=str(i).count('9')
print(t)