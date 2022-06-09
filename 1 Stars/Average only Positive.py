# https://www.borntodev.com/devlab/task/490?languageId=71
global n
n=float(input())
s=[]
while n > 0:
  s.append(n)
  n = float(input())
  
print('{:.02f}'.format(sum(s)/len(s)) if len(s) > 0 else 'No Data')