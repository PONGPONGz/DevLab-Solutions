# https://www.borntodev.com/devlab/task/737?languageId=71
try:
  n=int(input())
  if n>1:
    for i in range(n-1):print('|'+' '*i+'\\')
    print('|'+'='*(n-1)+'\\')
  else:print('ERROR please input more than 1')
except:
  print('ERROR please input integer only')