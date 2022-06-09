# https://www.borntodev.com/devlab/task/216?languageId=71
n = int(input())
categories = [input().split()for _ in range(int(input()))]
for i in categories:
  if n in range(int(i[0]), int(i[1])+1):
    print(i[-1])
    break