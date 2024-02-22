# Операции с строками

s = 'Lorem \tIpsum is simply dummy text of the printing and typesetting industry.\nLorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book'

print(s)

# первый символ в строке
print(s[0])

# длина строки
print('len str: ', len(s))

# последний символ в строке
print('len str: ', s[len(s)-1])

# последний символ в строке
print(s[-1])

# срез из 10 символов
print(s[:10])

# срез из 10 символов начиная с 10ого заканчивая 20ым
print(s[10:20])

# срез из 10 симв начиная с 10 и взять каждый 2 символ
print(s[10:20:2])

# срез 3его символа в строке
print(s[::3])


# не сработает так как строка не изменяемый тип дпнных
# s[0] = 'asdasd'

# конкатенация строк
s1 = '11111'+'as das dasd'
print(s1)

# Заменить первый символ в строке s на строку s1
s = s1+s[1:]
print(s)

# создание строки из списка по разделителю " "(пробел)
l=['Lorem','Ipsum',"is",'simply','dummy','of']
s2=' '.join(l)
print(s2)

# разбить строку s по разделителю "."(точка)
l2=s.split('.')
print(l2)

# удаление пробелов с начала строки(lstrip) и конца(rstrip)
s3=' Hello, John! '
print(s3, 'len: ', len(s3))
s3=s3.lstrip()
print(s3, 'len: ', len(s3))
s3=s3.rstrip()
print(s3, 'len: ', len(s3))

# изменить регистр
s4='nam libero'
print(s4.upper())

s5='LOREM IPSUM'
print(s5.lower())

s6= 'lorem ipsum dolor sit amet, consectetur adipiscing elit'
print(s6)
s7 = s6[0].upper()
s6 = s7 + s6[1:]
print(s6)

