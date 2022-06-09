# https://www.borntodev.com/devlab/task/543?languageId=71
print(*sorted([input() for _ in range(int(input()))], key=lambda x: len(x)), sep='\n')