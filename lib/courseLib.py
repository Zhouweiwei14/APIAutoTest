import requests
proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

def  CourseAdd(name,desc,display_idx):
    data={'action':'add_course',
           'data':f'{{"name":"{name}","desc":"{desc}","display_idx":"{display_idx}"}}'
    }

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    #dict1 = 'action=add_course&data={"name":"初中化学","desc":"初中化学课程","display_idx":"4"}'
    #dict1 = dict1.encode(encoding="utf-8")
    try:
        req = requests.post("http://localhost/api/mgr/sq_mgr/", data=data, headers=headers, proxies=proxies)
        return req.json()
    except:
        return '异常'

#print(CourseAdd('英文大学4234234','ceshjhjhj','0'))

def CourseDelete(id):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    data = {'action': 'delete_course','id': id}
    try:
        req = requests.delete('http://localhost/api/mgr/sq_mgr/', data=data, headers=headers)
        return req.json()
    except:
        return '异常'


def CourseList(pagenum,pagesize):
    params = {'action': 'list_course', 'pagenum': pagenum, 'pagesize':pagesize}
    try:
        req = requests.get('http://localhost/api/mgr/sq_mgr/', params=params)
        return req.json()
    except:
        return '异常'


def CourseModify(id,name,desc,display_idx):
    data = {
        'action': 'modify_course',
        'id': f'{id}',
        'newdata': f'''{{"name":"{name}","desc":"{desc}","display_idx":"{display_idx}"}}'''

    }
    # payload={
    #     'action':'modify_course',
    #     'id':'2013',
    #     'newdata': '''{"name":"初中化学8888","desc":"初中化学课程","display_idx":"4"}'''

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    try:
        req = requests.put('http://localhost/api/mgr/sq_mgr/', data=data, headers=headers)
        return req.json()
    except:
        return '异常'


def CourseAdds(name,desc,display_idx):
    headers = {'Content-Type': 'application/json'}
    data =f'''
    {{
      "action" : "add_course_json",
      "data" :{{"name":"{name}","desc":"{desc}","display_idx":"{display_idx}"}}
    }}
    '''
    data = data.encode(encoding='utf-8')
    try:
        req = requests.post('http://localhost/apijson/mgr/sq_mgr/', data=data, headers=headers)
        return req.json()
    except:
        return '异常'