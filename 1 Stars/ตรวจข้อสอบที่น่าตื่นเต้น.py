# https://www.borntodev.com/devlab/task/459?languageId=71
n,k,m,p=map(int,input().split())
a,b=input(),input()
print('Your score:{}'.format(sum(k if a[i] == b[i] else -m if b[i] != 'X' else p for i in range(n))))
  