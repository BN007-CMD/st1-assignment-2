# AI Usage

## AI Tool

Microsoft Copilot was used as a Python tutor and to generate an alternative appointment-booking function.

## AI Tutor Activity

I asked the AI to explain my appointment-booking code, identify three limitations, suggest improvements and ask questions to test my understanding. I asked it not to rewrite the whole application.

The AI helped me understand how a function can create an appointment dictionary and add that dictionary to an appointments list.

## AI Suggestions

The AI suggested:

- Adding appointment conflict checking.
- Improving input validation.
- Using `datetime` for appointment times.
- Removing duplicated initial data.
- Adding data persistence later.

I evaluated these suggestions rather than automatically accepting them.

## Evaluation

- Conflict checking: Useful, but not implemented in this prototype.
- Input validation: Useful. I implemented a check for a blank patient name in my human version.
- `datetime`: Useful, but not required at this stage.
- Removing duplicated data: Useful. My human version does not use the duplicated tutorial data.
- Data persistence: Useful for a future version, but not required at this stage.

## AI-Generated Alternative

I asked the AI to create a beginner-friendly Python function that stores patient name, practitioner name and appointment time without using a database or GUI.

The AI-generated version successfully stored a normal appointment.

## Verification

I tested the AI-generated version with:

1. A normal appointment.
2. A blank patient name.
3. Two appointments using the same practitioner and time.
4. `None` as a patient name.

The AI version accepted the blank patient name, allowed duplicate bookings and accepted `None`.

This demonstrated that AI-generated code should be tested and evaluated rather than automatically treated as correct.

