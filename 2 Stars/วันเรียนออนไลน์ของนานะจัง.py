# https://www.borntodev.com/devlab/task/654?languageId=71
t='study math online,learn English online,learn Thai online,study science online,read test preparation o-net,do housework,learn to draw,learn to sing'.split(',')
for i in input().split(','):
	t.remove(i)
print('There is still {} things to do.\n- {}'.format(len(t), '\n- '.join(t)))