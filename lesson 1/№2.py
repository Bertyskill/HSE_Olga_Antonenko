"""Реализуйте структуру данных «Участники спора». Она должна представлять собой
список (list) словарей (dict).
Каждый словарь хранит информацию об отдельном участнике. Словарь содержит
пары «ключ-значение» параметрами, то есть характеристиками участника:
наименование, статус, ИНН.
Заполнение данных должно быть произведено пользователем через консоль для трёх
различных участников.
Выведите полученные данные в консоль.
"""

def make_dictionary():
    print("Введите имя участника спора")
    name = input()
    print("Введите статус участника спора")
    status = input()
    print("Введите ИНН участника спора")
    inn = input()
    dictionary = dict()
    dictionary['name'] = name
    dictionary['status'] = status
    dictionary['inn'] = inn
    return dictionary


result = list()
result.append(make_dictionary())
result.append(make_dictionary())
result.append(make_dictionary())
print(result)