# https://www.borntodev.com/devlab/task/484?languageId=71
m, y = map(int, input().split())
y-=543
t = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if m != 2:
  print(t[m-1])
elif y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
  print(29)
else:
  print(28)