# https://www.borntodev.com/devlab/task/639?languageId=71
from re import findall
print(sum(x if x>0else 1for x in[sum(map(int,findall(r'[0-9]+', i)))for i in findall('[A-Z][^A-Z]*', input())]))