from patient_data import patients


def get_patient(id):
    patient_info = patients.get(id)
    if patient_info:
        return {
            'name': patient_info.get('name'),
            'age': patient_info.get('age'),
            'gender': patient_info.get('gender')}


def get_diagnosis(id):
    patient_info = patients.get(id)
    if patient_info:
        return patient_info.get('diagnosis')


def get_medications(id):
    patient_info = patients.get(id)
    if patient_info:
        return patient_info.get('medications')


def get_allergies(id):
    patient_info = patients.get(id)
    if patient_info:
        return patient_info.get('allergies')

def get_meet_dates(id):
    patient_info = patients.get(id)
    if patient_info:
        return {
            'last_checkup_date': patient_info.get('last_checkup_date'),
            'next_appointment_date': patient_info.get('next_appointment_date')}
   

def get_ids():
    return list(patients.keys())

if __name__ == "__main__":

    patient_list = get_ids()

    for patient_id in patient_list:
        print(f"Patient ID: {patient_id}")
        print("Patient Info:", get_patient(patient_id))
        print("Diagnosis:", get_diagnosis(patient_id))
        print("Medications:", get_medications(patient_id))
        print("Allergies:", get_allergies(patient_id))
        print("Meeting Dates:", get_meet_dates(patient_id))
        print()

