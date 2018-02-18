import json

#сохранить в json
with open('data.json', 'w', encoding='utf-8') as fh: #открываем файл на запись
    fh.write(json.dumps(data, ensure_ascii=False)) #преобразовываем словарь data в unicode-строку и записываем в файл

#загрузить из json
with open('data.json', 'r', encoding='utf-8') as fh: #открываем файл на чтение
    data = json.load(fh) #загружаем из файла данные в словарь data