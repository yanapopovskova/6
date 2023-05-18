"""" Сгенерировать все возможные одномерные массивы из чисел 0, 1, 2 и 3"""
n = 4
K = []
for i in range(1, 2*n+1):
    if i % 2 == 0:
        # четные позиции
        for j in range(1, n+1, 2):
            K.append(j)
        for j in range(2, n+1, 2):
            K.append(j)
    else:
        # нечетные позиции
        for j in range(2, n+1, 2):
            K.append(j)
        for j in range(1, n+1, 2):
            K.append(j)

# Все возможные варианты массива K из чисел 0, 1, 2 и 3
combinations = []
for i in range(4**n):
    combo = []
    for j in range(n):
        digit = (i // (4**j)) % 4
        combo.append(digit)
    combinations.append(combo)

# Проверка все комбинации суммы и выбрать, которые равны 5 по модулю
valid_combinations = []
for combo in combinations:
    if all((combo[i] % 2) != (i % 2) for i in range(n)):
        if abs(sum(combo)) == 6:
            valid_combinations.append(combo)

print("Количество допустимых комбинаций:", len(valid_combinations))
print("Все допустимые комбинации:")
for combination in valid_combinations:
    print(combination)