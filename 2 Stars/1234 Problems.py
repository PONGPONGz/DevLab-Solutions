# https://www.borntodev.com/devlab/task/309?languageId=71
#(n / 2)(first number + last number) = sum, where n is the number of integers.
n,m,k,a=map(int,input().split())
r = ((m-n+1)/2)*(k+k+((m-n)*a))
print('YES'if r>=1234else 1234-int(r))

