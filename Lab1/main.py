import sys

print("Hello, World!")

# Запитуємо ім'я користувача
name = input("Введіть ваше ім'я: ")

# Виводимо привітання
print(f"Привіт, {name}!")

# Створюємо приклади базових типів
int_value = 0
float_value = 0.0
str_value = ""
list_value = []
tuple_value = ()
dict_value = {}
bool_value = True

# Виводимо розміри
print(f"Розмір int: {sys.getsizeof(int_value)} байт")
print(f"Розмір float: {sys.getsizeof(float_value)} байт")
print(f"Розмір str (порожній): {sys.getsizeof(str_value)} байт")
print(f"Розмір list (порожній): {sys.getsizeof(list_value)} байт")
print(f"Розмір tuple (порожній): {sys.getsizeof(tuple_value)} байт")
print(f"Розмір dict (порожній): {sys.getsizeof(dict_value)} байт")
print(f"Розмір bool: {sys.getsizeof(bool_value)} байт")
