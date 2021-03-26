# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.
def my_func(var1, var2, var3):
    lst = [var1, var2, var3]
    lst.remove(min(lst))
    return sum(lst)

print('sum =', my_func(*[int(x) for x in input('Введите три числа через запятую: ').split(', ')]))