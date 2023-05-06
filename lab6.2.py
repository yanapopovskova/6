"""" Сгенерировать все возможные одномерные массивы из чисел 0, 1, 2 и 3, где сумма элементов массива должна быть кратна 3.
Целевая функция будет максимизировать количество уникальных комбинаций элементов массива."""

import itertools

elements = [0, 1, 2, 3]
k = 4        # длина массива
count = 0    # количество уникальных комбинаций
result = []  # список всех комбинаций

for combination in itertools.product(elements, repeat=k):
    if sum(combination) % 3 == 0:
        if combination not in result:
            result.append(combination)
            count += 1

print("Количество уникальных комбинаций:", count)
print("Все комбинации:")
for combination in result:
    print(combination)