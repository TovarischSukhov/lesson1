mylist = ['Вася', 'Маша', 'Петя', 'Саша']
add_name = str(input('Введите имя: '))
mylist.append(add_name)
print(mylist)
print('В списке всего', len(mylist), 'элементов.')
print(type(mylist))
mylist.count('Саша')
print(mylist)
