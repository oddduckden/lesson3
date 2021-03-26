# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
import re


def person_data(name, surname, birth_year, location, email, phone):
    """
    Вывод данных пользователя
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
    print(
        f'{name.capitalize():<20} {surname.capitalize():<20} {birth_year:<20} {location.capitalize():<20} {email:<20} {phone:<20}')


def format_check(param):
    """
    Проверка формата введенных строк.
    :param param:list (наименование параметра: str, значение параметра: str)
    :return: значение параметра: str
    """

    def reinput(old_list, message):
        """
        Повторный ввод параметра
        :param old_list: list (наименование параметра: str, значение параметра: str)
        :param message: str (сообщение об ошибке)
        :return:
        """
        print(message)
        old_list.pop(-1)
        old_list.append(input(f'Введите {old_list[0]}: '))
        return old_list

    if not param[1]:
        param = reinput(param, 'Поле не должно быть пустым.')
    elif param[0] in ('имя', 'фимилия', 'город проживания') and [s for s in param[1] if s in '0123456789']:
        param = reinput(param, 'Поле не должно содержать цифры.')
    elif param[0] == 'год рождения':
        if len(param[1]) != 4 or not param[1][:2] in ('19', '20') or not param[1].isdigit():
            param = reinput(param, 'Неверный формат года рождения.')
    elif param[0] == 'email' and not re.match(r"[^@]+@[^@]+\.[^@]+", param[1]):
        param = reinput(param, 'Неверный формат e-mail.')
    elif param[0] == 'телефон' and not re.match(r"(?:[0-9+()-])", param[1]):
        param = reinput(param, 'Неверный формат номера телефона.')
    return param[1]


parametrs = ('имя', 'фамилия', 'год рождения', 'город проживания', 'email', 'телефон')
person_data(*[format_check([p, input(f'Введите {p}: ')]) for p in parametrs])
