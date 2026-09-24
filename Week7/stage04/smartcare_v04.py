from enum import Enum


class AppointmentStatus(Enum):
    

    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"


class InvalidAppointmentStateError(Exception):
    pass
    

class Patient:
    
    def __init__(self, patient_id: str, patient_information: str) -> None:
        
        if not patient_id.strip():
            raise ValueError("Patient ID cannot be empty.")

        if not patient_information.strip():
            raise ValueError("Patient information cannot be empty.")

        self.patient_id = patient_id
        self.patient_information = patient_information

    def update_information(self, patient_information: str) -> None:
        
        if not patient_information.strip():
            raise ValueError("Patient information cannot be empty.")

        self.patient_information = patient_information


class Practitioner:
    

    def __init__(
        self,
        practitioner_id: str,
        name: str,
        specialty: str,
        availability: str
    ) -> None:
        
        if not practitioner_id.strip():
            raise ValueError("Practitioner ID cannot be empty.")

        if not name.strip():
            raise ValueError("Practitioner name cannot be empty.")

        if not specialty.strip():
            raise ValueError("Practitioner specialty cannot be empty.")

        if not availability.strip():
            raise ValueError("Practitioner availability cannot be empty.")

        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty
        self.availability = availability

    def update_information(self, name: str, specialty: str) -> None:
        
        if not name.strip():
            raise ValueError("Practitioner name cannot be empty.")

        if not specialty.strip():
            raise ValueError("Practitioner specialty cannot be empty.")

        self.name = name
        self.specialty = specialty

    def update_availability(self, availability: str) -> None:
        """Update the practitioner's availability."""
        if not availability.strip():
            raise ValueError("Practitioner availability cannot be empty.")

        self.availability = availability


class Appointment:
    

    def __init__(
        self,
        patient: Patient,
        practitioner: Practitioner,
        appointment_time: str,
        status: AppointmentStatus
    ) -> None:
       
        if not appointment_time.strip():
            raise ValueError("Appointment time cannot be empty.")

        if not isinstance(status, AppointmentStatus):
            raise ValueError("Appointment status must be an AppointmentStatus.")

        self.patient = patient
        self.practitioner = practitioner
        self.appointment_time = appointment_time
        self._status = status

    @property
    def status(self) -> AppointmentStatus:
        
        return self._status

    def cancel(self) -> None:
        
        if self._status == AppointmentStatus.CANCELLED:
            raise InvalidAppointmentStateError(
                "Appointment has already been cancelled."
            )

        self._status = AppointmentStatus.CANCELLED


def main() -> None:
    

    patient = Patient("P001", "Alice Smith")

    practitioner = Practitioner(
        "PR001",
        "Dr John Doe",
        "General Practice",
        "Monday to Friday"
    )

    appointment = Appointment(
        patient,
        practitioner,
        "2026-09-02 10:00 AM",
        AppointmentStatus.SCHEDULED
    )

    print("SmartCare v0.4 Stage 4 verification")
    print("Valid objects created successfully")
    print("Patient:", patient.patient_id)
    print("Practitioner:", practitioner.name)
    print("Appointment status:", appointment.status.value)

    try:
        Patient("", "Alice Smith")
    except ValueError:
        print("Invalid input rejected")

    appointment.cancel()

    assert appointment.status == AppointmentStatus.CANCELLED
    assert appointment.patient is patient
    assert appointment.practitioner is practitioner

    print("Scheduled appointment cancelled")
    print("Appointment object retained")
    print("Appointment status:", appointment.status.value)

    try:
        appointment.cancel()
    except InvalidAppointmentStateError:
        print("Second cancellation attempt rejected")


if __name__ == "__main__":
    main()
