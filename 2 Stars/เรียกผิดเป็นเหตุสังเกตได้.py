# https://www.borntodev.com/devlab/task/655?languageId=71
x,n,g=int(input()),int(input()),int(input())
r=max(0,g-n)
a=(r*(r+1))//2
print('Krit was arrested'if a>1000or a>=x else x-a)