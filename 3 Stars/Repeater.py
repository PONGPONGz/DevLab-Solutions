# https://www.borntodev.com/devlab/task/220?languageId=71
text = input()
length = len(text)
for i in range(length):
 #chars= text[1:][::-1][length-i-1:] + text[0] + text[1:][:i]
  chars = text[:i+1][::-1] +text[1:i+1]
  print((' '*((length*2)-len(chars)-1) + ' '.join(chars)))
  
