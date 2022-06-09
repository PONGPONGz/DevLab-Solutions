# https://www.borntodev.com/devlab/task/450?languageId=71
n=input()
print(''.join(chr(ord(n[i])-i-1)for i in range(len(n))).swapcase())