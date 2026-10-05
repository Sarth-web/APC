# Hospital Patient Management System

patients = {}


def add_patient():
    patient_id = input("Enter Patient ID: ")

    if patient_id in patients:
        print("Patient ID already exists.")
        return

    name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    disease = input("Enter Disease: ")
    phone = input("Enter Phone Number: ")

    patients
