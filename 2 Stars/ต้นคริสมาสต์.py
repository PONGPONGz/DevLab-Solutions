# https://www.borntodev.com/devlab/task/215?languageId=71
n=int(input())
for i in range(1,n+1):
	print((' '*n)+'*')
	for v in range(1,i+1):
		print((' '*(n-v))+('*'*(1+(2*v))))
print(' '*n + '|\n'+'='*n+'V'+'='*n)