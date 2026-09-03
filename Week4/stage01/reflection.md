# Stage 1 Reflection

Before using AI, I built my own simple Python appointment prototype. I started by identifying the information an appointment needs: a patient, practitioner and appointment time. I then created an appointments list, used dictionaries to store appointment information and created a function to book appointments. I also added basic validation so a blank patient name is rejected.

After building my version, I used Microsoft Copilot as a tutor. It helped me understand my code and suggested possible improvements such as checking for appointment conflicts, improving input validation, using datetime objects and saving appointments so they could persist.

The AI also generated an alternative appointment function. I did not assume that this code was correct. I tested the AI-generated version using a normal appointment, a blank patient name, duplicate appointments for the same practitioner and time, and None as a patient name. The tests showed that the AI version accepted invalid input and allowed duplicate bookings.

This showed me why software engineers need to evaluate and test AI-generated code. AI can produce code quickly, but it does not know all of the requirements or necessarily make the correct assumptions.

The engineering work remained with me because I had to understand the problem, build my own solution, evaluate the AI suggestions, test the code and decide which improvements were appropriate.

