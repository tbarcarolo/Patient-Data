patients = {
    'P12345': {
        'name': 'John Doe',
        'age': 35,
        'gender': 'Male',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril', 'Hydrochlorothiazide'],
        'allergies': ['Penicillin'],
        'last_checkup_date': '2022-05-20',
        'next_appointment_date': '2023-11-15',
    },
    'P67890': {
        'name': 'Jane Smith',
        'age': '41',
        'gender': 'Female',
        'diagnosis': 'Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'allergies': [],
        'last_checkup_date': '2023-04-20',
        'next_appointment_date': 'No-Date',
    },
    'P24680': {
        'name': 'Robert Johnson',
        'age': 28,
        'gender': 'Male',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol', 'Prednisone'],
        'allergies': ['Peanuts'],
        'last_checkup_date': '2022-06-08',
        'next_appointment_date': '2023-12-10',
    },
    'P18945': {
        'name': 'Alice Davis',
        'age': 55,
        'gender': 'Female',
        'diagnosis': 'Diabetes',
        'medications': ('Metformin', 'Insulin'),
        'allergies': ['Penicillin'],
        'last_checkup_date': '2023-04-15',
        'next_appointment_date': 'No-Date',
    },
    'P69918': {
        'name': 'Michael Smith',
        'age': 42,
        'gender': 'Male',
        'diagnosis': 'Hypertension',
        'medications': ('Lisinopril', 'Hydrochlorothiazide'),
        'allergies': [],
        'last_checkup_date': '2023-05-20',
        'next_appointment_date': '2023-11-20',
    },
    'P13579': {
        'name': 'Emily Johnson',
        'age': 33,
        'gender': 'Female',
        'diagnosis': 'Migraine',
        'medications': ['Sumatriptan', 'Ibuprofen'],
        'allergies': ['Sulfonamides'],
        'last_checkup_date': '2023-01-05',
        'next_appointment_date': '2023-12-05',
    }
}

# Exercise 1

# 1.1
def average_age():
    agesum = 0
    countpatients = 0

    for patient_age in patients.keys():
        patient = patients[patient_age]
        try:
            age = int(patient['age'])
            agesum += age
            countpatients += 1
        except:
            print("String value has been found")
            
    if countpatients == 0:
        return 0
    else:
        print("Total sum of age: ", agesum, "\nTotal amount of patients: ", countpatients)
        return agesum / countpatients


#1.2

def add_medication(id, med):
    
    try: 
        if id not in patients:
            raise ValueError(f"Invalid patient ID: {id}")

        if not isinstance(med, str): 
            raise ValueError("Invalid medication type. Expected str.")

        if isinstance(patients[id]["medications"], tuple):
            patients[id]["medications"] = list(patients[id]["medications"])

        patients[id]["medications"].append(med)
    except ValueError as e:
        print(f"Error: {e}")      
        

#1.3

from datetime import datetime

def upcoming_appointments(id):
    
    try:
        if id not in patients:
            raise ValueError(f"Invalid patient ID.")
        

        last_date_str = patients[id]['last_checkup_date']
        next_date_str = patients[id]['next_appointment_date']

        
        if next_date_str == 'No-Date':
            print(f"Patient {id} has no upcoming appointment date.")
            return "No upcoming appointment date."
        
        date1 = datetime.strptime(patients[id]['last_checkup_date'], '%Y-%m-%d')
        date2 = datetime.strptime(patients[id]['next_appointment_date'], '%Y-%m-%d')

        time_difference = date2-date1

        return time_difference
    
    except ValueError as e:
        print(f"Error: {e}")
    return f"Error processing data for patient {id}."


if __name__ == "__main__":

    print("")
    result = average_age()
    print("Average result: ", result)
    print("")

    meds = ["Aspirin", "Acetaminophen", "Penicillin", "Amoxicillin", "Ibuprofen", "Hydrochlorothiazide"]
    for id, med in zip(patients.keys(), meds):
    
        print("For: ", patients[id]["name"])
        print("Medications before: ", patients[id]["medications"])
    
        add_medication(id, med)
    
        print("Medications after: ", patients[id]["medications"])
        print("")

    for patient_id in patients.keys():
        print(f"Patient {patient_id}: {upcoming_appointments(patient_id)}")
        print("")






    



        