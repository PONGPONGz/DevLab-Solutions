# https://www.borntodev.com/devlab/task/226?languageId=71
goods = [int(input())for _ in range(int(input()))]
t=int(input())
print(f"Position: {','.join(str(i+1) for i,v in enumerate(goods) if v == t)}")