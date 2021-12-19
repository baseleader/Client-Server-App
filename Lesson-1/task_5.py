"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

args1 = ['ping', 'yandex.ru']
args2 = ['ping', 'youtube.com']
subproc_ping1 = subprocess.Popen(args1, stdout=subprocess.PIPE)
subproc_ping2 = subprocess.Popen(args2, stdout=subprocess.PIPE)

for line in subproc_ping1.stdout:
    result = chardet.detect(line)
    print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'), end='')
    print('*' * 100)

print('/' * 100)

for line in subproc_ping2.stdout:
    result = chardet.detect(line)
    print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'), end='')
    print('*' * 100)
