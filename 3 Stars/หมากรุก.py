# https://www.borntodev.com/devlab/task/217?languageId=71
chess = ''
for i in range(8):
  	chess += input().replace('.','')
scores = {
    'p': 1,
    'n': 3,
    'b': 3,
    'r': 5,
    'q': 9,
    'k': 0
}

a,b=0,0

for i in chess:
    if i.islower():
      	b += scores[i.lower()]
    else:
      	a += scores[i.lower()]
        
print('equal' if a-b == 0 else a-b)