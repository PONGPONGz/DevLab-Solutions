# https://www.borntodev.com/devlab/task/533?languageId=71
n=int(input())
s='th'
if n == 1:
  s='st'
elif n == 2:
  s='nd'
print('Error! Not have this floor' if n not in range(1, 6) else 'OK! Wait please\n---------------\nLift is arriving!\n---------------\nLift is going up!\n---------------\nLift has reached the {}{} floor!'.format(n, s))