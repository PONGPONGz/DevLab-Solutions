# https://www.borntodev.com/devlab/task/463?languageId=71
t=0
n=int(input())
for i in range(12):
  print(f"{n} x {i+1} = {n*(i+1)}")
  t+=n*(i+1)
print(f"รวม : {t if t < 1000 else str(t)[0]+','+str(t)[1:]}.00")