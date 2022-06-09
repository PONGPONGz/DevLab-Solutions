# https://www.borntodev.com/devlab/task/412?languageId=71
n=int(input())
if n <= 2:
  print("Box's height must be more than 2")
else:
  print('#'*n)
  for i in range(n-2):
    print('#'+' '*(n-2)+'#')
  print('#'*n)