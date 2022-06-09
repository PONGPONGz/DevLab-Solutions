# https://www.borntodev.com/devlab/task/409?languageId=71
a,b=sorted(list(map(int, input().split()))),input()
print(*[a[sorted(b).index(i)]for i in b],sep=' ')
  
