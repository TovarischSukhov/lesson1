price = 100
vat_rate = 18

vat = price / 100 * vat_rate

print(vat)

price_no_vat = price - vat
print(price_no_vat, '\n')

#Создаем функцию
def get_vat(price, vat_rate):
    vat = price / 100 * vat_rate
    price_no_vat = price - vat
    print(price_no_vat)

price1 = 100
vat_rate1 = 18
get_vat(price1, vat_rate1)

print('_' * 20, '\n')

price2 = 500
vat_rate2 = 10
get_vat(price2, vat_rate2)

print('_' * 20, '\n')
get_vat(50, 5)
get_vat(-100, 18)

print('\n')

# Задание 1
"""
Измените функцию get_summ() чтобы результат
выводился заглавными буквами использйте метод 'строка'.upper()
Вызовите функцию, пердав в нее два аргумента "Learn" и "python"
Сохраните результат вызова функции в переменную sum_string
Выведите на экран значение переменной
Исходная функция выглядит так

def get_summ(one, two, delimiter='&'):
    return str(one) + str(delimiter) + str(two)

"""
def get_summ(one, two, delimiter=' & '):
    list = str(one) + str(delimiter) + str(two)
    list = list.upper()
    return list

text1 = 'Learn'
text2 = 'python'
sum_string = get_summ(text1,text2)
print(sum_string)
