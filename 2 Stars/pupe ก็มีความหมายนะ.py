# https://www.borntodev.com/devlab/task/420?languageId=71
n=''.join(input().replace('pu', '0').replace('pe', '1'))
print(''.join(chr(int(n[i-8:i],2))for i in range(8,len(n)+1,8)))


