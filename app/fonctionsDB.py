from flask_sqlalchemy import SQLAlchemy
import random
import string
db = SQLAlchemy()

# Modèles de données
class Patients(db.Model):
    IdPatient = db.Column(db.Integer, primary_key=True,nullable=False,)
    email = db.Column(db.String(50), nullable=False)
    code = db.Column(db.Integer, nullable=False)
    mdp = db.Column(db.String, nullable=False, unique=True)

class Accompagnants(db.Model):
    IdAccompagnant = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    relation = db.Column(db.String(50), nullable=False)
    IdPatient = db.Column(db.Integer, db.ForeignKey('Patients.IdPatient'), nullable=False)
    patient = db.relationship('Patient', backref=db.backref('accompagnants', lazy='dynamic'))




def generer_code_unique(patient_id):
    """
    Génère un code unique de 6 caractères alphanumériques pour un patient donné.
    """
    # Utilise l'ID du patient comme base pour générer un code unique
    random.seed(patient_id)
    
    # Génère un code de 6 caractères alphanumériques
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    
    return code
# Fonctions# Fonctions pour les patients
def creer_patient(email,  mdp):
    code = generer_code_unique(IdPatient)

    patient = Patients(email=email, code=code, mdp=mdp)
    db.session.add(patient)
    db.session.commit()
    return patient

def get_patient_by_email(email):
    return Patients.query.filter_by(email=email).first()

def get_patient_by_id(id):
    return Patients.query.get(id)

def update_patient(patient_id, email, code, mdp):
    patient = Patients.query.get(patient_id)
    patient.email = email
    patient.code = code
    patient.mdp = mdp
    db.session.commit()
    return patient

def delete_patient(patient_id):
    patient = Patients.query.get(patient_id)
    db.session.delete(patient)
    db.session.commit()

# Fonctions pour les accompagnants
def creer_accompagnant(nom, prenom, relation, patient_id):
    accompagnant = Accompagnants(nom=nom, prenom=prenom, relation=relation, IdPatient=patient_id)
    db.session.add(accompagnant)
    db.session.commit()
    return accompagnant

def get_accompagnants_by_patient_id(patient_id):
    return Accompagnants.query.filter_by(IdPatient=patient_id).all()

def update_accompagnant(accompagnant_id, nom, prenom, relation):
    accompagnant = Accompagnants.query.get(accompagnant_id)
    accompagnant.nom = nom
    accompagnant.prenom = prenom
    accompagnant.relation = relation
    db.session.commit()
    return accompagnant

def delete_accompagnant(accompagnant_id):
    accompagnant = Accompagnants.query.get(accompagnant_id)
    db.session.delete(accompagnant)
    db.session.commit()