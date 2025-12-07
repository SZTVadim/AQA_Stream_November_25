# Минимум и максимум

numbers = [3, 5, 77, 543, 67]
print(min(numbers))
print(max(numbers))

words = ["яблоко", "банан", "апельсин", "явлоко"]
print(min(words))
print(max(words))

# Копирование списков
original = [1, 2, 3, 4, 5]
copy1 = original.copy()
copy2 = original[::]

original.append(6)
print(f"Оригинальный список {original}")
print(f"Копия 1 {copy1}")
print(f"Копия 2 {copy2}")
print(f"ID списка оригинального {id(original)}")
print(f"ID списка копия 1 {id(copy1)}")
print(f"ID списка копия 2 {id(copy2)}")

# Сумма элементов списка
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(numbers))

mixed = [1, 2, "3", 4, "5"]
# print(sum(mixed))  # Ошибка сложения разных типов данных
sum_mixed = sum([x**2 for x in mixed if isinstance(x, int)])

print(sum_mixed)

# List Comprehensions
numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    squares.append(number**2)
    print(squares)
print(f"Result: {squares}")

squares_2 = [number**2 for number in numbers]
print(squares_2)

squares_3 = [x**2 for x in range(5)]
print(squares_3)

list_for_work = [x for x in range(10)]
print(list_for_work)

test_ids = [f"user_{i}" for i in range(10)]
print(test_ids)

words = ["hello", "world", "python"]
upper_case_words = [
    slovo.upper() for slovo in words if slovo == "python" or slovo == "hello"
]
print(upper_case_words)
words[1] = words[1].upper()
print(words)
