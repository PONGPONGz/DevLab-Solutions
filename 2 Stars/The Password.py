# https://www.borntodev.com/devlab/task/212?languageId=71
from string import punctuation, digits
i = input()
l = len(i)

if (l >= 3 and l <= 20) and (i.lower() != i) and (i.upper() != i) and list(filter(lambda x: x, [v in digits for v in i])) and list(filter(lambda x: x, [v in punctuation for v in i])):
  print('Valid')
else:
  print('Invalid')