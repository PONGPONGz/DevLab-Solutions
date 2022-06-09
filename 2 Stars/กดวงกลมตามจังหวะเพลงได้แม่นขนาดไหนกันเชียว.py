# https://www.borntodev.com/devlab/task/597?languageId=71
a, b, c, d = [int(input())for _ in range(4)]
print(f'{(((50 * c) + (100 * b) + (300 * a)) / (300 * (a + b + c + d)))*100:.02f}%')