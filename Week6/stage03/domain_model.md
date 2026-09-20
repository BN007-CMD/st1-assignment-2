# SmartCare v0.3 Domain Model

## Requirement-to-Concept Trace

The following table maps each functional requirement from SmartCare v0.2 to the domain concept that supports it.

| Requirement | Concept | State / Behaviour | Decision |
|---|---|---|---|
| FR-01 | Patient | Stores the patient identifier and required patient information. | Include Patient as a core domain class. |
| FR-02 | Patient | Stores a patient identifier that can be used to locate the patient record. | Keep the identifier as part of Patient. |
| FR-03 | Patient | Patient information can be updated. | Include update_information() in Patient. |
| FR-04 | Practitioner | Stores the practitioner identifier and required practitioner information. | Include Practitioner as a core domain class. |
| FR-05 | Practitioner | Stores practitioner availability and supports updating it. | Include availability in Practitioner and add update_availability(). |
| FR-06 | Practitioner / Appointment | A practitioner is associated with their scheduled appointments. | Link Practitioner to Appointment using an association. |
| FR-07 | Appointment | Stores a patient, practitioner and appointment time. | Include Appointment as a core domain class with these attributes. |
| FR-08 | Appointment / Practitioner | A practitioner cannot have two appointments at the same time. | Represent this as a business rule involving Appointment and Practitioner. Full checking is left for Stage 4. |
| FR-09 | Appointment | Stores appointment details and appointment status. | Include patient, practitioner, appointment time and status in Appointment. |
| FR-10 | Appointment | An appointment can be cancelled. | Include cancel() in Appointment. The actual status change is left for Stage 4. |
| FR-11 | Appointment | Cancelled appointments remain part of the appointment history. | Keep cancelled appointments as Appointment objects rather than deleting them. |
| FR-12 | Appointment | Appointment information can be retrieved for basic operational reporting. | Keep appointment information together in Appointment. Detailed reporting behaviour is outside the Stage 3 domain model. |

## CRC Cards

### Patient

#### Responsibilities

- Represent a patient record.
- Store the patient identifier.
- Store the required patient information.
- Support updating patient information.

#### Collaborators

- Appointment

### Practitioner

#### Responsibilities

- Represent a practitioner record.
- Store the practitioner identifier.
- Store the required practitioner information.
- Represent practitioner availability.
- Support updating practitioner information.
- Support updating practitioner availability.

#### Collaborators

- Appointment

### Appointment

#### Responsibilities

- Represent an appointment.
- Store the patient associated with the appointment.
- Store the practitioner associated with the appointment.
- Store the appointment time.
- Store the appointment status.
- Represent appointment cancellation.
- Retain the appointment when it is cancelled.

#### Collaborators

- Patient
- Practitioner
- AppointmentStatus

### AppointmentStatus

#### Responsibilities

- Represent the current status of an appointment.
- Provide the status values used by the Stage 3 model.

#### Collaborators

- Appointment

AppointmentStatus is included as the optional supporting concept for the fourth CRC card. It is an enumeration rather than a normal domain class.

The initial confirmed statuses are:

- SCHEDULED
- CANCELLED

Additional statuses have not been added because Stage 2 identified the complete list of appointment statuses as an open question.

## UML Class Diagram

The UML class diagram for the SmartCare domain model is stored as a separate image file and embedded below.

![SmartCare v0.3 UML Class Diagram](uml.png)

The diagram shows:

- Patient
- Practitioner
- Appointment
- AppointmentStatus

The main associations are:

- One Patient can have zero or many Appointment objects.
- One Practitioner can have zero or many Appointment objects.
- Each Appointment is associated with exactly one Patient.
- Each Appointment is associated with exactly one Practitioner.
- Each Appointment has one AppointmentStatus.

## Design Rationale

### Class Selection

The final model contains Patient, Practitioner and Appointment as the main domain classes.

Patient is included because the requirements involve creating, searching and updating patient records.

