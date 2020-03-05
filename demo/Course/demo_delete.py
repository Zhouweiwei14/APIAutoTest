import requests

headers={'Content-Type':'application/x-www-form-urlencoded'}

data={
    'action':'delete_course',
    'id':'1516'

}
req=requests.delete('http://localhost/api/mgr/sq_mgr/',data=data,headers=headers)

print(req.json())