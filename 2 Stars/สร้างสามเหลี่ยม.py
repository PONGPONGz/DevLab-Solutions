# https://www.borntodev.com/devlab/task/602?languageId=71
n=int(input())
print('\n'.join((' '*(n-i-1))+'/'+('  '*i)+'\\'for i in range(n-1)))
print('/'+('__'*(n-1))+'\\')