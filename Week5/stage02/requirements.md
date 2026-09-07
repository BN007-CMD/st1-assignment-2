# SmartCare v0.2 - Requirements Specification

## 1. Problem and Scope

### Problem

SmartCare Community Clinic currently manages patient information and appointments using spreadsheets, paper records and manual processes. This creates several operational problems, including duplicate appointment bookings, difficulty locating patient information, inconsistent appointment status information, limited visibility of practitioner availability, manual cancellation processes and unreliable appointment history. Management wants a small and maintainable software system to improve the management of patients, practitioners and appointments while remaining appropriate for a small community clinic.

### Scope

The first version of SmartCare will provide basic functionality for managing patient, practitioner and appointment information. The system will support clinic staff in recording and locating patient information, managing practitioner information and availability, creating and managing appointments, maintaining appointment status and retaining appointment history.

The system will be designed as a manageable clinic application rather than a complex hospital information system.

## 2. Stakeholders

| Stakeholder            | Need                                                                   | Evidence                                                                                                                                         |
| ---------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Reception/Clinic Staff | Manage patient information and create, update and cancel appointments. | The clinic currently relies on spreadsheets, paper records and manual processes, which contribute to appointment and record-management problems. |
| Practitioners (GPs)    | View their appointment schedule and availability.                      | The case study identifies limited visibility of practitioner availability as an operational problem.                                             |
| Clinic Management      | Obtain reliable appointment information and basic operational reports. | The case study identifies difficulty producing basic operational reports and management wants improved clinic processes.                         |
| Patients               | Have appointments recorded accurately and avoid conflicting bookings.  | Duplicate appointment bookings are identified as an existing clinic problem.                                                                     |

### System Users and Affected Stakeholders

Reception/clinic staff and practitioners are the primary users of the proposed system. Clinic management is a stakeholder who requires operational information and reporting. Patients are affected by the accuracy of appointment management, but the case study does not state that patients will directly access or log into the system.

## 2.1 In Scope

The following capabilities are within the scope of the initial SmartCare system:

* Managing patient information.
* Managing practitioner information.
* Recording practitioner availability.
* Creating appointments.
* Viewing appointments.
* Cancelling appointments.
* Maintaining appointment status information.
* Retaining cancelled appointments as part of appointment history.
* Searching for patient information.
* Supporting basic operational reporting about appointments.

## 2.2 Out of Scope

The following are outside the scope of the initial SmartCare system:

* Patient self-service login or patient portal functionality.
* Online payments.
* Insurance processing.
* AI diagnosis or treatment recommendations.
* Automatic treatment-plan generation.
* Facial-recognition authentication.
* Complex hospital information-system functionality.
* Advanced clinical decision support.
* Integration with external healthcare systems.

## 2.3 Provisional Features

The following features are treated as provisional because the case study indicates a need for them but does not provide enough detail to define their exact behaviour:

* The specific patient information that must be stored.
* The specific practitioner information that must be stored, including whether specialty is required.
* The exact practitioner availability rules.
* The appointment statuses and allowed status transitions.
* The exact rules for preventing duplicate appointments.
* The content and format of basic operational reports.
* The method used to uniquely identify patients and practitioners.
* Whether practitioner access requires authentication or authorisation.

These provisional items are not treated as fully confirmed requirements and will be clarified before they are relied upon for detailed implementation decisions.

## 3. Functional Requirements

### Patient Management

**FR-01:** The system shall allow clinic staff to create a patient record containing the required patient information.

**FR-02:** The system shall allow clinic staff to search for a patient record using a patient identifier.

**FR-03:** The system shall allow clinic staff to update patient information stored in a patient record.

### Practitioner Management

**FR-04:** The system shall allow clinic staff to create and maintain practitioner records containing the required practitioner information.

**FR-05:** The system shall allow clinic staff to record and update practitioner availability.

**FR-06:** The system shall allow practitioners to view their scheduled appointments.

### Appointment Management

**FR-07:** The system shall allow clinic staff to create an appointment by selecting a patient, practitioner and appointment time.

**FR-08:** The system shall prevent an appointment from being created when the selected practitioner is already booked for the same appointment time.

**FR-09:** The system shall allow clinic staff to view appointment details, including the patient, practitioner, appointment time and appointment status.

**FR-10:** The system shall allow clinic staff to cancel a scheduled appointment.

**FR-11:** The system shall retain cancelled appointments in the appointment history rather than deleting them.

**FR-12:** The system shall allow clinic staff to retrieve appointment information for basic operational reporting.

> **Note:** The exact meaning of patient information, practitioner information, patient and practitioner identifiers, appointment status, duplicate bookings, practitioner availability and reporting remains subject to client clarification.

## 4. Non-Functional Requirements

### NFR-01: Reliability

