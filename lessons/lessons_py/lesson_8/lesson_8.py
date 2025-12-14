# Комбинирование операций
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x ** 2 for x in numbers if x % 3 == 0]
print(even_squares)

# Синтаксис if - else
numbers = [-2, -1, 0, 1, 2, 3, 4, 1]
positive = [x if x > 0 else f"{x}: не положительное число" for x in numbers]
positive_1 = [x for x in numbers if x > 0]
# print(positive)
# print(positive_1)

positive_2 = [x if x < 0 else "pass" if x == 1 else f"{x}: это не равно единице" if x == 2 else "дичь" for x in numbers]
print(positive_2)
