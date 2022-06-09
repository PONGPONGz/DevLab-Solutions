# https://www.borntodev.com/devlab/task/352?languageId=71
hours, minutes, seconds = 0, 0, int(input())
minutes = seconds // 60
seconds = seconds % 60
hours = minutes // 60
minutes = minutes % 60
print(f"{hours}:{minutes or '00'}:{seconds or '00'}")