The system shall maintain appointment information consistently when appointments are created, viewed or cancelled, so that an appointment's recorded status and details remain consistent.

### NFR-02: Data Integrity

The system shall prevent invalid appointment records from being created when required information is missing and shall prevent a practitioner from being booked for two appointments at the same time.

### NFR-03: Usability

The system shall provide clear prompts, messages and outputs so that clinic staff can perform the supported patient, practitioner and appointment tasks without needing to understand the underlying Python implementation.

### NFR-04: Maintainability

The domain logic shall be organised into clear responsibilities for patients, practitioners and appointments so that individual components can be understood, tested and modified without unnecessary dependencies.

### NFR-05: Testability

Core business logic shall be implemented so that patient, practitioner and appointment behaviour can be tested independently using normal and invalid inputs.

### NFR-06: Simplicity

The system shall remain limited to the confirmed SmartCare scope and shall not introduce unnecessary external services, complex infrastructure or unsupported features.

> **Engineering note:** NFR-04 to NFR-06 are treated as engineering and design constraints supporting the assignment and maintainability goals, rather than assumptions that the client explicitly requested a particular implementation.

## 5. User Stories

**US-01:** As a receptionist, I want to create and update patient records so that patient information can be maintained without relying on paper records or separate spreadsheets.

**US-02:** As a receptionist, I want to search for a patient using their identifier so that I can locate patient information efficiently.

**US-03:** As a receptionist, I want to create an appointment for a patient with a practitioner at a specific time so that appointments can be recorded consistently.

**US-04:** As a receptionist, I want the system to prevent a practitioner from being booked for two appointments at the same time so that duplicate appointment bookings are avoided.

**US-05:** As a practitioner, I want to view my scheduled appointments so that I can see my current appointment schedule.

**US-06:** As a receptionist, I want to cancel an appointment without deleting its history so that cancelled appointments remain available for future reference and reporting.

## 6. Acceptance Criteria

### US-01: Create a Patient Record

**Scenario 1: Valid patient record**

**GIVEN** a receptionist has entered all required patient information

**WHEN** the receptionist submits the new patient record

**THEN** the system shall create and store the patient record.

**Scenario 2: Missing required patient information**

**GIVEN** a receptionist has not entered a required patient field

**WHEN** the receptionist attempts to create the patient record

**THEN** the system shall reject the record and indicate that the required information is missing.

### US-02: Search for a Patient

**Scenario 1: Patient identifier exists**

**GIVEN** a patient record exists with the entered patient identifier

**WHEN** the receptionist searches using that identifier

**THEN** the system shall display the matching patient record.

**Scenario 2: Patient identifier does not exist**

**GIVEN** no patient record exists with the entered patient identifier

**WHEN** the receptionist searches using that identifier

**THEN** the system shall indicate that no matching patient record was found.

### US-03: Create an Appointment

**Scenario 1: Valid appointment**

**GIVEN** a valid patient and practitioner have been selected

**WHEN** the receptionist creates the appointment using a valid appointment time

**THEN** the system shall create the appointment with a scheduled status.

**Scenario 2: Practitioner already booked**

**GIVEN** the selected practitioner already has an appointment at the selected time

**WHEN** the receptionist attempts to create another appointment for that practitioner and time

**THEN** the system shall reject the new appointment.

> The exact rules for practitioner availability and overlapping appointments remain open questions and are not assumed here.

### US-04: Prevent Duplicate Practitioner Booking

**Scenario 1: Practitioner is already booked**

**GIVEN** a practitioner already has an appointment at the selected time

**WHEN** a receptionist attempts to create another appointment for the same practitioner and time

**THEN** the system shall reject the new appointment.

**Scenario 2: Different practitioner**

**GIVEN** the selected practitioner has no appointment at the selected time

**WHEN** the receptionist creates the appointment

**THEN** the system shall allow the appointment to be created.

### US-05: View Practitioner Appointments

**Scenario 1: Practitioner has scheduled appointments**

**GIVEN** a practitioner has one or more scheduled appointments

**WHEN** the practitioner views their appointments

**THEN** the system shall display their scheduled appointments.

### US-06: Cancel an Appointment

**Scenario 1: Scheduled appointment**

**GIVEN** an appointment has a scheduled status

**WHEN** the receptionist cancels the appointment

**THEN** the system shall change the appointment status to cancelled and retain the appointment in the history.

**Scenario 2: Already cancelled appointment**

**GIVEN** an appointment already has a cancelled status

**WHEN** the receptionist attempts to cancel the appointment again

**THEN** the system shall reject the invalid status transition and leave the appointment status unchanged.

## 7. Assumptions and Open Questions

### Assumptions

The following assumptions are being made for the initial requirements specification:

