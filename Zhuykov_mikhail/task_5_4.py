from random import randint


def choice_el(lst):
    return [lst[i] for i in range(len(lst)) if lst[i] > lst[i - 1] and i != 0]


print('________________Список из задания_______________')
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print('Исходный список:', src)
print('Результат:', choice_el(src))

print('_____________Сгенерированный список_____________')
random_src = [randint(1, 100) for i in range(randint(10, 30))]
print('Исходный список:', random_src)
print('Результат:', choice_el(random_src))
