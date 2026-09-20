from enum import Enum


class AppointmentStatus(Enum):
   

    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"


class Patient:
    

    def __init__(self, patient_id, patient_information):
        """Create a patient record."""
        self.patient_id = patient_id
        self.patient_information = patient_information

    def update_information(self, patient_information):
      
        pass


class Practitioner:
    

    def __init__(self, practitioner_id, practitioner_information, availability):
        """Create a practitioner record."""
        self.practitioner_id = practitioner_id
        self.practitioner_information = practitioner_information
        self.availability = availability

    def update_information(self, practitioner_information):
        
        pass

    def update_availability(self, availability):
        
        pass


class Appointment:
    

    def __init__(self, patient, practitioner, appointment_time, status):
        
        self.patient = patient
        self.practitioner = practitioner
        self.appointment_time = appointment_time
        self.status = status

    def cancel(self):
        
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
