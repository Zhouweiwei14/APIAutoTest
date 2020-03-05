import requests


dict1={'action':'list_course','pagenum':1,'pagesize':20}
req=requests.get('http://localhost/api/mgr/sq_mgr/',params=dict1)


print(req.json())