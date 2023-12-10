import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Use a service account.
cred = credentials.Certificate('service_account.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

checklist_ref = db.collection("checklist").document()

checklist_ref.set(
    {
    "course_subject": "CSCI 100",
    "course_title": "Intro to Computer Science",
    "credit": 3,
    "grade": "A",
    "year": "Freshman"
    }
)