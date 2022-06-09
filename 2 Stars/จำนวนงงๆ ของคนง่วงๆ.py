# https://www.borntodev.com/devlab/task/337?languageId=71
l=[1]
p1,p2,p3=0,0,0
for _ in range(int(input())):
  b3 = l[p1] * 3
  b11= l[p2] * 11
  b19=l[p3]*19
  
  m = min(b3,b11,b19)
  if m==b3:p1+=1
  if m==b11:p2+=1
  if m==b19:p3+=1
  l.append(m)
print(l[-2])