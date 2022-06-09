# https://www.borntodev.com/devlab/task/657?languageId=71
l=list(map(int,input()[1:-1].split(',')))
print([sum(l[:i+1])for i in range(len(l))])