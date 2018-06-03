import chardet

# Пошаговое описание задачи
# 1. Прочитать данные из файла и сохранить в переменную all_words_in_text
# 2. Из all_words_in_text создать список long_words из слов длиннее 6 символов
# 3. Узнать сколько раз каждое слово встречается в тексте
# 3.1 Создать множетство не повторяющихся слов из списка long_words
# 3.2 Циклом пробегая по каждому сложу в множетсве считать кол-во вхождения в список long_words
# 3.3 Сохранять результаты в списке word_value_list в виде списков ['words', value],
#     где 'words' - слово, а value - число вхождений
# 4. Сделать сортировку этого списка по первому индексу с помощью sorted(long_words, key=quantity),
#    где quantity = отедльная функция
# 5. Вывести первые 10 частовстречающиъся отсротированных слов без указания их кол-ва

def get_count_of_words(some_set, lst):
    """Функция получает на вход список и подсчитывает какое кол-во
    раз каждый элемент встречается в списке.
    Для этого создается множество не повторяющихся элементов списка.
    Возвращается новый список вида [['word1', quantity], ['word2', quantity]].
    """
    word_quantity_list = []
    for word in some_set:
        word_quantity_list.append([word, lst.count(word)])
    return word_quantity_list


def get_long_words_list(lst, x):
    """Функция принимает итеррируемых объект lst и целое число x.
    Возвращает новый список long_words состоящий из элементов переданного
    итеррируемого объекта lst, отвечающего условию len(элемент) > x.
    """

    long_words = []
    for word in lst:
        if len(word) > x:
            long_words.append(word)
    return long_words


def read_file(file_name, world_length):
    """Функция read_file открывает файл, декодирует е
    го и возвращает список результат работы функции
    get_long_words_list.
    """

    with open('{0}'.format(file_name), 'rb') as f:   # Определяем кодировку
        data = f.read()
        result = chardet.detect(data)
        print('Используемая кодировка:', result['encoding'])

    with open('{0}'.format(file_name), 'r', encoding=result['encoding']) as f:    # Определяем кодировку
        new_data = f.read()
        all_words_in_text = new_data.split()  # Получили список всех слов, разбитых по пробеллом.
        long_word_list = get_long_words_list(all_words_in_text, world_length)  # Получили список слов, длиннее world_length

    return long_word_list


def quantity(lst):
    """Данная функция принимает список вида ['word1', quantity],
    состоящий их 2-х элементов и возвращает второй элемент,
    т.е. quantity.
    """
    return lst[1]


def run_func(file_lst):
    print('Определим 10 самых высокочастотных слов.')
    world_length = int(input('Укажите количество символов в слове: '))
    for file in file_lst:
        print('Обработка файла: {0}'.format(file))
        long_words_list = read_file(file, world_length)  #  Присвоили переменной long_words_list массив слов длиннее world_length
        set_words = set(long_words_list)  # Получили множество слов из файла
        word_quantity_list = get_count_of_words(set_words, long_words_list)
        sorted_list = sorted(word_quantity_list, key=quantity, reverse=True)
        res_list = [i[0] for i in sorted_list[:10]]  # Список из 10 самых высокочастотных слов в файле
        print('10 самых высокочастотных слов длиннее {0} символов:\n'.format(world_length), res_list)
        print('===============\n')

run_func(['newsafr.txt', 'newscy.txt', 'newsfr.txt', 'newsit.txt'])