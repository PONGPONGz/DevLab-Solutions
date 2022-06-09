# https://www.borntodev.com/devlab/task/549?languageId=71
n,k=map(int,input().split())
pancakes = n//k
coupons, plates = pancakes, pancakes
while coupons >= 2 or plates >= 4:
  ac,ap=coupons // 2,plates // 4
  pancakes += ac+ap
  coupons %= 2
  plates %= 4
  coupons+=ac+ap
  plates+=ap+ac

print(pancakes)

