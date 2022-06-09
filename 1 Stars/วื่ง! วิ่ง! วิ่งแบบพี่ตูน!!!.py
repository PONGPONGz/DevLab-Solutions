# https://www.borntodev.com/devlab/task/462?languageId=71
r,p=int(input()),input()
print(*[str(i+1)+'-'+p for i in range(r)], int(p)*r, sep='\n')