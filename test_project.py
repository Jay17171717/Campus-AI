import pytest

from project import (
    calculate_attendance,
    attendance_advice,
    calculate_cgpa,
    parse_numbers,
    search_campus,
    get_contact,
    campus_assistant,
)


def test_calculate_attendance():
    assert calculate_attendance(75, 100) == 75.0
    assert calculate_attendance(45, 50) == 90.0
    assert calculate_attendance(10, 20) == 50.0


def test_attendance_errors():
    with pytest.raises(ValueError):
        calculate_attendance(10, 0)

    with pytest.raises(ValueError):
        calculate_attendance(-5, 100)

    with pytest.raises(ValueError):
        calculate_attendance(110, 100)


def test_attendance_advice():
    assert "Attend the next" in attendance_advice(60, 100)
    assert "miss up to" in attendance_advice(90, 100)
    assert "right at" in attendance_advice(75, 100)


def test_calculate_cgpa():
    assert calculate_cgpa([8, 9, 10]) == 9.0

    assert calculate_cgpa(
        [7.5, 8.5, 9.0]
    ) == 8.33


def test_weighted_cgpa():
    assert calculate_cgpa(
        [8, 9, 10],
        [4, 3, 3]
    ) == 8.9


def test_cgpa_errors():
    with pytest.raises(ValueError):
        calculate_cgpa([])

    with pytest.raises(ValueError):
        calculate_cgpa([8, 11, 9])

    with pytest.raises(ValueError):
        calculate_cgpa(
            [8, 9],
            [4]
        )


def test_parse_numbers():
    assert parse_numbers(
        "8,9,10"
    ) == [8.0, 9.0, 10.0]

    assert parse_numbers(
        "7.5, 8.5, 9"
    ) == [7.5, 8.5, 9.0]


def test_search_campus():
    assert search_campus(
        "library"
    ) == "The library is located in the main academic block."

    assert search_campus(
        "Where is the canteen?"
    ) == "The canteen is located near the main campus area."

    assert search_campus(
        "gym"
    ) == "Location not found."


def test_get_contact():
    assert get_contact(
        "emergency"
    ) == "112"

    assert get_contact(
        "sports"
    ) == "Contact not found."


def test_campus_assistant():
    assert "Attendance Calculator" in campus_assistant(
        "How do I check my attendance?"
    )

    assert "CGPA Calculator" in campus_assistant(
        "How can I calculate my CGPA?"
    )

    assert "library" in campus_assistant(
        "Where is the library?"
    ).lower()

    assert "canteen" in campus_assistant(
        "Where can I get food?"
    ).lower()

    assert "112" in campus_assistant(
        "What is the emergency contact?"
    )

    assert campus_assistant(
        ""
    ) == "Please ask me a question."
