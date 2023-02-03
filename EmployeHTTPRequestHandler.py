#Import de la classe a partir du module
from http.server import BaseHTTPRequestHandler
'''
Cette classe est une sous-classe de BaseHTTPRequestHandler voir:
https://docs.python.org/fr/3/library/http.server.html?highlight=basehttprequest#http.server.BaseHTTPRequestHandler

Cette classe permet:
- d'enregister une liste d'employees avec leur salaire via POST
- de retourner la liste des employees ainsi que leur salaire sur GET /
- de retourner la liste des employees ainsi que la mediane des salaires GET /sommaire
'''
class EmployeHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Renvoie du statut
        self.send_response(200)
        # ajout d'entete HTTP pour specifer le contenu renvoye
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        # Logique a implementer

        #
        # String HTML de test
        response_string = '<html>' \
                          ' <head><title>Employes Acme Co</title></head>' \
                          ' <p>Ceci est une String de test!' \
                          '</html>'
        # Exemple de renvoie d'une String convertie en Bytes UTF-8
        self.wfile.write(bytes(response_string, 'utf-8'))

    def do_POST(self):
        # Le nombre de bytes a lire est contenu dans l'entente de la requete
        content_length = int(self.headers['Content-Length'])
        # lecture entiere du corps du POST
        body = self.rfile.read(content_length)
        print(body)
        # logique pour lire les employes et leurs salaires a implementer

        #
        # Renvoie du statut
        self.send_response(200)
        # renvoie d'entete(s)
        self.end_headers()
        # Renvoie d'une String de test
        self.wfile.write(bytes('Recu ' + str(content_length) + ' bytes', 'utf-8'))



