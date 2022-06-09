# https://www.borntodev.com/devlab/task/349?languageId=71
from math import sqrt
sqrted = sqrt(int(input()))
if str(sqrted)[-1] != '0':
  print('No Numbers Matching!')
else:
  print(int(sqrted))