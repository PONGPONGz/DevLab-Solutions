# https://www.borntodev.com/devlab/task/554?languageId=71
price, cash = int(input()), int(input())
change = cash - price
cashes = {}
for i in range(6):
  n=input().split()
  if int(n[1]) > 0 and int(n[0]) <= change:
    cashes[n[0]] = int(n[1])
print('change: {}'.format(change))

for b, a in cashes.items():
  if int(a) > 0 and change >= int(b):
    amount = min(a, change//int(b))
    change = change - (int(b)*amount)
    print('cash: {} amount: {}'.format(b, amount))