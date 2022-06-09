# https://www.borntodev.com/devlab/task/345?languageId=71
n=input()
print(''.join([v.upper()if i%2!=0 else v for i,v in enumerate(n)]))