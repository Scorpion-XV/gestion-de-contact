import sqlite3

print("Application de Gestion de contacte avec Python et Sqlite3")

with sqlite3.connect("Lescontact.db") as connection:
    cursor = connection.cursor()
    
class Contact :
    def __init__(self, NomComplet, AdresseEmail, Telephone, Adresse) :
        self.NomComplet = NomComplet
        self.AdresseEmail = AdresseEmail
        self.Telephone = Telephone
        self.Adresse = Adresse
    
    def create_table(self):
        cursor.execute(
        "CREATE TABLE if not exists contacts (ID INTEGER PRIMARY KEY AUTOINCREMENT,NomComplet TEXT NOT NULL, AdresseEmail TEXT, Telephone TEXT NOT NULL, Adresse TEXT)")
    
    def ajouter_contacte(self):
        self.NomComplet = input('votre nom : ')
        self.AdresseEmail = input('votre email : ')
        self.Telephone = input('votre telephone : ')
        self.Adresse = input('Votre adresse : ')
        cursor.execute("INSERT INTO contacts(NomComplet, AdresseEmail, Telephone, Adresse) VALUES(?, ?, ?, ?)", (self.NomComplet, self.AdresseEmail,self.Telephone, self.Adresse))
        connection.commit()
        
    def supprimer_contacte(self):
        self.Telephone = input('votre telephone : ')
        cursor.execute(
        "DELETE FROM contacts WHERE Telephone = ?",
        (self.Telephone, ))
        connection.commit()
        
    def afficher_les_contactes(self):
        print(cursor.execute(
        "SELECT * FROM contacts").fetchall())
        
        
class ContactModifie(Contact):
    def __init__(self, NomComplet, AdresseEmail, Telephone, Adresse , nouveau_numero, ancien_numero) :
        Contact.__init__(self, NomComplet, AdresseEmail, Telephone, Adresse)
        self.nouveau_numero = nouveau_numero
        self.ancien_numero = ancien_numero
    def modifier_contacte(self):
        self.nouveau_numero = input('votre ancien numero : ')
        self.ancien_numero = input('votre nouveau numero : ')
        cursor.execute(
        "UPDATE contacts SET Telephone = ? WHERE telephone = ?",
        (self.ancien_numero, self.nouveau_numero))
        connection.commit()
        
class ContactAffiche(Contact):
    def __init__(self, NomComplet, AdresseEmail, Telephone, Adresse , row) :
        Contact.__init__(self, NomComplet, AdresseEmail, Telephone, Adresse)
        self.row = row
    def afficher_un_contacte(self):
        self.Telephone = input('votre telephone : ')
        self.row = cursor.execute(
        "SELECT * FROM contacts WHERE telephone = ?",(self.Telephone, )).fetchone()
        if self.row:
            print(self.row)
        else:
            print('contact non trouve')
     
Contact.create_table(Contact)
if __name__ == '__main__':
    while True:
            print("1. Ajouter un contact")
            print("2. Modifier un contact")
            print("3. Supprimer un contact")
            print("4. Afficher la liste des contacts")
            print("5. Rechercher un contact")
            print("6. Quitter")
            choix = input("Veuillez saisir le numero de votre choix : ")
            if choix == '1':
                print("Bienvenue dans notre rubrique d'ajout de contact\n")
                Contact.ajouter_contacte(Contact)
            elif choix == '2':
                print("Bienvenue dans notre rubrique de modification de contact\n")
                ContactModifie.modifier_contacte(ContactModifie)
            elif choix == '3':
                print("Bienvenue dans notre rubrique de suppression de contact\n")
                Contact.supprimer_contacte(Contact)
            elif choix == '4':
                print("La liste des contacts\n")
                Contact.afficher_les_contactes(Contact)
            elif choix == '5':
                print("Bienvenue dans le rubrique de recherche de contact\n")
                ContactAffiche.afficher_un_contacte(ContactAffiche)
            elif choix == '6':
                break
            else:
                print("Choix invalide.\n")