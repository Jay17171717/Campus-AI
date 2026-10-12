import math
import streamlit as st

ATTENDANCE_THRESHOLD = 75


def calculate_attendance(attended, total):
    if total == 0:
        raise ValueError("Total classes cannot be zero.")

    if attended < 0 or total < 0:
        raise ValueError("Values cannot be negative.")

    if attended > total:
        raise ValueError("Classes attended cannot be more than total classes.")

    return round((attended / total) * 100, 2)


def attendance_advice(attended, total, threshold=ATTENDANCE_THRESHOLD):
    if total == 0:
        raise ValueError("Total classes cannot be zero.")

    if attended < 0 or total < 0:
        raise ValueError("Values cannot be negative.")

    if attended > total:
        raise ValueError("Classes attended cannot be more than total classes.")

    percentage = (attended / total) * 100

    if percentage < threshold:
        t = threshold / 100
        needed = math.ceil((t * total - attended) / (1 - t))

        return (
            f"Attend the next {needed} class(es) in a row "
            f"to reach {threshold}%."
        )

    can_miss = math.floor(
        attended / (threshold / 100) - total
    )

    if can_miss > 0:
        return (
            f"You can miss up to {can_miss} class(es) "
            f"and stay at {threshold}% or above."
        )

    return (
        f"You are right at the {threshold}% limit. "
        "Try not to miss any class."
    )


def calculate_cgpa(grades, credits=None):
    if len(grades) == 0:
        raise ValueError("Grades cannot be empty.")

    for grade in grades:
        if math.isnan(grade) or grade < 0 or grade > 10:
            raise ValueError("Grades must be between 0 and 10.")

    if credits is None:
        return round(sum(grades) / len(grades), 2)

    if len(credits) != len(grades):
        raise ValueError(
            "Number of credits must match number of grades."
        )

    for credit in credits:
        if math.isnan(credit) or credit <= 0:
            raise ValueError("Credits must be positive numbers.")

    weighted_sum = sum(
        grade * credit
        for grade, credit in zip(grades, credits)
    )

    return round(weighted_sum / sum(credits), 2)


def parse_numbers(text):
    return [
        float(part)
        for part in text.split(",")
        if part.strip()
    ]


def search_campus(query):
    campus_locations = {
        "library": (
            "The library is located in the main academic block."
        ),
        "canteen": (
            "The canteen is located near the main campus area."
        ),
        "lab": (
            "The computer labs are located in the academic block."
        ),
        "office": (
            "The administrative office is located in the main block."
        ),
    }

    query = query.strip().lower()

    if not query:
        return "Please enter a location to search."

    for name, description in campus_locations.items():
        if name in query:
            return description

    return "Location not found."


def get_contact(department):
    contacts = {
        "office": "0422-1234567",
        "library": "0422-2345678",
        "placement": "0422-3456789",
        "emergency": "112",
    }

    return contacts.get(
        department.strip().lower(),
        "Contact not found."
    )


def campus_assistant(question):
    question = question.strip().lower()

    if not question:
        return "Please ask me a question."

    if "attendance" in question:
        return (
            "You can use the Attendance Calculator to calculate "
            "your attendance percentage and get attendance advice."
        )

    if "cgpa" in question or "grade" in question:
        return (
            "You can use the CGPA Calculator to calculate your "
            "CGPA using grade points and optional course credits."
        )

    if "library" in question:
        return search_campus("library")

    if "canteen" in question or "food" in question:
        return search_campus("canteen")

    if "lab" in question:
        return search_campus("lab")

    if "office" in question:
        return search_campus("office")

    if "emergency" in question:
        return (
            f"The emergency contact number is "
            f"{get_contact('emergency')}."
        )

    if "placement" in question:
        return (
            f"The placement contact number is "
            f"{get_contact('placement')}."
        )

    if "contact" in question:
        return (
            "Open Important Contacts to find office, library, "
            "placement, and emergency contact information."
        )

    if "hello" in question or "hi" in question:
        return (
            "Hello! I am the Campus AI Assistant. "
            "How can I help you?"
        )

    return (
        "I'm not sure about that yet. Try asking me about "
        "attendance, CGPA, the library, canteen, labs, office, "
        "placements, emergencies, or campus contacts."
    )


def main():
    st.title("🎓 Campus AI")
    st.write("Your smart companion for everyday campus life.")

    menu = st.sidebar.selectbox(
        "Choose a feature",
        [
            "Home",
            "AI Assistant",
            "Attendance Calculator",
            "CGPA Calculator",
            "Campus Search",
            "Important Contacts",
        ],
    )

    if menu == "Home":
        st.header("🏠 Welcome to Campus AI")

        st.write(
            "Campus AI is a student assistant designed to make "
            "everyday campus tasks easier."
        )

        st.subheader("Features")
        st.write("🤖 Ask the Campus AI Assistant")
        st.write("📊 Calculate your attendance percentage")
        st.write("🎓 Calculate your CGPA")
        st.write("🔍 Find important campus locations")
        st.write("📞 Find important campus contacts")

    elif menu == "AI Assistant":
        st.header("🤖 Campus AI Assistant")

        st.write(
            "Ask me questions about attendance, CGPA, campus "
            "locations, contacts, placements, and more."
        )

        question = st.text_input(
            "What would you like to know?"
        )

        if st.button("Ask AI"):
            answer = campus_assistant(question)
            st.info(answer)

    elif menu == "Attendance Calculator":
        st.header("📊 Attendance Calculator")

        attended = st.number_input(
            "Classes attended",
            min_value=0,
            step=1
        )

        total = st.number_input(
            "Total classes",
            min_value=0,
            step=1
        )

        if st.button("Calculate Attendance"):
            try:
                percentage = calculate_attendance(
                    attended,
                    total
                )

                st.success(
                    f"Attendance: {percentage}%"
                )

                st.info(
                    attendance_advice(attended, total)
                )

            except ValueError as e:
                st.error(str(e))

    elif menu == "CGPA Calculator":
        st.header("🎓 CGPA Calculator")

        grades_input = st.text_input(
            "Enter your grade points separated by commas "
            "(e.g. 9, 8, 10)"
        )

        credits_input = st.text_input(
            "Credits for each course, same order "
            "(optional, e.g. 4, 3, 3)"
        )

        if st.button("Calculate CGPA"):
            try:
                grades = parse_numbers(grades_input)

                if credits_input.strip():
                    credits = parse_numbers(credits_input)
                else:
                    credits = None

                cgpa = calculate_cgpa(
                    grades,
                    credits
                )

                st.success(
                    f"Your CGPA is: {cgpa}"
                )

            except ValueError as e:
                message = str(e)

                if "could not convert" in message:
                    message = (
                        "Please enter numbers separated by commas."
                    )

                st.error(message)

    elif menu == "Campus Search":
        st.header("🔍 Campus Search")

        query = st.text_input(
            "Search for a campus location"
        )

        if st.button("Search"):
            result = search_campus(query)
            st.info(result)

    elif menu == "Important Contacts":
        st.header("📞 Important Contacts")

        department = st.selectbox(
            "Select a department",
            [
                "office",
                "library",
                "placement",
                "emergency",
            ],
        )

        if st.button("Get Contact"):
            contact = get_contact(department)

            st.info(
                f"Contact: {contact}"
            )


if __name__ == "__main__":
    main()
