# https://www.borntodev.com/devlab/task/642?languageId=71
from string import ascii_lowercase
print(''.join([str(ascii_lowercase.index(i)+1) for i in input()]))