# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def division_func():
    '''
    Функция деления двух введенных чисел первое на второе
    :return: None
    '''
    while True:
        try:
            num = input('Введите два числа через запятую: ').replace(' ', '').split(',')
            print(f'Результат деления первого на второе: {float(num[0]) / float(num[1])}')
        except ZeroDivisionError:
            print('Извините, деление на ноль недопустимо')
        except ValueError:
            print('Нужно было вводить числа')
        except IndexError:
            print('Нужно было ввести два числа')
        else:
            if input('Повторим?(Y/N): ') == 'N':
                break
        finally:
            print('\n')
    return


division_func()
