s = 'This is a string %s' % 'string value goes here'
print(s)
print('Hi, my name is %s' % 'Sam')

print('%s=%s' % ('spam', 42))
print('%s, %s and %s' % (3.14, 42, [1, 2]))

Morze_In = input('Введите  сообщение в виде последовательности точек и тире: ')
Text_Out = ''
for index in range(0, len(Morze_In), 4):
    Text_Out = Text_Out + Alphabet[Morze_In[index:index+4]]
print(Text_Out)