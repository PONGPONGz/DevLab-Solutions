# https://www.borntodev.com/devlab/task/342?languageId=71
n=[len(set(x.strip().split()))for x in ''.join(i for i in input()if not i in'ABC')[2:].split(' : ')]
print('ABC'[n.index(max(n))])