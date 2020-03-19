#В том же проекте создать модуль test_filemanager.py для тестирования функций консольного файлового менеджера
# В файле написать тесты для каждой ""чистой"" функции, чем больше тем лучше. Это могут быть функции консольного файлового менеджера, а так же программы мой счет и программы викторина
#Если в проекте нет функций либо не получается написать ни одного теста, можно использовать мою урезанную версию данного проекта по ссылке: https://yadi.sk/d/n6gyaovRG2
# материалы к занятию:
import os
import sys
import filemanager

from filemanager import author_info
author_programm = author_info()
if author_programm ('Elena') != 'Elena':
    print ("Error author_info")

def create_dir():
    if os.path.exist(answer) is True:
        print("Копирование файла- ок")
    else:
        print ('Error ceate directory')

def copy_file ():
    if os.path.exist (destination) is True:
        print ("Копирование файла- ок")
    else:
        print ('Error copy file')
