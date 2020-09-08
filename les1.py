# PEP 8


# snake_case = 1
# CamelCase = 2
# camelCase = 3

# kebab-case = 2


some_str = "Hello my friends"  # str()
some_str2 = 'Hello my friends'

some_int = 1  # int()
some_float = 2.333334322  # float
some_bool = True  # bool()

ask_name = "введите имя\n"
ask_age = "введите возраст\n"
#
# name = input(ask_name)
#
# print("Привет", name, end='!!!!!', sep='----')

# age = input(ask_age)
#
# if age.isdigit():
#     age = int(age)
#     if age >= 18:
#         print('Доступ к разделам ХХХ открыт')
#     elif age > 16:
#         print("доступ к боевикам")
#     else:
#         print("Смотри мультики")
# else:
#     print('Введено не число')
#     print('Повторите ввод')
#
# print('HELLO')
# print('WORLD')

a = 12534614230

temp = a
while (tmp := temp % 10) or temp:
    temp //= 10
    # if tmp == 5:
    #     break
    # a = a // 10
    print(tmp, temp)
else:
    print('ELSE')
