import requests

# dict1={'action':'add_course','data':'''{
#   "name":"初中化学",
#   "desc":"初中化学课程",
#   "display_idx":"4"
# }'''
# }
proxies = {'http': 'http://127.0.0.1:8888','https': 'http://127.0.0.1:8888'}
dict2={'Content-Type':'application/x-www-form-urlencoded'}
dict1='action=add_course&data={"name":"初中化学","desc":"初中化学课程","display_idx":"4"}'
dict1=dict1.encode(encoding="utf-8")
req=requests.post("http://localhost/api/mgr/sq_mgr/",data=dict1,headers=dict2, proxies=proxies)
print(req.json())