# Human vs AI Comparison

| Question | Human version | AI version |
|---|---|---|
| Easy to understand? | Yes. I built it step by step using a list, dictionary and function. | Yes. The AI version was short and simple. |
| Runs successfully? | Yes. I tested it and it worked. | Yes. The normal appointment test worked. |
| Uses only required features? | Yes. It stores patient, practitioner and appointment time. | Yes. It stores patient, practitioner and appointment time. |
| Adds assumptions? | No major assumptions. | No major assumptions. |
| Handles errors? | Yes. It rejects a blank patient name. | No. It accepted a blank patient name and `None`. |
| Could I explain it? | Yes. I built and tested the code myself. | Yes, after reviewing and testing the AI-generated code. |

## AI Suggestions

| Suggestion | Decision |
|---|---|
| Appointment conflict checking | Useful, but not implemented yet. |
| Better input validation | Useful. I implemented validation for a blank patient name in my human version. |
| Use `datetime` objects | Useful, but not required for this prototype. |
| Remove duplicated initial data | Useful. My human version does not use the duplicated tutorial data. |
| Save appointments to a file/JSON | Useful for a future version, but not required at this stage. |

## Testing the AI Version

### Normal appointment

The AI version successfully stored and displayed a normal appointment.

### Blank patient name

The AI version accepted a blank patient name instead of rejecting it.

### Duplicate appointment

The AI version allowed two patients to book the same practitioner at the same time.

### Strange input

The AI version accepted `None` as a patient name.

## Overall Decision

The human version was more suitable for this prototype because it included basic validation and I could explain how it worked. The AI version was useful as an alternative and helped identify possible improvements, but testing showed that its output was not automatically correct.

