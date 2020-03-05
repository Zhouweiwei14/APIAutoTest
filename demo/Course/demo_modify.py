import requests
data={
    'action':'modify_course',
    'id': '1517',
    'newdata': '''{"name":"初中化学12112","desc":"初中化学课程","display_idx":"4"}'''

}
# payload={
#     'action':'modify_course',
#     'id':'2013',
#     'newdata': '''{"name":"初中化学8888","desc":"初中化学课程","display_idx":"4"}'''

headers={'Content-Type':'application/x-www-form-urlencoded'}


req=requests.put('http://localhost/api/mgr/sq_mgr/',data=data,headers=headers)

print(req.json())