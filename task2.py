# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
import re


def person_data(name, surname, birth_year, location, email, phone) -> None:
    """
    Функция выводит данные пользователя
    :param name: имя
    :param surname: фамилия
    :param birth_year: год рождения
    :param location: город проживания
    :param email: e-mail
    :param phone: телефон
    :return: пропущенный параметр
    """

    print('{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format('Имя', 'Фамилия', 'Год рождения', 'Город проживания',
                                                             'E-mail', 'Телефон'))
    print(f'{name:<20} {surname:<20} {birth_year:<20} {location:<20} {email:<20} {phone:<20}')


def format_check(param):
    """
    Функция проверяет формат введенных строк года рождения, e-mail и номера телефона
    :param param:tuple (наименование параметра: str, значение параметра: str)
    :return: значение параметра: str
    """
    if not param[1]:
        print('тут')
        return
    elif param[0] in ('имя', 'фимилия', 'город проживания') and [s for s in param[1] if s in '0123456789']:
        print('azaza')
    elif param[0] == 'год рождения':
        if len(param[1]) != 4 or not param[1][:2] in ('19', '20') or not param[1].isdigit():
            print('здесь')
    elif param[0] == 'email' and not re.match(r"[^@]+@[^@]+\.[^@]+", param[1]):
        print('wrong')
    elif param[0] == 'телефон' and not re.match(r"(?:[0-9+()-])", param[1]):
        print('ups')
    print(param)
    return param[1]


parametrs = ('имя', 'фамилия', 'год рождения', 'город проживания', 'email', 'телефон')
person_data(*[format_check((p, input(f'Введите {p}: '))) for p in parametrs])
