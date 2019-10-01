import pytest

import markbook


def test_create_assigment():
    assignment1 = markbook.create_assignment(name="Assignment One",
                                            due="2019-09-21",
                                            points=100
                                            classcode = ICS4U1)
    expected = {
        "name": "Assignment One",
        "due": "2019-09-21",
        "points": 100
        "classcode": ICS4U
    }
    assert assignment1 == expected

    assignment2 = main.create_assignment(name="Assignment Two",
                                             due=None,
                                             points=1
                                             classcode = ICS4U1)
    assert assignment2["name"] == "Assignment Two"
    assert assignment2["due"] is None
    assert assignment2["points"] == 1
    assert assignment2["classcode"] == ICS4U1


def test_create_classroom():
    classroom = main.create_classroom(course_code="ICS4U",
                                          course_name="Computer Science",
                                          period=2,
                                          teacher="Mr. Gallo")
    expected = {
        "course_code": "ICS4U",
        "course_name": "Computer Science",
        "period": 2,
        "teacher": "Mr. Gallo"
    }

    # The classroom needs to be a dictionary identical to the expected
    assert classroom == expected

    # The classroom needs to be created with an empty student list in order for students to be inputted.
    assert classroom["Students"] == []


def test_add_student_to_classroom():
    """
    Dependencies:
        - create_classroom()
    """
    classroom = markbook.create_classroom(course_code="ICS4U",
                                          course_name="Computer Science",
                                          period=2,
                                          teacher="Mr. Gallo")
    first_name = "test"
    last_name = "test"

    markbook.add_student_to_classroom(first_name, last_name)
    assert type(classroom["Students"]) is list
    assert len(classroom["Students"]) == 1


def test_remove_student_from_classroom():
    """
    Dependencies:
        - create_classroom()
        - add_student_to_classroom()
    """
    classroom = markbook.create_classroom(course_code="ICS4U",
                                          course_name="Computer Science",
                                          period=2,
                                          teacher="Mr. Gallo")
    first_name = "test"
    last_name = "test"

    markbook.add_student_to_classroom(first_name, last_name)
    assert len(classroom["Students"]) == 1
    markbook.remove_student_from_classroom(first_name, last_name)
    assert type(classroom["Students"]) is list
    assert len(classroom["Students"]) == 0


def test_edit_student():
    student = {"first_name": "John", "last_name": "Smith", "grade": 10}
    markbook.edit_student("first_name", "Bob")
    
