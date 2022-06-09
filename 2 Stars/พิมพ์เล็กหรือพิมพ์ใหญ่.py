# https://www.borntodev.com/devlab/task/354?languageId=71
n=input()
l=len(n)
u=len(list(filter(lambda x: x.isupper(), n)))
print(f"UPPER:{u}\nLOWER:{l-u}")