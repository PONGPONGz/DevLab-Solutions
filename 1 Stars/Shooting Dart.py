# https://www.borntodev.com/devlab/task/416?languageId=71
t=0
n=int(input())
for i in range(5, 0, -1):
  t += n // i
  n = n % i
print(t)
  