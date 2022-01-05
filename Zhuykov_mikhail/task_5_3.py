from sys import getsizeof

tutors = ['Иван', 'Анастасия', 'Пётр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Михаил', 'Григорий', 'Алексей']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

tut_klass = ((tutors[i], klasses[i]) if i < len(klasses) else (tutors[i], 'None') for i in range(len(tutors)))

print(type(tut_klass), 'Занимаемый объем памяти, байт:', getsizeof(tut_klass))
print(next(tut_klass))  # Получение первого значения генератора
print(next(tut_klass))  # Получение второго значения генератора
print(*tut_klass)  # Получение остальных значений генератора
print(next(tut_klass))  # Проверка, что генератор распакован полностью и появляется ошибка StopIteration
