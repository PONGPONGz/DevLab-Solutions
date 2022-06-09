# https://www.borntodev.com/devlab/task/640?languageId=71
def f(n):
  return n * f(n-1) if n > 0 else 1
n=int(input()[1:-1])
print(f"{n}!:{f(n)}")