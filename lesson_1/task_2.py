"""
Найти любое API, требующее авторизацию (любого типа).
Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
"""
import requests
import json

API_KEY = 'e2a8f2e2658995f80e46e0fc76114136'
IP_ADDRESS = '8.8.4.4'

params = {'access_key': API_KEY}
data = requests.get(f'http://api.ipstack.com/{IP_ADDRESS}', params=params)

if data.ok:
    with open('lesson_2.json', 'w', encoding='utf-8') as f:
        json.dump(data.json(), f, ensure_ascii=False, indent=4)

    print('Information saved')
else:
    print(f'Error. Status code {data.status_code}')