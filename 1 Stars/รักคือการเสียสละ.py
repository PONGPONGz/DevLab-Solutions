# https://www.borntodev.com/devlab/task/522?languageId=71
from string import punctuation
n=input()
print(''.join(list(filter(lambda x: x.lower() in 'aeiou', n))))
print(''.join(list(filter(lambda x: x.lower() not in 'aeiou '+punctuation, n))))