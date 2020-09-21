import json

data = [{
    'one': 'HELLO',
    'TWO': [1, 2, 3, 4, 'yep'],
    1: False,
    2: True,
    3: None,
    4: "КИРИЛИТИЧЕСКИЙ ТЕКСТ",
    5: (22, 33, 44),
},
    {
        'one': 'HELLO',
        'TWO': [1.22, 2, 3, 4, 'yep'],
        1: False,
        2: True,
        3: None,
        4: "КИРИЛИТИЧЕСКИЙ ТЕКСТ",
        5: (22, 33, 44),
    },
]

j_data = json.dumps(data, ensure_ascii=False)

with open('test.json', 'w', encoding='UTF-8') as file:
    # file.write(json.dumps(data, ensure_ascii=False))
    json.dump(data, file, ensure_ascii=False)
print(j_data)

enc_data = json.loads(j_data)
print(type(enc_data))
print(enc_data)
