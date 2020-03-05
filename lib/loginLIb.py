import requests


def login(username,password):
    data = {'username': f'{username}', 'password': f'{password}'}
    headers = {'Content-Type': 'application/json'}
    try:
        req = requests.post('http://localhost/api/mgr/loginReq', data=data,headers=headers)

        return req.json(), req.cookies['sessionid']
    except:
        return '异常错误'



