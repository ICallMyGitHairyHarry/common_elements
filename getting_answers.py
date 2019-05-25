# этот файл стоит читать в последнюю очередь

# импортируем списки и функцию из соответствующих файлов
from common_elements import common_elements
from test_common_elements import lists

# двумя циклами проходимся по lists и поочерёдно передаём его элементы функции common_elements
for i in range(len(lists)):
    for j in range(i + 1, len(lists)):
        answer = common_elements(lists[i], lists[j])
        print('Сет1 {}'.format(lists[i]))  # печетаем первый сет
        print('Сет2 {}'.format(lists[j]))  # печатаем второй сет
        print('Kол-во общих элементов {}'.format(answer))  # печаем кол-во общих элементов у этих сетов
        print()  # печатаем пустую строку
        #  осторожно, эта программа поочерёдно печатает все списки для наглядности, а в одном из них 2000 элементов
        #  p.s. set() в выводе - это пустой сет
