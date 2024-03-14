# Словари

person={
    'name': 'John',
    'age': 18,
    'last_name': 'Johnson',
    # 'address': 'Durand, Michigan(MI), 48429 Mount Street',
    'address': {
        'city': 'Durand',
        'state': 'Michigan(MI)',
        'zip': 48429,
        'street': 'Mount Street',
    },
    'phone': None,
}

print(
    'person:', person,
)
#
#

# Получение значений

print(
    'name: ', person.get('name'),
    'name: ', person['name'],
    # 'email: ', person['email']
    'email: ', person.get('email', None)
)
# result
#

# Получение только значений словаря
print(
   person.values()
)
#
#

# Получение ключей
print(
    person.keys()
)
#
#

# Получение: пар ключ-значение
print(
    person.items()
)
#

for k in person.items():
    print(k)


for k in person.values():
    print(k)


# добавление значения

person['birthday']='2005-06-14'
print(
    'person: ',person
)

person.setdefault('birthday', '2005-06-14')
print(
    'person: ',person
)