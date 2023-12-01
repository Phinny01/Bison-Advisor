import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from user import *

cred = credentials.Certificate("softwareengineeringproje-30cbf-firebase-adminsdk-ubktw-48450c6b23.json")
databaseURL= "https://softwareengineeringproje-30cbf-default-rtdb.firebaseio.com/"
app = firebase_admin.initialize_app(cred, {'databaseURL':databaseURL})

ref = db.reference("/") # set reference to the root of the database (or you could also set it to a key value or child key value)
users_ref = ref.child('users')

# TODO: when creating new user, email and username must be unique
sashe = Student("sasheo", "mezisashe.ojuba@bison.howard.edu", "sasheo","Computer Science")
sashe.update_values_in_firebase(users_ref)
