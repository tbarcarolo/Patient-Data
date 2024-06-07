# Patient Data Management System

In this assignment, I developed a patient data management system to handle and analyze patient information. It is structured into two main parts, focusing on data manipulation and creating a user-friendly interface for accessing patient details.


## Part 1:

In the first part, I extended the functionality of a Python dictionary named `patients`, which contains detailed information about some patients. Each patient is represented by a unique patient ID (e.g., 'P12345') and their details are stored as nested dictionaries.


## Part 2:

To facilitate easy access to patient data, I designed a command-line interface (CLI) for doctors to retrieve patient information. This interface complies with GDPR by separating data access and interface functionalities into distinct modules.

### Module 1: Fetching Patient Data

I created the `fetch_patient_data.py` module to encapsulate functions that retrieve specific pieces of patient data. 

### Module 2: Doctor Interface

In the `doctor_interface.py` module, I created a CLI that interacts with the `fetch_patient_data` module to provide a seamless experience for doctors.
