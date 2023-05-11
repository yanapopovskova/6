""""Вариант 12. Сгенерировать все возможные варианты одномерного массива (К) из чисел 0, 1, 2 и 3."""

n = 4
K = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                    K.append([i, j, k, l])

print("Количество комбинаций:", len(K))
print("Все комбинации:")
for combination in K:
    print(combination)