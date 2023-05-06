""""Вариант 12. Сгенерировать все возможные варианты одномерного массива (К) из чисел 0, 1, 2 и 3."""

import itertools

K = [0, 1, 2, 3]
all_combinations = list(itertools.product(K, repeat=len(K)))

print(all_combinations)
