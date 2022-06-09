# https://www.borntodev.com/devlab/task/210?languageId=71
def f(n):
  return n*f(n-1) if n > 1 else n or 1

print(f(int(input())))