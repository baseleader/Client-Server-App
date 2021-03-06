"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""

some_words = ('attribute', 'класс', 'функция', 'type')

for i in some_words:
    try:
        print('----------')
        print(bytes(i, 'ascii'))
        print('Слово записано в bytes')
        print('----------')
    except UnicodeEncodeError:
        print(f'Слово {i} невозможно записать в байтовый тип с маркировкой b''')
