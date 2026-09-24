from enum import Enum


class AppointmentStatus(Enum):
   '''Represent the status of a SmartCare appointment'''

SCHEDULED = "scheduled"
CANCELLED = "cancelled"


class Patient:
    '''Represent a patient record (FR-01, FR-02, FR-03)'''

    def __init__(self, patient_id, patient_information):
        """Create a patient record."""
        self.patient_id = patient_id
        self.patient_information = patient_information

    def update_information(self, patient_information):
        '''Update the stored patient information'''
      
        pass


class Practitioner:
    '''Represent a practitoner record (FR-04, FR-05, FR-06)'''
    

    def __init__(self, practitioner_id, practitioner_information, availability):
        """Create a practitioner record."""
        self.practitioner_id = practitioner_id
        self.practitioner_information = practitioner_information
        self.availability = availability

    def update_information(self, practitioner_information):
        '''Update the stored practitioner information'''
        pass

    def update_availability(self, availability):
        '''Update the practitioner's availability'''
        
        pass


class Appointment:
    '''Represent an appointment (FR-07 to FR-12)'''

    def __init__(self, patient, practitioner, appointment_time, status):
        '''Create an appointment for a patient with a practitoner'''
        
        self.patient = patient
        self.practitioner = practitioner
        self.appointment_time = appointment_time
        self.status = status

    def cancel(self):
        '''Cancel the appointment.'''
        
        pass


patient = Patient("P001", "Alice Smith")

practitioner = Practitioner(
    "PR001",
    "Dr John Doe",
    "Monday to Friday"
)

appointment = Appointment(
    patient,
    practitioner,
    "2026-09-02 10:00 AM",
    AppointmentStatus.SCHEDULED
)

print("SmartCare v0.3 skeleton")
print("Patient:", patient.patient_id)
print("Practitioner:", practitioner.practitioner_id)
print("Appointment status:", appointment.status.value)
