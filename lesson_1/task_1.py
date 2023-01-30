"""
1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного
пользователя, сохранить JSON-вывод в файле *.json.
"""
import requests
import json

REPO_NAME = 'Shadow48lip'

data = requests.get(f'https://api.github.com/users/{REPO_NAME}/repos')
# print(type(json.dump(data.json())))

if data.ok:
    with open('lesson_1.json', 'w', encoding='utf-8') as f:
        # f.write(json.dumps(data.json(), ensure_ascii=False, indent=4))
        json.dump(data.json(), f, ensure_ascii=False, indent=4)

    print('Repository list saved')
else:
    print(f'Error. Status code {data.status_code}')
