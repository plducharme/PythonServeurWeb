'''
    Client Web pour tester
    voir: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request (en anglais seulement)
'''

# import des classes necessaires (dependence sur le package requests)
import requests

url = 'http://localhost:8080'
headers = {'Content-Type': 'text/plain'}

post_body = 'Nguyen,Alice,75360'
post_request = requests.post(url + '/', headers=headers, data=post_body)
print('Requete POST /')
print(post_request.status_code)
print(post_request.text)

get_request = requests.get(url + '/' , headers=headers)
print('Requete GET /')
print(get_request.status_code)
print(get_request.text)

get_request_sommaire = requests.get(url + '/sommaire', headers=headers)
print('Requete GET /sommaire')
print(get_request_sommaire.status_code)
print(get_request_sommaire.text)
