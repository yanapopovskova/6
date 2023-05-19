"""" Сгенерировать все возможные одномерные массивы из чисел 0, 1, 2 и 3"""
n = 4
K = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                K.append([i, j, k, l])

min_sum = float('inf')
min_combination = None

for combination in K:
    # Проверяем ограничения на четность и нечетность элементов
    if all(x % 2 == 1 for x in combination[::2]) and all(x % 2 == 0 for x in combination[1::2]):
        # Вычисляем значение
        sum_mod = sum(abs(x) for x in combination) % 6
        # Обновляем минимальное значение и комбинацию переменных
        if sum_mod < min_sum:
            min_sum = sum_mod
            min_combination = combination

print("Количество допустимых комбинаций:", sum_mod)
print("Минимальное значение:", min_sum)
print("Набор переменных, при котором достигается минимум:", min_combination)
