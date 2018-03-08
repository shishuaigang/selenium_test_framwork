import requests


def getmobilecode(url, phonenumber, cookie):
    data = {
        'APIVersion': 999999999,
        'phonenumber': phonenumber
    }
    req = requests.request('post', url=url + '/API/Account/GetMobCode', data=data, cookies=cookie)
    return req.json()['data']['items'][0]['code']
