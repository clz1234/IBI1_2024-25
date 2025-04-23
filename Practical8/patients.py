#define a patients' class
#class initialization, receive patient name; age; date of latest admission; and medical history.
#give its value
#define print_patient_details(self), to print the information in one line
#give an example, show how call the code

#define class
class patients:
    def __init__(self, patient_name, age, date_of_latest_admission, medical_history):
        #give its value
        self.patient_name = patient_name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.medical_history = medical_history
    #define a function to print the result
    def print_patient_details(self):
        print(f"name: {self.patient_name}, age: {self.age}, date of latest: {self.date_of_latest_admission}, medical history: {self.medical_history}")

#an example to call the code
patient_name = "Alan"
age = "18"
date_of_latest_admission = "2025-1-1"
medical_history = "No"
patient1 = patients(patient_name, age, date_of_latest_admission, medical_history)
patient1.print_patient_details()