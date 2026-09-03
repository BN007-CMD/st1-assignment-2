
print("Welcome to SmartCare")


appointments = []

def book_appointment(patient, practitioner, time):
    if not patient:
        raise ValueError("Patient name cannot be empty")

    appointment = {
        "patient": patient,
        "practitioner": practitioner,
        "time": time
    }
    appointments.append(appointment)

book_appointment(
    "Alice Smith",
    "Dr. John Doe",
    "2026-09-02 10:00 AM"
)
book_appointment(
    "Bob Johnson",
    "Dr. Jane Roe",
    "2026-09-02 11:30 AM"
)

for appointment in appointments:
    print(
        f"Patient: {appointment['patient']} | "
        f"Practitioner: {appointment['practitioner']} | "
        f"Time: {appointment['time']}"
    )
