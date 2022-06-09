# https://www.borntodev.com/devlab/task/350?languageId=71
x,y=map(int,input()[1:-1].split(','))
n=int(input())
if x>=n or y>=n:print('That position is not loaded.')
else:
  grids=['#'*n]*n
  t=grids[n-y-1]
  grids[n-y-1]=t[:x]+'*'+t[x+1:]
  print('\n'.join(grids))