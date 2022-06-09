# https://www.borntodev.com/devlab/task/755?languageId=71
n=int(input())
while n > 0:
    print('{} = {}'.format(str(n), 'even'if n%2==0 else'odd'))
    n=int(input())