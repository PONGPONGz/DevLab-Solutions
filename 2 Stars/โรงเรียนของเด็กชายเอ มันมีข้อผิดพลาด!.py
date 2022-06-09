# https://www.borntodev.com/devlab/task/19?languageId=71
n=int(input())
if n < 0:
  print('Error : Value must be greater than or equal to 0.')
elif n > 100:
  print('Error : Value must be less than or equal to 100.')
else:
  if n > 80:
  		print('A')
  elif n > 60 and n < 80:
    	print('B')
  elif n > 40 and n < 60:
    	print('C')
  else:
			print('F')