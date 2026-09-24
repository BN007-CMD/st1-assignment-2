from enum import Enum


class AppointmentStatus(Enum):
    """Represent the status of a SmartCare appointment."""

    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"


class InvalidAppointmentStateError(Exception):
    """Raised when an appointment status transition is not permitted."""


class Patient:
    """Represent a patient record (FR-01, FR-02, FR-03)."""

    def __init__(self, patient_id: str, patient_information: str) -> None:
        """Create a patient record, rejecting missing required values."""
        if not patient_id.strip():
            raise ValueError("Patient ID cannot be empty.")

        if not patient_information.strip():
            raise ValueError("Patient information cannot be empty.")

        self.patient_id = patient_id
        self.patient_information = patient_information

    def update_information(self, patient_information: str) -> None:
        """Update the stored patient information after validating it."""
        if not patient_information.strip():
            raise ValueError("Patient information cannot be empty.")

        self.patient_information = patient_information


class Practitioner:
    """Represent a practitioner record (FR-04, FR-05, FR-06)."""

    def __init__(
        self,
        practitioner_id: str,
        name: str,
        specialty: str,
        availability: str
    ) -> None:
        """Create a practitioner record, rejecting missing required values."""
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
        """Update the practitioner's name and specialty after validating them."""
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
    """Represent an appointment (FR-07 to FR-12).

    The appointment status is protected: it is stored privately and can
    only be changed through cancel().
    """

    def __init__(
        self,
        patient: Patient,
        practitioner: Practitioner,
        appointment_time: str,
        status: AppointmentStatus
    ) -> None:
        """Create an appointment, rejecting a missing time or invalid status."""
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
        """Return the current status. Read-only: there is no public setter."""
        return self._status

    def cancel(self) -> None:
        """Cancel a scheduled appointment (FR-10).

        The appointment object is retained so it remains part of the
        appointment history (FR-11). Raises InvalidAppointmentStateError
        if the appointment has already been cancelled.
        """
        if self._status == AppointmentStatus.CANCELLED:
            raise InvalidAppointmentStateError(
                "Appointment has already been cancelled."
            )

        self._status = AppointmentStatus.CANCELLED


def main() -> None:
    """Run the four Stage 4 manual behaviour checks required by lab step F."""
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
