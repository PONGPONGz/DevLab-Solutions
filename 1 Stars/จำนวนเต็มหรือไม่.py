# https://www.borntodev.com/devlab/task/351?languageId=71
from math import sqrt
a=str(sqrt(int(input()))).split('.')
print('Integer'if a[1]=='0'and len(a[1])==1 else'Float')