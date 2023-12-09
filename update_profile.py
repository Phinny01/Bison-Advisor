'''
This is all testing to ensure you can update user profile as whatever is stored in that user object 
by calling student_instance.update_values_in_firebase(users_ref) where users_ref is a realtime database reference to where users are sotred
'''
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from user import *

cred = credentials.Certificate("softwareengineeringproje-30cbf-firebase-adminsdk-ubktw-48450c6b23.json")
databaseURL= "https://softwareengineeringproje-30cbf-default-rtdb.firebaseio.com/"
app = firebase_admin.initialize_app(cred, {'databaseURL':databaseURL})

ref = db.reference("/") # set reference to the root of the database (or you could also set it to a key value or child key value)
users_ref = ref.child('users')

# # TODO: when creating new user, email and username must be unique
# sashe = Student("sasheo", "mezisashe.ojuba@bison.howard.edu", "sasheo","Computer Science")
# sashe.update_values_in_firebase(users_ref)

# load user from firebase
username = "sasheo"
print(users_ref.child(username).get())