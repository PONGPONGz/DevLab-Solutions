# https://www.borntodev.com/devlab/task/389?languageId=71
from math import ceil
n, x = map(int, input().split())
print(sum(list(map(lambda i: ceil(int(i)*(1+(x/100))), input().split()))))