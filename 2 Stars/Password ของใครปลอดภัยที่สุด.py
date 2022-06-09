# https://www.borntodev.com/devlab/task/348?languageId=71
import re
passwords,scores=input().split(','),[]
for i in range(len(passwords)):
  password=passwords[i]
  t=0
  if len(password)>=6 and len(password)<=12:
  	t+=1
  if re.search(r'[a-z]', password):
  	t+=1
  if re.search(r'[A-Z]', password):
  	t+=1
  if re.search(r'[0-9]', password):
  	t+=1
  if re.search(r'[?:#|$|@]', password):
  	t+=1

  scores.append(t)

print('{} ({})'.format(passwords[scores.index(max(scores))], ['Man','Non','Miv'][scores.index(max(scores))]))