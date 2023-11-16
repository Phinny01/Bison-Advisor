from multipledispatch import dispatch
import json
import pickle
class User:
    user_id=0

    @dispatch(str, str, str)
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        User.user_id+=1
    
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


class Student(User):
    def __init__(self, username, email, password,department):
        super().__init__(username, email, password)
        self.major = ""
        self.minor = ""
        self.classification = ""
        self.checklist = []
        self.advisor = None
        self.chats = set()
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
        # Implementation for requesting advice from the advisor
        print(f"Student {self.username} sent a message to their advisor: {message}")


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
        students_dict = {}

        try:
            with open('students.pkl', 'rb') as file:
                students_dict = pickle.load(file)

        except FileNotFoundError:
            pass

        for data in student_data:
            student = Student(data['username'], data['email'], data['password'], data['department'])
            students_dict[student.email] = student
            # SystemAdmin.assign_student_to_advisor(student)

        with open('students.pkl', 'wb') as file:
            pickle.dump(students_dict, file)

    @staticmethod
    def create_advisor_object(advisor_data):
        advisors_dict = {}

        try:
            with open('advisors.pkl', 'rb') as file:
                advisors_dict = pickle.load(file)
        except FileNotFoundError:
            pass

        for data in advisor_data:
            advisor = AcademicAdvisor(data['username'], data['email'], data['password'], data['department'])
            advisors_dict[advisor.email] = advisor

        with open('advisors.pkl', 'wb') as file:
            pickle.dump(advisors_dict, file)

        return advisor


    @staticmethod
    def assign_student_to_advisor(student):
        advisors_dict = {}


        with open('advisors.pkl', 'rb') as file:
            advisors_dict = pickle.load(file)


        # Filter advisors by department
        advisors_in_department = [advisor for advisor in advisors_dict.values() if advisor.department == student.department]
        for advisors in advisors_in_department:
            print(advisors.email, advisors.department)
        print(student.department)

        # Find the advisor with the least number of students
        selected_advisor = min(advisors_in_department, key=lambda advisor: len(advisor.advisee_student_ids))


        # Link the student to the selected advisor (put student ids in list of student associated to advisor)
        selected_advisor.link_student(student.user_id)

        # Update the advisors dictionary
        advisors_dict[selected_advisor.email] = selected_advisor

        # Save the updated advisors dictionary to the file
        with open('advisors.pkl', 'wb') as file:
            pickle.dump(advisors_dict, file)
