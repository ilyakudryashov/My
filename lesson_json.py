import json
""""
#сохранить в json
with open('data.json', 'w', encoding='utf-8') as fh: #открываем файл на запись
    fh.write(json.dumps(data, ensure_ascii=False)) #преобразовываем словарь data в unicode-строку и записываем в файл

#загрузить из json
with open('data.json', 'r', encoding='utf-8') as fh: #открываем файл на чтение
    data = json.load(fh) #загружаем из файла данные в словарь data


# to string
data = ['Test data', {'Structure':'Any'} ]
s = json.dumps(data)
print(s)

# from string
print(json.loads(s))

# save
data = ['Test data', {'Structure':'Any'} ]
json.dump(data, open('test', 'w'))

# load
data = json.load( open('test', 'r') )

"""

s = {'4': 5, '6': 7}
print(json.dumps(s, sort_keys=True, indent=1))
