from random import randint
from sys import getsizeof
from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]  # Список из задания.
print(src)

print('\n______Решение в лоб, через count______')


def src_selection_1(lst_num_val):
    lst_num = []
    for i in lst_num_val:
        if lst_num_val.count(i) == 1:
            lst_num.append(i)
    print(getsizeof(lst_num), '- Это методом count. Объем памяти result_1 в функции')
    return lst_num


start = perf_counter()
result_1 = src_selection_1(src)
print(result_1)
print('Время выполнения:', perf_counter() - start, 'Объем занимаемой памяти полученного списка:', getsizeof(result_1))

print('\n______Решение в одну строку через count______')


def src_selection_2(lst_num_val):
    return (i for i in lst_num_val if lst_num_val.count(i) == 1)


start = perf_counter()
result_2 = [*src_selection_2(src)]
print(result_2)
print('Время выполнения:', perf_counter() - start, 'Объем занимаемой памяти полученного списка:', getsizeof(result_2))

print('\n______Решение через словарь______')


def src_selection_3(lst_num_val):
    unique_dict = dict()
    tmp_dict = dict()
    for el in lst_num_val:
        if el not in tmp_dict:
            tmp_dict[el] = el
            unique_dict[el] = el
            continue
        if el in unique_dict:
            del unique_dict[el]
    print(getsizeof(unique_dict), '- Это словарь. Объем памяти unique_dict в функции')
    print(getsizeof(tmp_dict), '- Это словарь. Объем памяти tmp_dict в функции')
    return (key for key in unique_dict)


start = perf_counter()
result_3 = src_selection_3(src)
print('Время выполнения:', perf_counter() - start, 'Объем занимаемой памяти полученного списка:', getsizeof(result_3))
result_3_unpacked = [*result_3]
print('Объем занимаемой памяти распакованного списка:', getsizeof(result_3_unpacked))
print(result_3_unpacked)

print('\n______Решение через множества______')


def src_selection_4(lst_num_val):
    unique_set = set()
    tmp_set = set()
    for el in lst_num_val:
        if el not in tmp_set:
            tmp_set.add(el)
            unique_set.add(el)
            continue
        if el in unique_set:
            unique_set.discard(el)
    print(getsizeof(unique_set), '- Это множество. Объем памяти unique_set в функции')
    print(getsizeof(tmp_set), '- Это множество. Объем памяти tmp_set в функции')
    return (elem for elem in lst_num_val if elem in unique_set)


start = perf_counter()
result_4 = src_selection_4(src)
print('Время выполнения:', perf_counter() - start, 'Объем занимаемой памяти полученного списка:', getsizeof(result_4))
result_4_unpacked = [*result_4]
print('Объем занимаемой памяти распакованного списка:', getsizeof(result_4_unpacked))
print(result_4_unpacked)
