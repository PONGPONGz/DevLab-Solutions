# https://www.borntodev.com/devlab/task/469?languageId=71
l,a=[int(input())for _ in range(int(input()))],0
for i in l:
  if i>1000000:a+=i*.25
  elif i>500000:a+=i*.2
  elif i>300000:a+=i*.15
  elif i>100000:a+=i*.1
print(f"เสียภาษีทั้งหมด {int(a)} กะลา"if a>0 else"ไม่ต้องเสียภาษี")