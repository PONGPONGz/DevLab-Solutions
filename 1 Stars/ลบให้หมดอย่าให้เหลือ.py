# https://www.borntodev.com/devlab/task/500?languageId=71
n = []
i = int(input())
while True:
  n.append(i)
  try:
    i = int(input())
  except:
    break
  
for v in n[:-1]:
  print(v+n[-1])