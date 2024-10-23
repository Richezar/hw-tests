import requests

def create_folder(folder, token):  # метод создает папку на Я.Диск
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    params = {
        'path': folder
    }
    headers = {
        'Authorization': f'OAuth {token}'
    }
    res = requests.put(url, params=params, headers=headers).status_code
    return res

