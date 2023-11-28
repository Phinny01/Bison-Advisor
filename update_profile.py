import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from user import User

cred = credentials.Certificate("softwareengineeringproje-30cbf-firebase-adminsdk-ubktw-48450c6b23.json")
databaseURL= "https://testbookstoreproject-default-rtdb.firebaseio.com/"
app = firebase_admin.initialize_app(cred, {'databaseURL':databaseURL})

ref = db.reference("/") # set reference to the root of the database (or you could also set it to a key value or child key value)