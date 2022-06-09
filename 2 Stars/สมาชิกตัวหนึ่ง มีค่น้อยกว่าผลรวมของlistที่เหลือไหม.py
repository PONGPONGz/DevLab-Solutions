# https://www.borntodev.com/devlab/task/402?languageId=71
n=list(map(int,input()[1:-1].split(',')))
for i in range(len(n)):
  if n[i] >= sum(n[:i]+n[i+1:]):
  	print('false')
  	break
else:
  print('true')