# https://www.borntodev.com/devlab/task/661?languageId=71
r=[]
n=int(input())
for i in range(2, n + 1):
    for e in range(2, i+1):
        if i != e and i % e == 0:
            break
    else:
        r.append(i)
      
print(r)