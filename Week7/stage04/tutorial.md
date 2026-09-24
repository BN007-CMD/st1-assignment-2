# SmartCare v0.4 - Stage 4 Tutorial

## Activity 1: Encapsulation Review

Encapsulation means keeping important object state protected and making sure it can only be changed in controlled ways.

| Class | Protected state / invariant | Public operations |
|---|---|---|
| `Patient` | The patient identifier must be present and non-empty. Required patient information must also be present and non-empty. | `update_information()` |
| `Practitioner` | The practitioner identifier, name, specialty and availability must contain required values. Practitioner information and availability should be changed through the class operations. | `update_information()`, `update_availability()` |
| `Appointment` | An appointment must have a patient, practitioner, appointment time and valid appointment status. The status should not be changed directly from outside the class. A cancelled appointment cannot be cancelled again. | `cancel()` and the read-only `status` property |

The main example of encapsulation in this stage is the appointment status. Instead of allowing other parts of the program to directly change the status, the status will be stored in `_status`.

The current status can be read using the `status` property, but there will be no public setter. The `cancel()` method will control the change from `SCHEDULED` to `CANCELLED`.

This means the appointment itself is responsible for protecting its state.

---

## Activity 2: Composition or Inheritance?

| Relationship | Decision | Reason |
|---|---|---|
| `Appointment` ↔ `Patient` | Association | An appointment is associated with a patient. An appointment is not a type of patient, so inheritance would not make sense. |
| `Appointment` ↔ `Practitioner` | Association | An appointment is associated with a practitioner. It is not a type of practitioner, so this should remain an association. |
| `Doctor` ↔ `Practitioner` | Inheritance | A Doctor is a type of Practitioner. A Doctor could therefore inherit the common information and behaviour of a Practitioner. |
| `Clinic` ↔ `Appointment` | Association | A clinic and an appointment are separate concepts. The SmartCare requirements do not establish Clinic as a parent class of Appointment or require Clinic to be a domain class. |

The first, second and fourth relationships are associations because they describe relationships between separate concepts. The Doctor and Practitioner relationship is different because a Doctor is a specialised type of Practitioner, so inheritance is appropriate.

---

## Activity 3: Responsibility Allocation

### Who decides whether `SCHEDULED` can become `CANCELLED`?

`Appointment` should decide.

The status transition is a rule about the appointment itself. The `cancel()` method should check the current status and only allow the transition when it is valid.

If the appointment is already cancelled, the method should raise `InvalidAppointmentStateError`.

### Who validates a patient name?

The `Patient` class should handle validation of its required patient information.

This keeps the validation close to the object whose state needs to be protected. It also means that invalid patient information cannot be accepted simply because another part of the application forgot to validate it.

### Should `Appointment` execute SQL? Why?

No.

SQL is related to database persistence and is not part of the responsibility of the Appointment domain object. The Appointment class should manage appointment information and behaviour without depending on a particular database.

The Stage 4 instructions also specifically state that database logic should not be added.

### Should the UI decide whether a status transition is legal?

No.

The UI can request that an appointment be cancelled, but the Appointment object should decide whether the cancellation is allowed.

This keeps the business rule inside the domain object and means the same rule is applied regardless of where the cancellation request comes from.

---

## Activity 4: AI Code Critique

The AI-generated Appointment class in the scenario has several design problems.

| Problem | Correction |
|---|---|
| **1. Public status mutation** | Store the status in private `_status` state and provide a read-only `status` property. The `cancel()` method should control the status transition. |
| **2. SQL inside `cancel()`** | Remove the SQL. Appointment should contain domain behaviour and should not directly manage database operations. |
| **3. `NotificationManager` dependency** | Remove the dependency because appointment notifications or reminders are not part of the confirmed SmartCare requirements. |
| **4. Inheritance from `PatientRecord`** | Remove the inheritance relationship. An Appointment is associated with a Patient but is not a type of Patient. |
| **5. No protection against cancelling twice** | Check the current status in `cancel()` and raise `InvalidAppointmentStateError` if the appointment has already been cancelled. |
| **6. No constructor validation** | Validate required values when the object is created and reject missing or empty input. |
| **7. Missing type hints** | Add type hints to all parameters and return values as required by the Stage 4 implementation instructions. |

These changes keep the Appointment class consistent with the approved domain model and stop the AI from adding features or dependencies that are outside the requirements.

---

## Exit Question: Why can code be object-oriented syntactically but still have poor object-oriented design?

Code can use classes and methods and still have poor object-oriented design if the classes do not have the right responsibilities.

For example, a class might only store data while another class or the user interface performs all of its important business rules. This creates an anemic domain model. The code is technically object-oriented, but the objects do not properly manage their own state or behaviour.

This connects to the Stage 3 decision to reject unnecessary manager classes. The SmartCare design keeps responsibilities with the domain concepts they relate to.

In Stage 4, this is shown by putting the appointment cancellation rule inside `Appointment`. The Appointment class protects its own status instead of relying on the UI or another manager to decide whether a status change is allowed.

Good object-oriented design is therefore about more than simply using classes. It is about giving objects appropriate responsibilities and protecting the rules that apply to their state.
