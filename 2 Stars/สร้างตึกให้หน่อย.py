# https://www.borntodev.com/devlab/task/721?languageId=71
a=int(input())
b,c=map(int,input().split())
print(*[' '.join('.'*b for _ in range(a))for _ in range(c)],sep='\n')