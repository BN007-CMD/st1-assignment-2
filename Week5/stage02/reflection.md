# Stage 2 Reflection

The AI requirements review helped me identify several issues that I had not noticed when I first wrote the requirements. In particular, it identified that terms such as "required patient information", "practitioner availability" and "same appointment time" were not defined clearly enough to be tested. It also identified that some of my functional requirements did not yet have corresponding acceptance criteria.

The AI also overreached in some areas. It suggested that terms such as authorised staff could imply authentication and questioned whether features such as practitioner specialty, patient identifiers and reporting were directly supported by the case study. These suggestions were useful as questions, but I did not automatically accept them as requirements. I checked them against the case study and treated uncertain areas as clarification questions or assumptions.

One important change after the review was recognising that the duplicate booking requirement needs clearer definition. The case study identifies duplicate bookings as a problem, but it does not completely explain what types of duplicate bookings must be prevented. I therefore kept the requirement focused on preventing a practitioner from having two appointments at the same time while recording the broader issue as an open question.

Requirements must have evidence because otherwise developers can build features based on assumptions rather than what the client actually needs. AI can suggest reasonable features, but reasonable does not mean required. Evidence helps keep the system within scope and makes requirements defensible and testable.

