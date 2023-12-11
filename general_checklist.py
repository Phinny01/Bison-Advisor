import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Use a service account.
cred = credentials.Certificate('service_account.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

# Creating a new collection goes into the collection func
checklist_ref = db.collection("general_checklist")

# list of docs in json format to populate the general checklist for computer science
checklist_doc = [
    {
    "course_subject": "CSCI 120",
    "course_title": "Exploring Computer Science",
    "credit": 2,
    "grade": "",
    "year": "Freshman"
    },
    {
    "course_subject": "",
    "course_title": "Non-Technical Elective",
    "credit": 3,
    "grade": "",
    "year": "Freshman"
    },
    {
    "course_subject": "",
    "course_title": "Science Lec A",
    "credit": 3,
    "grade": "",
    "year": "Freshman"
    },
    {
    "course_subject": "",
    "course_title": "Science Lab A",
    "credit": 1,
    "grade": "",
    "year": "Freshman"
    },
    {
    "course_subject": "ENGW",
    "course_title": "English I",
    "credit": 3,
    "grade": "",
    "year": "Freshman"
    },
    {
    "course_subject": "CSCI 100",
    "course_title": "Intro to Computer Science",
    "credit": 3,
    "grade": "",
    "year": "Freshman"
    },
    {
    "course_subject": "CSCI 135",
    "course_title": "Computer Science I",
    "credit": 4,
    "grade": "",
    "year": "Freshman"
    },
    {
    "course_subject": "CSCI 211",
    "course_title": "UNIX Lab",
    "credit": 1,
    "grade": "",
    "year": "Freshman"
    },
    {
    "course_subject": "MATH 156",
    "course_title": "Calculus I",
    "credit": 4,
    "grade": "",
    "year": "Freshman"
    },
    {
    "course_subject": "ENGW",
    "course_title": "English II",
    "credit": 3,
    "grade": "",
    "year": "Freshman"
    },
    {
    "course_subject": "SLMC 101",
    "course_title": "Principles of Speech",
    "credit": 3,
    "grade": "",
    "year": "Freshman"
    },
    {
    "course_subject": "CSCI 136",
    "course_title": "Computer Science II",
    "credit": 3,
    "grade": "",
    "year": "Sophomore"
    },
    {
    "course_subject": "CSCI 136",
    "course_title": "Computer Organization I",
    "credit": 3,
    "grade": "",
    "year": "Sophomore"
    },
    {
    "course_subject": "MATH 157",
    "course_title": "Calculus II",
    "credit": 4,
    "grade": "",
    "year": "Sophomore"
    },
    {
    "course_subject": "",
    "course_title": "Science Lec B(1)",
    "credit": 3,
    "grade": "",
    "year": "Sophomore"
    },
    {
    "course_subject": "",
    "course_title": "Science Lab B(1)",
    "credit": 1,
    "grade": "",
    "year": "Sophomore"
    },
    {
    "course_subject": "CSCI 354",
    "course_title": "Computer Science III",
    "credit": 3,
    "grade": "",
    "year": "Sophomore"
    },
    {
    "course_subject": "Large Scale Programming",
    "course_title": "CSCI 363",
    "credit": 3,
    "grade": "",
    "year": "Sophomore"
    },
    {
    "course_subject": "CSCI 202",
    "course_title": "Computer Organization II",
    "credit": 3,
    "grade": "",
    "year": "Sophomore"
    },
    {
    "course_subject": "MATH 181",
    "course_title": "Discrete Structures",
    "credit": 3,
    "grade": "",
    "year": "Sophomore"
    },
    {
    "course_subject": "Science Lec B(2)",
    "course_title": "",
    "credit": 3,
    "grade": "",
    "year": "Sophomore"
    },
    {
    "course_subject": "",
    "course_title": "Science Lab B(2)",
    "credit": 1,
    "grade": "",
    "year": "Sophomore"
    },
    {
    "course_subject": "",
    "course_title": "",
    "credit": 3,
    "grade": "",
    "year": "Sophomore"
    },
    {
    "course_subject": "CSCI 341",
    "course_title": "Theory of Computation",
    "credit": 3,
    "grade": "",
    "year": "Junior"
    },
    {
    "course_subject": "CSCI 401",
    "course_title": "Operating Systems",
    "credit": 3,
    "grade": "",
    "year": "Junior"
    },
    {
    "course_subject": "CSCI 341",
    "course_title": "Fundamentals of Algorithm",
    "credit": 3,
    "grade": "",
    "year": "Junior"
    },
    {
    "course_subject": "CSCI 450",
    "course_title": "Data Communications and Network Programming",
    "credit": 3,
    "grade": "",
    "year": "Junior"
    },
    {
    "course_subject": "CSCI 453",
    "course_title": "Intro to Cybersecurity I",
    "credit": 3,
    "grade": "",
    "year": "Junior"
    },
    {
    "course_subject": "CSCI 350",
    "course_title": "Structure of Programming Languages",
    "credit": 3,
    "grade": "",
    "year": "Junior"
    },
    {
    "course_subject": "",
    "course_title": "Technical Elective",
    "credit": 3,
    "grade": "",
    "year": "Junior"
    },
    {
    "course_subject": "CSCI 432",
    "course_title": "Database Systems",
    "credit": 3,
    "grade": "",
    "year": "Junior"
    },
    {
    "course_subject": "ENGL 009",
    "course_title": "Technical Writing",
    "credit": 3,
    "grade": "",
    "year": "Junior"
    },
    {
    "course_subject": "MATH 180",
    "course_title": "Intro to Linear Algebra",
    "credit": 3,
    "grade": "",
    "year": "Junior"
    },
    {
    "course_subject": "CSCI 491",
    "course_title": "Senior Project I",
    "credit": 3,
    "grade": "",
    "year": "Senior"
    },
    {
    "course_subject": "CSCI 375",
    "course_title": "Software Engineering",
    "credit": 3,
    "grade": "",
    "year": "Senior"
    },
    {
    "course_subject": "CSCI 473",
    "course_title": "Applied Data Science",
    "credit": 4,
    "grade": "",
    "year": "Senior"
    },
    {
    "course_subject": "",
    "course_title": "Technical Elective",
    "credit": 3,
    "grade": "",
    "year": "Senior"
    },
    {
    "course_subject": "",
    "course_title": "Technical Elective",
    "credit": 3,
    "grade": "",
    "year": "Senior"
    },
    {
    "course_subject": "",
    "course_title": "Technical Elective",
    "credit": 3,
    "grade": "",
    "year": "Senior"
    },
    {
    "course_subject": "CSCI 492",
    "course_title": "Senior Project II",
    "credit": 2,
    "grade": "",
    "year": "Senior"
    },
    {
    "course_subject": "",
    "course_title": "Technical Elective",
    "credit": 3,
    "grade": "",
    "year": "Senior"
    },
    {
    "course_subject": "",
    "course_title": "Non-Technical Elective",
    "credit": 3,
    "grade": "",
    "year": "Senior"
    },
    {
    "course_subject": "",
    "course_title": "Non-Technical Elective",
    "credit": 3,
    "grade": "",
    "year": "Senior"
    }
]

for doc in checklist_doc:
    checklist_ref.document().set(doc)


