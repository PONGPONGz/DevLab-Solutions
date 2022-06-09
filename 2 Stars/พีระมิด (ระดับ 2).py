# https://www.borntodev.com/devlab/task/3?languageId=71
n=int(input())

for i in range(1, n*2, 2):
    print(' ' * (((n*2)-i)//2) + '*' * i)