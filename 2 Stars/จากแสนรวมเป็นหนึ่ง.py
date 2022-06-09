# https://www.borntodev.com/devlab/task/211?languageId=71
n=input()
while len(n) > 1:
  n = str(sum(map(int, n)))
print(n)