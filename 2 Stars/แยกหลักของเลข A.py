# https://www.borntodev.com/devlab/task/395?languageId=71
n=input()

try:
    n = int(n)
    if n > 1000000:raise ValueError('OVER')
    elif n < 0:raise ValueError('UNDER')
    else:n=str(n);print(*[int(i)*10**(len(n)-n.index(i)-1)for i in n],sep='\n')
except ValueError as e:
  	print(e.args[0]if not'invalid'in e.args[0]else'Invalid')