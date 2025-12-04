age_str = "25"

print(type(age_str))
print(int(age_str))
print(type(int(age_str)))

age_str = "25.5"
print(float(age_str))
print(type(float(age_str)))

any_text = 'Abrakadabra'
print(any_text[0])
print(any_text[-1])
print(any_text[-2])

text = "Python"
reversed_text = text[::-1]
print(reversed_text)

any = "He said \nHello"
print(any)
#
# class Work:
#     """"Классы мы с Вами узнаем в будущем
#     А пока этот пример только для того,
#     чтобы посмотреть как работают тройные кавычки"""
#     pass
#
my_list = [1, {2: 3}, [4, 5], "6", 7.7, "8", 9, "10", True]
print(id(my_list))
my_list.append(4)
print(my_list)
print(id(my_list))
list_fruit = ["apple", "banana", "cherry"]
my_list.extend(list_fruit)
my_list.insert(3, 'potato')

print(my_list)

my_list = [1, 2, 3]
list_fruit = ["apple", "banana", "cherry"]
my_list.extend(list_fruit)
print(my_list)

my_list.remove("apple")
print(my_list)

# print(my_list.pop(-2))
element = my_list.pop(-2)
print(element)
print(my_list)
my_list.append('cherry')
print(my_list)

print(my_list.index(3))
print(my_list.count(3))
print(my_list)
my_list.reverse()
new_list = list(reversed(my_list))
print(new_list)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.sort(reverse=True)
print(numbers)
