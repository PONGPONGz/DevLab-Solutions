# https://www.borntodev.com/devlab/task/213?languageId=71
n=int(input())
print('#'*n)
if n > 1:
  for _ in range(n-2):
    print(f'#{" "*(n-2)}#')
  print('#'*n)