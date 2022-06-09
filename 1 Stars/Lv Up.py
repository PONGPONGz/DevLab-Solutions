# https://www.borntodev.com/devlab/task/483?languageId=71
import re
xp=int(re.findall(r'\d+', input())[0])
l=1
while True:
  if xp // (100*l) > 0:
    xp -= (100*l)
    l += 1
  else:
    break
print(f"Lv : {l}\nExp : {xp}/{100*l}\nATK : {l*10}\nHP : {l*100}")