import fetch_patient_data as fetch2

list_id = fetch2.get_ids()

print("")
print("IDs: ", list_id)
print("")
print("OPTIONS: ")
print("Details")
print("Diagnosis")
print("Allergies")
print("Dates")
print("")


def ask_id():
    while True:
        user_id = input("Please, enter a patient ID from the list above: ") 

        if user_id in list_id:
            ask_list(user_id)
            break  

        print("It's an invalid ID. Please, enter the correct information again.")

def ask_list(user_id):

    while True:    
        ask_option = input("Please, enter a option from the list above: ")

        if ask_option == "Details":
            patient_details = fetch2.get_patient(user_id)
            print(f"Details for patient ID {user_id}: {patient_details}")
        elif ask_option == "Diagnosis":
            patient_diagnosis = fetch2.get_diagnosis(user_id)
            print(f"Details for patient ID {user_id}: {patient_diagnosis}")
        elif ask_option == "Allergies":
            patient_allergies = fetch2.get_allergies(user_id)
            print(f"Details for patient ID {user_id}: {patient_allergies}")
        elif ask_option == "Dates":
            patient_dates = fetch2.get_meet_dates(user_id)
            print(f"Details for patient ID {user_id}: {patient_dates}")
        else: 
            print("It's an invalid option. Please, enter the correct information again.") 
            ask_list(user_id)   
        break

ask_id()
