import sqlite3
connection = sqlite3.connect('swiftlinkdb.db')
print(connection.total_changes)
cursor = connection.cursor()

cursor.execute(
    'CREATE TABLE IF NOT EXISTS patients (id INTEGER PRIMARY KEY, prenom TEXT, nom TEXT, mdp TEXT)'
)

#essayer d'utiliser utiliser la fonction MD5('mot_de_passe') dans le sql pour chiffrer le mot de passe et les infos sensibles

#fonctions d'accès à la base de donnée ici