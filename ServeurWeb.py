# import des modules necessaires
from EmployeHTTPRequestHandler import EmployeHTTPRequestHandler
from http.server import HTTPServer
# Le serveur va ecouter sur localhost:8080
httpd = HTTPServer(('localhost', 8080), EmployeHTTPRequestHandler)

# Commence a 'servir' les connections
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
