my_dict = {'Nikita': 16, 1: 'Один', (1, 2): [6, 7, 8]}
print(f'Dictionary: {my_dict}')
print(f'Value: {my_dict['Nikita']}') #Выводим значение по ключу
print(f'No exiting value: {my_dict.get((3, 8))}') #Пытаемся вывести элемент по ключу, которого нет
my_dict.update({'Okorochok': 1.98, (1, 'sobaka'): 'planeta'}) # Добавляем в словарь данные
(my_dict)
print(f'Deleted value: {my_dict.pop('Okorochok')}') #Убираем из словаря значение по ключу
print(f'Modified dictionary: {my_dict}')

my_set = {1, 1, 3, 2, 3, (1, 2, 3), (3, 1, 2), (1, 2, 3), 'Repka', False}
print(f'Set: {my_set}')
my_set.add('Kpl') #Добавляем элемент. Добавлять можно только по одному?
my_set.add(87)
print(my_set)
my_set.remove(3) #Удаляем элемент. Удалять тоже по одному?
print(f'Modified set: {my_set}')

#my_dict = {'Nikita': 16, 1: 'Один', (1, 2): [6, 7, 8]}
#print(f'Словарь: {my_dict.keys()}') # Показываем только ключи
#key = input('Введите ключ:') # Вводим ключ. Он всегда строка. Напрямую получится только с ключами строками.
#print(my_dict.get(key)) #Выводим значение по ключу. Что делать если input это строка а ключ число или кортеж? Откуда узнать какой тип данных искать?
#Сначала надо привести все ключи к str?
#print(my_dict)
#print(my_dict.pop(key)) #Убираем из словаря значение по ключу
#print(my_dict)


