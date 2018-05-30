import chardet

# Пошаговое описание задачи
# 1. Прочитать данные из файла и сохранить в переменную all_words_in_text
# 2. Из all_words_in_text создать список long_words из слов длиннее 6 символов
# 3. Узнать сколько раз каждое слово встречается в тексте
# 3.1 Создать множетство не повторяющихся слов из списка long_words
# 3.2 Циклом пробегая по каждому сложу в множетсве считать кол-во вхождения в список long_words
# 3.3 Сохранять результаты в списке word_value_list в виде списков ['words', value], где 'words' - слово, а value - число вхождений
# 4. Сделать сортировку этого списка по первому индексу с помощью sorted(long_words, key=quantity), где quantity = отедльная функция
# 5. Вывести первые 10 частовстречающиъся отсротированных слов без указания их кол-ва



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

def read_file(file_name, world_length):  # Добавить определение кодировки, возможно вынести ее в отдельную функцию!
    """Функция read_file открывает файл, декодирует е
    го и возвращает список результат работы функции
    get_long_words_list.
    """

    with open('{0}'.format(file_name), 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        print(result)
        print('encoding', result['encoding'])
        # all_words_in_text = data.split()  # Получили список всех слов, разбитых по пробеллом.
        # return get_long_words_list(all_words_in_text, world_length)  # Получили список элементов длинне 6 символов

read_file('newsafr.txt', 6)  # Отладочный принт

def run_func(file_lst):
    print('Запущена программа получения 10 самых высокочастотных слов.')
    world_length = int(input('Укажите минимальную длину слова: '))
    for file in file_lst:
        print('Сейчас будем работать с файлом: {0}'.format(file))
        long_words_list = read_file(file, world_length)  #  Присвоили переменной long_words_list массив слов длиннее world_length
        print(long_words_list)



# run_func(['newsafr.txt', 'newscy.txt', 'newsfr.txt', 'newsit.txt'])
# run_func(['newsafr.txt'])