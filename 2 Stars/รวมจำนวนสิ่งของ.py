# https://www.borntodev.com/devlab/task/306?languageId=71
a, b = list(map(int, input().split())), list(map(int, input().split()))
for i in range(max(len(a),len(b))):
  try:
    a[i]=a[i]+b[i]
    if a[i] > 32548:raise
  except:
    print('Invalid')
    break
else:
  print(*a)