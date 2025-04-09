
#def a class called 'patients'
class patients:
    
    #initialise class
    def __init__(self,patient_name,age,date_of_latest_admission,medical_history):
        self.patient_name=patient_name
        self.age=age
        self.date_of_latest_admission=date_of_latest_admission
        self.medical_history=medical_history
    #define a way to print user informations
    def print_detail(self):
        print(f"patient name: {self.patient_name}, age: {self.age}, date of latest admission: {self.date_of_latest_admission}, medical history: {self.medical_history}")

#example of class calls
patient_example=patients("Hzt", 19, "2025-04-04", "constipation, no other serious illness")
patient_example.print_detail()

#fetch user imformations
patient_name=input("Please enter patient name:")
age=int(input("Please enter patient age:"))
date_of_latest_admission=input("Please enter date of latest admission:")
medical_history=input("Please enter medical history:")

#print user informations
patient=patients(patient_name,age,date_of_latest_admission,medical_history)
patient.print_detail()