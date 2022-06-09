# https://www.borntodev.com/devlab/task/538?languageId=71
from re import findall
print(f"{int(findall('[0-9]+', input())[0])*4} Baht")