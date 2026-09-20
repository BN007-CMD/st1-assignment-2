# SmartCare v0.3 Domain Modelling Tutorial

## Candidate Concepts

The following candidate concepts were identified from the SmartCare v0.2 requirements and reviewed to decide whether each should become a domain class.

| Candidate Concept | Class? | Reason |
|---|---|---|
| **Patient** | Yes | Patient records are directly required by FR-01, FR-02 and FR-03. |
| **Practitioner** | Yes | Practitioner records and availability are required by FR-04, FR-05 and FR-06. |
| **Appointment** | Yes | Appointment creation, viewing, cancellation, status and history are covered by FR-07 to FR-12. |
| **Name** | No | A name is information belonging to a Patient or Practitioner rather than a separate domain object. |
| **Clinic** | No | The requirements describe SmartCare as a community clinic, but do not give Clinic separate state or responsibilities. |
| **Database** | No | A database is an implementation concern and is not a confirmed domain requirement. |
| **Cancellation** | No | Cancellation is an action involving an Appointment rather than a separate domain object. |
| **Status** | No | Appointment status is part of an Appointment and is represented using the `AppointmentStatus` enumeration. |

## CRC Cards

CRC stands for **Class, Responsibilities and Collaborators**.

### Patient

**Class:** `Patient`

**Responsibilities:**

- Represent a patient record.
- Store the patient identifier.
- Store the required patient information.
- Support updating patient information.

**Collaborators:**

- `Appointment`

**Supporting requirements:**

- FR-01
- FR-02
- FR-03

### Practitioner

**Class:** `Practitioner`

**Responsibilities:**

- Represent a practitioner record.
- Store the practitioner identifier.
- Store the required practitioner information.
- Store practitioner availability.
- Support updating practitioner information.
- Support updating practitioner availability.

**Collaborators:**

- `Appointment`

**Supporting requirements:**

- FR-04
- FR-05
- FR-06

### Appointment

**Class:** `Appointment`

**Responsibilities:**

- Represent an appointment.
- Store the patient associated with the appointment.
- Store the practitioner associated with the appointment.
- Store the appointment time.
- Store the appointment status.
- Represent appointment cancellation.
- Retain the appointment as part of the appointment history.

**Collaborators:**

- `Patient`
- `Practitioner`

**Supporting requirements:**

- FR-07
- FR-08
- FR-09
- FR-10
- FR-11
- FR-12

## Relationship Reasoning

### 1. What is the relationship between Patient and Appointment?

A `Patient` can have zero or many `Appointment` objects.

Each `Appointment` is associated with exactly one `Patient`.

The relationship is:

`Patient "1" -------- "0..*" Appointment`

This is an association rather than inheritance. The relationship is supported by FR-07, which requires an appointment to be created for a selected patient, and FR-11, which requires appointments to be retained as history.

### 2. What is the multiplicity between Practitioner and Appointment?

A `Practitioner` can have zero or many appointments.

Each `Appointment` is associated with exactly one `Practitioner`.

The relationship is:

`Practitioner "1" -------- "0..*" Appointment`

This is supported by FR-06 and FR-07.

FR-08 also establishes an important business rule: a practitioner cannot have two appointments at the same time.

The detailed duplicate booking check will be implemented in Stage 4, not in the Stage 3 skeleton.

### 3. Should Appointment inherit from Patient?

No.

`Appointment` should not inherit from `Patient` because an appointment is not a type of patient.

They are separate domain concepts that are associated with each other.

The same reasoning applies to `Practitioner`. An appointment is associated with a practitioner, but it is not a type of practitioner.

### 4. Does Clinic need to own every object?

No.

The requirements do not give `Clinic` separate responsibilities or behaviour that justify making it a domain class.

The word "clinic" describes the context in which the system operates. It does not automatically need to become a class.

Adding a `Clinic` class would introduce extra structure that is not required by the confirmed requirements.

## AI Model Critique

The following possible classes were considered during the AI design review:

- `PatientManager`
- `PractitionerManager`
- `AppointmentManager`
- `ClinicController`
- `NotificationManager`
- `ScheduleEngine`

The suggestions were checked against the confirmed SmartCare requirements before making a decision.

| Proposed Class | Decision | Reason |
|---|---|---|
| `PatientManager` | Rejected | The requirements require patient management, but they do not require a separate manager class. Patient information can remain the responsibility of `Patient`. |
| `PractitionerManager` | Rejected | Practitioner information and availability are requirements, but no separate manager object is required by the case study. |
| `AppointmentManager` | Rejected | Appointment creation and duplicate checking are required by FR-07 and FR-08, but the requirements do not justify creating a separate manager class at the domain level. |
| `ClinicController` | Rejected | No confirmed requirement gives a controller separate domain responsibilities. Adding one would move the model towards application architecture rather than the required domain model. |
| `NotificationManager` | Rejected | There is no confirmed requirement for SMS, email or other appointment notifications. |
| `ScheduleEngine` | Rejected | Practitioner availability and duplicate booking are requirements, but there is no requirement for a separate scheduling engine. |

### AI Critique Conclusion

The AI suggestions were treated as design suggestions rather than requirements.

The final domain model remains deliberately small:

- `Patient`
- `Practitioner`
- `Appointment`
- `AppointmentStatus`

This keeps the model within the confirmed requirements and avoids unnecessary design complexity.
