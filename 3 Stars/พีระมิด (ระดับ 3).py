# https://www.borntodev.com/devlab/task/4?languageId=71
n = int(input())
p=[' '*(n-i-1)+'*'*(i+i+1)for i in range(n)] 
print('{}\n{}'.format('\n'.join(p), '\n'.join(p[-2::-1])))

