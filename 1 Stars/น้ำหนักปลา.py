# https://www.borntodev.com/devlab/task/224?languageId=71
a = int(input())
n = []
while a != 0:
  n.append(a)
  a = int(input())
print(*sorted(n, reverse=(input() == 'MaX')))