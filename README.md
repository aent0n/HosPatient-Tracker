# HosPatient-Tracker
![image](https://github.com/aent0n/HosPatient-Tracker/assets/116871473/fd2fd302-4575-4363-805f-c2bdadf39cd3)
![image](https://github.com/aent0n/HosPatient-Tracker/assets/116871473/288826f2-4951-4c2a-801d-0c094e8d1733)
![image](https://github.com/aent0n/HosPatient-Tracker/assets/116871473/4fa34f46-83ea-4cb1-b6c4-b67791f2c492)



## What is it ?
HosPatient-Tracker is a web application designed to streamline patient tracking within a hospital emergency department. The system utilizes a "room" based approach, providing a clear visual representation of a patient's journey through various stages of their emergency care.


## Key Features
**Room-Based Tracking**: Patients are assigned to virtual "rooms" representing different stages of their treatment (e.g., triage, examination, lab tests). Each room has:

- A descriptive name
- A brief description of the stage
- An estimated time for completion
- Optionally, a queue for patients awaiting that stage
**Dynamic Room Generation**: Upon patient arrival, a sequence of rooms is automatically generated based on their initial diagnosis, ensuring a tailored care pathway.

**Secure Patient Identification**: A unique encrypted identifier is used to link patients with their relatives. This ID is securely stored in the database and can only be decrypted by authorized personnel, ensuring patient privacy. Relatives can use this ID to access patient tracking information.

**User-Friendly Interface**: The application features a "fast food" style interface with large buttons and clear visuals, optimized for quick and efficient navigation in a high-pressure environment.

## Technical Details
- **Database**: SQLlite will be used for storing patient data and room information
- **Encryption**: No big security process, each patient have a unique code
- **Front-End Technologies**: HTML5, CSS3 (Tailwind Framework), JavaScript
- **Back-End Technologies**: [List the technologies used for server-side logic (Python)]

## Installation and Usage
[Provide instructions on how to set up and run the application]

## License
This project is under a MIT license.




