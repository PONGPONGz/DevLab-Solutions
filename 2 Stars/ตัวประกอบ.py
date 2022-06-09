# https://www.borntodev.com/devlab/task/429?languageId=71
n = int(input())
a = [str(i) for i in range(1, n+1) if n % i == 0]
print('{} : {}'.format(len(a), ','.join(a)))