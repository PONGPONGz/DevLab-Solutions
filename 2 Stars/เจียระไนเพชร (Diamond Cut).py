# https://www.borntodev.com/devlab/task/545?languageId=71
n, r = map(int, input().split())
d = ['*'*n]*n

for i in range(n):
  dif = max(0, r-i, i-n+r+1) 
  d[i] = ('-'*dif) + d[i][dif:n-dif] + ('-'*dif)

print('\n'.join(d))