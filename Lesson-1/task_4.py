"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

some_words = ('разработка', 'администрирование', 'protocol', 'standard')

bytes_list = []
for i in some_words:
    UNC_WORD = i.encode("utf-8")
    bytes_list.append(UNC_WORD)
print(bytes_list)
print('----------')
string_list = []
for i in bytes_list:
    STR_LST = i.decode('utf-8')
    string_list.append(STR_LST)
print(string_list)
