import requests
data={'username':'auto','password':'sdfsdfsdf'}
headers={'Content-Type':'application/json'}
req=requests.post('http://localhost/api/mgr/loginReq',data=data)

print(req.json())
print(req.cookies['sessionid'])