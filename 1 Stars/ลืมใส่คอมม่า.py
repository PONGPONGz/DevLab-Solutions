# https://www.borntodev.com/devlab/task/625?languageId=71
n=input()
print(','.join(n[::-1][i:i+3]for i in range(0, len(n), 3))[::-1])