# https://www.borntodev.com/devlab/task/466?languageId=71
p=[
  {'underwear':20,'pants':30,'skirt':30,'shirt':40,'blouse':40},
  {'size S':5,'size M':10,'size L':15,'size XL':20,'size XXL':25},
  {'color red':15,'color blue':15,'color white':10,'color green':15,'color black':15},
  {'cotton': 20,'nylon':15,'spandex':25,'wool':30,'linen':25}
]
c=['R','B','W','G','BK']
s=0
for i in range(4):
  n=input()
  n=int(n)-1if n not in c else c.index(n)
  key = list(p[i])[n]
  print('{} - {}'.format(key, p[i][key]))
  s+=p[i][key]
a=int(input())
print('amount - {}\ncost - {}*{} = {}'.format(a, s, a, s*a))