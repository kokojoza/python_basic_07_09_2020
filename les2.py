var_str = "Это строка"  # str неизменяемый тип коллекция итерируемый
var_int = 22  # int неизменяемый тип
var_float = 2.33  # float неизменяемое число
var_list = [1, 2, 3, 4, 5, [1, 2, 3], True, False, 'HELLO']  # list изменяемый коллекция итерируемая
var_tuple = (1, 2, 3, [1, 2, 3], True, False, 'HELLO')  # кортеж tuple неизменяемая коллекция

var_set = {1, 2, 3, 4, 5, 1, 2, 3, (1, 2, 3)}  # set множество изменяемый не индексируемый итерируемый

var_dict = {'key': 'HELLO', 1: 22, (1, 2): 33}  # dict словарь изменяем итерируемый

# i = 0
# while i < len(var_str):
#     char = var_str[i]
#     print(char)
#     i += 1

# for idx, char in enumerate(var_str, 10):
#     print(idx, char)
temp = {}
for idx, num in enumerate(range(9, -10, -1), 77):
    temp[idx] = num

print(temp)

user_template = {
    'age': 'Введите возраст',
    'name': 'Ввудите имя',
    'surname': 'Введите фамилию',
    'phone': 'Номер'
}

# user = {}
# for key, ask in user_template.items():
#     user[key] = input(ask+'\n')

# print(user)
