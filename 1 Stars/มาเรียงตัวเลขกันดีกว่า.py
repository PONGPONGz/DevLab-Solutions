# https://www.borntodev.com/devlab/task/452?languageId=71
n=input()
s=[]
for i in range(int(n[n.find(':')+2:])):
  s.append(int(input()))
  print(f"ROW {i+1} : {sorted(s)}")