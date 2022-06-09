# https://www.borntodev.com/devlab/task/343?languageId=71
b1, b2, b3 = map(lambda x: x[x.find('[')+1:-1].split(','), input().split())
print(*[i for i in b1 if i in b2 and not i in b3] or ['none'], sep=',')