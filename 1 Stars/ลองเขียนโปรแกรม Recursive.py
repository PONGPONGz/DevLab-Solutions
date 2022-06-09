# https://www.borntodev.com/devlab/task/358?languageId=71
def f(n):
  return f(n-1)+100 if n > 0 else (1 if n == 0 else -1)
print(f(int(input())))