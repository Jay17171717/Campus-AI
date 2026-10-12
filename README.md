# Campus AI
#### Video Demo: <https://www.youtube.com/watch?v=w8fibU1fSjI>

## Description

Campus AI is a Python-based student assistant designed to make common campus-related tasks easier and more convenient. The application was developed as my final project for CS50's Introduction to Programming with Python.

The project uses Streamlit to provide a simple graphical web interface. Instead of requiring users to interact with the program through a terminal, students can select different features from a sidebar and enter information through buttons, text boxes, and number inputs.

Campus AI includes an AI-style campus assistant, an attendance calculator, a CGPA calculator, a campus location search system, and an important contacts section.

## AI Assistant

The Campus AI Assistant is a rule-based assistant that allows students to ask common campus-related questions. It processes the user's question and identifies keywords such as attendance, CGPA, library, canteen, laboratory, office, placement, and emergency.

Based on the detected keyword, the assistant provides an appropriate response or uses other functions in the project to retrieve information.

The assistant is rule-based and does not use an external generative AI API.

## Attendance Calculator

The attendance calculator allows a student to enter the number of classes attended and the total number of classes conducted.

The program calculates the attendance percentage and also provides advice based on a 75 percent attendance requirement. If the student's attendance is below the threshold, the program calculates how many consecutive classes need to be attended to reach 75 percent. If the attendance is above the threshold, it estimates how many classes can be missed while remaining at or above the required percentage.

Invalid values, such as zero total classes, negative numbers, or attended classes greater than total classes, are handled using exceptions.

## CGPA Calculator

The CGPA calculator accepts grade points separated by commas. Students can optionally enter the number of credits for each course.

Without credits, the program calculates a normal average of the grade points. When credits are provided, it calculates a credit-weighted CGPA.

The program validates grade points and ensures that they are between 0 and 10. It also checks that the number of credits matches the number of grades.

## Campus Search

The Campus Search feature helps users find common locations such as the library, canteen, computer laboratory, and administrative office.

The program converts the search query to lowercase and checks it for known location keywords. This means a student can enter a simple word such as "library" or a sentence such as "Where is the library?"

## Important Contacts

The Important Contacts section allows students to select a department and retrieve its contact information.

The current project contains demonstration contact information for the office, library, placement department, and emergency services. Placeholder contact details should be replaced with verified campus information before real-world use.

## Files

`project.py` contains the main application, Streamlit interface, and the functions responsible for the project's logic.

`test_project.py` contains pytest tests for the project's functions, including attendance calculations, CGPA calculations, campus searching, contact retrieval, number parsing, attendance advice, and the campus assistant.

`requirements.txt` lists the Python packages required to run and test the project.

`README.md` contains the documentation and explanation of the project.

## Running the Project

Install the required packages using:

pip install -r requirements.txt

Then run the Streamlit application using:

streamlit run project.py

The automated tests can be run using:

pytest test_project.py

## Design Decisions

I chose Streamlit because it allowed me to build a simple interactive interface while keeping the main project written in Python. I separated the calculation and search logic into individual functions so that each component could be tested independently using pytest.

I also chose to make the Campus AI Assistant rule-based rather than depend on an external AI service. This keeps the project self-contained and allows it to work without an API key.

In the future, Campus AI could be expanded with verified college data, timetables, announcements, student schedules, additional campus locations, and a generative AI service.
