# https://www.borntodev.com/devlab/task/425?languageId=71
from string import punctuation

n=input()
while n[:n.find(':')] != 'GUITAR':
  n=input()

files = n[n.find('[')+1:n.find(']')].split(', ')
a = []
for file in files:
    for c in file:
        if c in punctuation:
            break
    else:
        a.append(file)

print(f"GUITAR:[{', '.join(a)}]")