Practitioner is included because the requirements involve practitioner information, practitioner availability and viewing scheduled appointments.

Appointment is included because appointments are the main interaction between patients and practitioners. The requirements require appointments to store information about the patient, practitioner, time and status.

AppointmentStatus is represented as an enumeration because status is part of an appointment rather than an independent object with its own responsibilities.

### Responsibility Allocation

The responsibilities have been kept with the domain concepts they relate to.

Patient is responsible for patient information.

Practitioner is responsible for practitioner information and availability.

Appointment is responsible for appointment information and its status.

This avoids creating extra manager classes when the requirements do not require them.

### Key Relationships

A Patient can have zero or many appointments, while each Appointment is associated with exactly one Patient.

`Patient "1" -------- "0..*" Appointment`

A Practitioner can have zero or many appointments, while each Appointment is associated with exactly one Practitioner.

`Practitioner "1" -------- "0..*" Appointment`

These are associations rather than inheritance relationships. An Appointment is not a type of Patient or Practitioner.

The duplicate booking rule in FR-08 is treated as a business rule involving appointments and practitioners. It does not require a separate ScheduleEngine class.

## Concepts Deliberately Excluded

Several candidate concepts were considered but were not included as domain classes.

Name was excluded because it is information belonging to a Patient or Practitioner.

Clinic was excluded because the requirements do not give it separate responsibilities.

Database was excluded because database technology is an implementation concern rather than a domain concept required at this stage.

Cancellation was excluded because cancellation is an action or change to an Appointment.

Status was not created as a separate class because appointment status belongs to Appointment. It is represented using AppointmentStatus.

The following AI-suggested classes were also not added:

- PatientManager
- PractitionerManager
- AppointmentManager
- ClinicController
- NotificationManager
- ScheduleEngine

These suggestions either introduced application-level structure or functionality that was not supported by the confirmed requirements.

## AI Design Review Record

The AI design review was completed using the confirmed SmartCare v0.2 requirements. The AI was instructed to cite requirement IDs and not introduce unsupported functionality.

| Suggestion | Evidence | Decision | Reason | Model Change |
|---|---|---|---|---|
| Use AppointmentStatus to represent appointment status. | FR-09, FR-10, FR-11 | Accepted | Appointment status is directly required. An enumeration keeps the representation simple without creating a separate Status class. | Added AppointmentStatus to the model with SCHEDULED and CANCELLED. |
| Store practitioner availability in Practitioner. | FR-05 | Accepted | Practitioner availability is directly identified as a requirement. It belongs with the Practitioner concept. | Added availability and update_availability() to Practitioner. |
| Add an AppointmentManager class. | FR-07, FR-08, FR-09, FR-12 | Modified | Appointment management is required, but a separate manager is not required by the case study. | Appointment remains the main domain concept. No AppointmentManager class was added. |
| Add a NotificationManager class. | No supporting FR | Rejected | There is no confirmed requirement for appointment notifications or reminders. | No change to the model. |
| Add a Clinic class that owns all patients, practitioners and appointments. | No supporting FR | Rejected | The clinic is part of the case study context, but the requirements do not give Clinic separate responsibilities or behaviour. | No Clinic class was added. |

## Final Model

The final Stage 3 domain model is intentionally small.

The main model elements are:

- Patient
- Practitioner
- Appointment
- AppointmentStatus

The main relationships are:

- Patient `1` to Appointment `0..*`
- Practitioner `1` to Appointment `0..*`
- Appointment has one Patient.
- Appointment has one Practitioner.
- Appointment has one AppointmentStatus.

The model is based on the confirmed requirements from Stage 2 and avoids adding unsupported functionality.

The Python implementation in `smartcare_v03.py` will use the same classes, attributes and operations shown in the UML diagram.

Working validation, duplicate booking checks and appointment status transitions are not implemented in Stage 3. These behaviours will be addressed during Stage 4.
