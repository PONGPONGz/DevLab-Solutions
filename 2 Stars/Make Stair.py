# https://www.borntodev.com/devlab/task/534?languageId=71
n=int(input())
print(' '*(n*3) + '__')
for i in range(n):
    print(' '*(n*3-((i+1)*3))+'__|')


