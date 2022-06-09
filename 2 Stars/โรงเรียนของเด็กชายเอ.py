# https://www.borntodev.com/devlab/task/18?languageId=71
n=int(input())
if n >= 90:
    print('A')
elif n >=85 and n < 90:
    print('B+')
elif n > 80 and n < 85:
	print('B')
elif n >= 75 and n < 80:
    print('C+')
elif n >= 70 and n < 75:
    print('C')
elif n >= 65 and n < 70:
    print('D+')
elif n >= 60 and n < 65:
    print('D')
else:
    print('F')