1. Reception or clinic staff are responsible for creating, updating and cancelling patient and appointment records.
2. Practitioners need to view their own scheduled appointments but do not require patient self-service functionality.
3. An appointment is associated with one patient, one practitioner and one appointment time.
4. A practitioner cannot have two appointments scheduled for the same time.
5. Cancelled appointments should remain stored so that they can contribute to appointment history and reporting.
6. The initial prototype will focus on application-level data structures and domain logic rather than requiring database or external-service implementation.

### Open Questions

The following questions should be clarified with the client before the requirements are considered fully confirmed:

1. What specific information must be stored for each patient?
2. What specific information must be stored for each practitioner?
3. What unique identifier format should be used for patients and practitioners?
4. What appointment statuses are required besides scheduled and cancelled?
5. Can appointments be rescheduled, or must an existing appointment be cancelled and a new one created?
6. What rules determine when a practitioner is available for appointments?
7. Should the system prevent appointments outside a practitioner's recorded availability?
8. What information should be included in the basic operational reports?
9. Which staff members are authorised to view or modify patient and appointment information?
10. Is persistent storage required for the initial version, or is application-level storage sufficient?

## 8. AI Requirements Review Record

Microsoft Copilot was used as a requirements reviewer after the initial requirements specification was completed. The AI was instructed to identify ambiguity, inconsistency, missing clarification questions and testability issues without inventing new client requirements.

The AI suggestions were compared against the SmartCare case study and the existing requirements. Suggestions were not automatically accepted.

### Accepted Suggestions

| AI suggestion                                                                    | Evidence                                                                                                                       | Decision | Reason                                                                                                                  |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------- | ----------------------------------------------------------------------------------------------------------------------- |
| "Required patient information" is undefined.                                     | The requirements use the term but the exact patient fields have not been provided.                                             | Accepted | The required patient fields need to be confirmed before this requirement can be implemented precisely.                  |
| Practitioner availability is not sufficiently defined.                           | The case study identifies limited visibility of practitioner availability, but the exact availability rules are not specified. | Accepted | The need is supported, but the rules for determining availability remain an open question.                              |
| "Same appointment time" may be ambiguous.                                        | The requirement does not define appointment duration or overlapping appointments.                                              | Accepted | The current requirement addresses identical times, while overlap rules require clarification.                           |
| Appointment statuses are underdefined.                                           | The case study identifies inconsistent appointment status information but does not define the complete set of statuses.        | Accepted | Scheduled and cancelled are currently used, but additional statuses and transitions require validation.                 |
| The duplicate booking requirement may not define exactly what "duplicate" means. | Duplicate bookings are identified as a problem, but the exact meaning is unclear.                                              | Accepted | The requirement currently focuses on practitioner double-booking while the broader definition remains an open question. |
| Some requirements have no corresponding acceptance criteria.                     | FR-03, FR-04, FR-05, FR-06, FR-09 and FR-12 were not originally covered.                                                       | Accepted | This is a genuine testability gap that should be addressed as the specification develops.                               |

### Modified Suggestions

| AI suggestion                                                           | Evidence                                                                                                           | Decision | Reason                                                                                                                                  |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| "Authorised clinic staff" may introduce unsupported access control.     | The provided case study does not establish authentication or permissions.                                          | Modified | Staff are recognised users, but the system should not assume a particular authentication or authorisation mechanism without validation. |
| NFR-04, NFR-05 and NFR-06 are partly design or development constraints. | These requirements describe maintainability, testability and simplicity rather than specific clinic functionality. | Modified | They remain useful engineering constraints but are not presented as explicit client requests.                                           |

### Rejected Suggestions

| AI suggestion                                                                  | Evidence                                                                     | Decision | Reason                                                                                                                   |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| The system should send SMS appointment reminders.                              | No evidence in the case study.                                               | Rejected | This would introduce a new feature that the client has not requested.                                                    |
| Facial recognition, AI diagnosis or treatment recommendations should be added. | No evidence in the case study and inconsistent with the small initial scope. | Rejected | These features are outside the intended scope.                                                                           |
| A database should be required immediately.                                     | No evidence establishes a specific database requirement for this stage.      | Rejected | Persistent storage may be appropriate later, but the current stage does not establish a database technology requirement. |

### AI Review Decision Summary

The review identified genuine weaknesses, particularly ambiguity around patient information, practitioner availability, appointment status and duplicate bookings. These suggestions were accepted because they identify information that is genuinely missing from the current specification.

Some suggestions were modified rather than accepted unchanged. In particular, the use of "authorised clinic staff" could imply an authentication or access-control system that has not been established by the client. Similarly, some non-functional requirements describe good engineering practices rather than explicit client requirements.

Suggestions for additional features such as SMS reminders, facial recognition and AI diagnosis were rejected because they were not supported by the case study and would unnecessarily expand the scope.

The review helped identify weaknesses in the requirements without allowing the AI to define the requirements itself.
