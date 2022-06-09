# https://www.borntodev.com/devlab/task/486?languageId=71
s='เรียนคณิตศาสตร์online,เรียนอังกฤษonline,เรียนไทยonline,เรียนวิทย์online,อ่านเตรียมสอบ o-net,ทำงานบ้าน,เรียนวาดรูป,เรียนร้องเพลง'.split(',')
n=input().split(',')
a=[i for i in s if i not in n]
print('ยังเหลือสิ่งที่ต้องทำอีก {} อย่าง'.format(len(a)))
for i in a:
  print('- {}'.format(i))