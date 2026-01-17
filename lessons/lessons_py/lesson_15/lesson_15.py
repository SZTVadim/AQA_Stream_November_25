# loop

number = 1
while number < 5:
    print(f"number: {number}")
    number += 1

print("End")
i = 0
while True:
    print(i)
    i += 1
    if i == 500:
        break
print("End")
for d in range(11):
    print(d)

words = "Hello World"
for word in words:
    print(word)

for d in range(5, 11):
    print(d)

for d in range(2, 12, 4):
    print(d)

message = "Hello "
for letter in message:
    print(letter)
else:
    print(f'Последний символ: "{letter}". Цикл завершен')

print("работа программы выполнена")


def any_func(x):
    return x ** 2


my_square_ = any_func(2)
print(my_square_)

my_square_2 = lambda x: x ** 2
print(my_square_2(5))

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)
