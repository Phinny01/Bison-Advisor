'''
Have only really worked on User and Student class.
'''

from multipledispatch import dispatch
import json
import pickle
class User:

    @dispatch(str, str, str)
    def __init__(self, username, email, password):
        self.username = username
        self.email = email # email must be unique
        self.password = password
    
    @dispatch(dict)
    def __init__(self, user_json):
        # TODO: fill this in
        pass

    def sign_in(self):
        # Implementation for user sign-in
        print(f"{self.username} signed in.")

    def sign_out(self):
        # Implementation for user sign-out
        print(f"{self.username} signed out.")
    
    def save_values(self):
        '''
        returns: 
            (dict) the user details
        '''
        return {"email": self.email, "password": self.password}
    
    def update_values_in_firebase(self, users_ref):
        '''
        params:
            users_ref: 
                (firebase realtime db reference) a firebase realtime database reference to where users are stored
        '''
        users_ref.update({self.username:self.save_values()})
    


class Student(User):
    def __init__(self, username, email, password,department):
        super().__init__(username, email, password)
        self.major = ""
        self.minor = ""
        self.classification = ""
        self.checklist = []
        self.advisor = None
        self.chats = [] # will be a list of chat ids
        self.department=department

    def set_major(self, major):
        self.major = major

    def set_minor(self, minor):
        self.minor = minor

    def set_classification(self, classification):
        self.classification = classification

    def set_checklist(self, checklist):
        self.checklist = checklist

    def set_advisor(self, advisor_id):
        self.advisor = advisor_id

    def request_advice(self, message):
        # TODO: Implementation for requesting advice from the advisor
        print(f"Student {self.username} sent a message to their advisor: {message}")
    
    def save_values(self):
        '''
        returns: 
            user_data: (dict) the user details
        '''
        user_data =super().save_values()
        user_data["major"] = self.major
        user_data["minor"] = self.minor
        user_data["classification"] = self.classification
        user_data["advisor"] = self.advisor
        user_data["checklist"] = self.checklist
        user_data['chats'] = self.chats
        user_data["department"] = self.department
        return user_data




class Chat():
    pass

class AcademicAdvisor(User):
    def __init__(self, username, email, password,department):
        super().__init__(username, email, password)
        self.department = department
        self.advisee_student_ids = set()

    def link_student(self, student_id):
        self.advisee_student_ids.add(student_id)

    def provide_advice(self, student_id, advice):
        # Implementation for providing advice to a student
        print(f"Advisor {self.username} provided advice to Student {student_id}: {advice}")


class SystemAdmin(User):
    def __init__(self, username, email, password):
        super().__init__(username, email, password)

    @staticmethod
    def create_student_objects(student_data):
        pass

    @staticmethod
    def create_advisor_object(advisor_data):
        pass


    @staticmethod
    def assign_student_to_advisor(student):
        pass
