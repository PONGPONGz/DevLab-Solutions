# https://www.borntodev.com/devlab/task/434?languageId=71
from math import sqrt
a=sqrt(int(input())**2+int(input())**2)
print(('{:.0f}'if str(a)[-1]=='0'else '{:.2f}').format(a))