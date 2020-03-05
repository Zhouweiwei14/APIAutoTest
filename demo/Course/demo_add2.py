import requests
headers={'Content-Type':'application/json'}
data='''
{
  "action" : "add_course_json",
  "data" : {"name":"初中化学4234234234234234","desc":"初中化学课程","display_idx":"4"}
}
'''
data=data.encode(encoding='utf-8')

req=requests.post('http://localhost/apijson/mgr/sq_mgr/',data=data,headers=headers)

print(req.json())