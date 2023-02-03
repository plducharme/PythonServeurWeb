# PythonServeurWeb
## Instructions de mise en place
- Cloner le dépot https://github.com/plducharme/PythonServeurWeb.git
- Ajouter l'environnement virtuel dans PyCharm
  - File -> Settings -> Project: Python ServeurWeb -> Python Interpreter -> add local interpreter (à droite) -> OK
- Installer le package "requests"
  - PyCharm:
    - menu View -> Tool Windows -> Python Packages
    - chercher pour requests et cliquer "install package" à droite
    ![](/images/requests_package.PNG)
  - Visual Studio:
    - https://learn.microsoft.com/fr-ca/visualstudio/python/tutorial-working-with-python-in-visual-studio-step-05-installing-packages?view=vs-2022
    ![](/images/vs_requests_package.PNG)

## Description
Ce projet contient trois fichiers principaux:
- EmployeHTTPRequestHandler.py
  - Contient la classe impémentant la logique pour gérer les requêtes
- ServeurWeb.py
  - Permet de démarrer le serveur Web
- ClentWeb.py
  - Client Web permettant de tester le serveur web

## Exercices
- ServeurWeb.py
  - Implémenter la méthode do_POST(self) permettant de sauvegarder en mémoire une liste d'employés à partir du contenu de la requête
    - Le "body" est String (en bytes) contenant une entrée sous la forme \<nom de famille\>,\<prénom\>,\<salaire\>
- ClientWeb.py
  - Modifier le code pour envoyer plusieurs Employés via des requêtes POST
  - Les requêtes GET peuvent être aussi tester dans le navigateur
    - http://localhost:8080/
    - http://localhost:8080/sommaire
- ServeurWeb.py
  - Implémenter la méthode do_GET(self)
    - Pour qu'elle affiche la liste des employées avec leurs salaires pour la requête GET /
    - Pour qu'elle affiche la liste des employées avec leurs salaires en order croissant de salaire ainsi que la moyenne des salaires et la médiane des salaires pour la requête GET /sommaire
      - La requête GET / doit continuer de fonctionner
- Extra
  - Renvoyer le résultant des GET dans une table HTML https://fr.w3docs.com/apprendre-html/les-tableaux-html.html
  - Convertir les fichiers ServeurWeb.py et ClientWeb.py pour en faire des classes respectant l'encapsulation

## Bugs
Si vous trouvez des bugs dans le code de base, me contacter via MIO