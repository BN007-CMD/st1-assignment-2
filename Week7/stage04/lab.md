# SmartCare v0.4 - Stage 4 Lab

## A. Revisit Approved UML

Before implementing the domain classes, the Stage 3 UML and requirements were reviewed.

The approved model contains:

- `Patient`
- `Practitioner`
- `Appointment`
- `AppointmentStatus`

The main relationships remain:

- One Patient can have zero or many Appointments.
- One Practitioner can have zero or many Appointments.
- Each Appointment has one Patient.
- Each Appointment has one Practitioner.
- Each Appointment has one AppointmentStatus.

The Stage 3 Practitioner model used a general `practitioner_information` attribute. The Week 7 lab specifically requires an identifier, name and specialty. The implementation therefore refines this into:

- `practitioner_id`
- `name`
- `specialty`
- `availability`

Availability has been retained because FR-05 requires practitioner availability to be recorded and updated.

The main Stage 4 change to Appointment is that its status must be protected. The status is stored privately and can only be changed through the `cancel()` operation.

The responsibilities remain with the domain objects rather than being moved into manager, service or controller classes.

---

## B. Implement Patient: AI OFF

Patient was implemented manually without using AI to generate the code.

The implementation includes:

- a typed `patient_id`
- patient information
- validation for required values
- `update_information()`
- type hints for parameters and return values

The constructor rejects a missing or empty patient identifier and patient information.

The update operation also checks that new patient information is not empty before changing the stored value.

This follows the Stage 4 requirement for basic validation while keeping the Patient class responsible for its own information.

**AI status: OFF**

No AI-generated code was used for the Patient implementation.

---

## C. Implement Practitioner: AI OFF

Practitioner was also implemented manually without using AI to generate the code.

The implementation contains:

- `practitioner_id`
- `name`
- `specialty`
- `availability`
- `update_information()`
- `update_availability()`

The constructor validates that the required practitioner values are present and non-empty.

The `update_information()` method allows the practitioner's name and specialty to be updated. The `update_availability()` method handles changes to practitioner availability.

No database logic was added.

The availability attribute was retained from the Stage 3 model because FR-05 explicitly requires practitioner availability. The generic `practitioner_information` attribute was replaced with the more specific `name` and `specialty` requested by the Week 7 lab.

**AI status: OFF**

No AI-generated code was used for the Practitioner implementation.

---

## D. Implement Appointment: AI ON

The Appointment implementation was completed with AI used as a Python pair programmer.

The AI was given the approved Appointment design and the Stage 4 constraints. The AI was instructed to implement only the Appointment class and the agreed `AppointmentStatus` enum and exception.

The prompt used was:

> Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML.

The generated implementation was required to:

- use type hints
- use `AppointmentStatus`
- store the appointment's patient, practitioner and appointment time
- protect the appointment status
- expose status through a read-only property
- change status through `cancel()`
- prevent a cancelled appointment from being cancelled again
- use a custom exception for the illegal repeated transition
- retain cancelled appointments as objects

**AI status: ON**

AI was used only for the Appointment-related implementation described above.

---

## E. Review Generated Code

The generated Appointment code was reviewed against the approved UML, the SmartCare requirements and the Stage 4 constraints.

The review checked for the following:

### Model consistency

The Appointment class still represents the same concept from the Stage 3 model. It contains a Patient, Practitioner, appointment time and appointment status.

### Unsupported features

No database, UI, notification or service classes were added.

### Public state mutation

The appointment status is not exposed as a public mutable attribute. It is stored using `_status` and accessed through a read-only `status` property.

### Unnecessary inheritance

Appointment does not inherit from Patient or Practitioner. The relationships remain associations, consistent with the Stage 3 UML.

### Invented dependencies

No `AppointmentManager`, `NotificationManager`, `ScheduleEngine` or other unsupported dependency was added.

### Error handling

The implementation raises `InvalidAppointmentStateError` when `cancel()` is called on an appointment that is already cancelled.

Constructor validation also rejects invalid required values.

The generated code was reviewed and simplified where necessary so that the final implementation remained focused on the approved SmartCare design.

---

## F. Manual Behaviour Checks

Manual checks were performed after the implementation was completed.

### Check 1: Valid objects

A valid Patient, Practitioner and Appointment were created using valid values.

The objects were created successfully and the Appointment initially had the status `SCHEDULED`.

### Check 2: Invalid input

Invalid input was tested using an empty required value.

The implementation rejected the invalid input by raising `ValueError`.

### Check 3: Appointment cancellation

A scheduled Appointment was cancelled using the `cancel()` method.

The status changed from `SCHEDULED` to `CANCELLED`.

The Appointment object was retained, including its Patient and Practitioner references. This is consistent with FR-11, which requires cancelled appointments to remain in appointment history rather than being deleted.

### Check 4: Repeated cancellation

The same Appointment was passed to `cancel()` a second time.

The implementation rejected the illegal state transition by raising `InvalidAppointmentStateError`.

The terminal output from these checks is recorded in `run_output.txt`.

---

## G. Refactor

After the behaviour checks, the implementation was reviewed for unnecessary code.

The final design was kept simple by:

- keeping responsibilities in the domain classes
- avoiding manager and service classes
- keeping database logic outside the domain layer
- using a single custom exception for the illegal appointment transition
- using a read-only property for appointment status
- keeping the Stage 3 associations between Patient, Practitioner and Appointment

No additional functionality was added beyond the Stage 4 requirements.

---

## H. AI Engineering Log

The AI was used only during Step D for the Appointment implementation.

### Prompt

The prompt used for the AI pair-programming step was:

> Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML.

### AI contribution

The AI provided an initial implementation of the Appointment class, including:

- constructor structure
- type hints
- AppointmentStatus usage
- protected `_status`
- read-only `status` property
- `cancel()` behaviour
- invalid state exception

### Review decisions

The generated code was compared with the approved UML and the Stage 4 requirements.

Any unnecessary or unsupported code was removed rather than being kept simply because it had been generated by AI.

The final implementation was kept limited to the Appointment domain behaviour and the agreed enum and exception.

### Verification evidence

The implementation was checked by running the program and performing the four required manual behaviour checks:

1. Valid objects were created successfully.
2. Invalid input was rejected.
3. A scheduled appointment was cancelled and the object remained available.
4. A second cancellation attempt was rejected with the custom exception.

The results are recorded in `run_output.txt`.

---

## Reflection

The main AI-generated part that needed careful review was the Appointment implementation, particularly the status handling.

The approved UML and the Stage 4 requirements meant that the status could not simply be left as a public mutable attribute. The implementation needed to protect the state and make `cancel()` responsible for the transition.

The AI was also constrained from adding database, notification, service or UI classes. These were deliberately excluded because they were not part of the approved domain model or the confirmed requirements.

The AI OFF and AI ON split also helped keep the design review clear. Patient and Practitioner were implemented manually, while AI was used only for Appointment. This made it possible to review the AI contribution directly against the approved design.

The approved UML therefore acted as a constraint on the AI rather than allowing the AI to redesign the SmartCare domain model.
