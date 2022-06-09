# https://www.borntodev.com/devlab/task/446?languageId=71
d=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
print(d[(d.index(input())+int(input()))%7])