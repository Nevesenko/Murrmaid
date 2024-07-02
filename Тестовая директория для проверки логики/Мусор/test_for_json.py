import json

data = {'name': 'John', 'age': 30, 'city': 'New York'}

with open('../../База данных/data.json', 'r+') as file:
    print(bool(file))
    if file is not None:
        cur_info = json.load(file)
        print(cur_info)
    json.dump(data, file)