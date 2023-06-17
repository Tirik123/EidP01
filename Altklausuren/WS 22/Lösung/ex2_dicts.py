# Aufgabe 2 (Dictionaries und Sets) ###########################################

def compose(
    prof_to_courses: dict[str, set[str]],
    course_to_students: dict[str, set[str]]
) -> dict[str, set[str]]:
    prof_to_students = dict()
    for prof, courses in prof_to_courses.items():
        if prof not in prof_to_students:
            prof_to_students[prof] = set()
        for course in courses:
            if course in course_to_students:  # optional
                for student in course_to_students[course]:
                    prof_to_students[prof].add(student)
    return prof_to_students


if __name__ == '__main__':
    d1 = {
        'A': {'a', 'b'},
        'B': {'b', 'c'},
        'C': {'e', 'f'},
    }

    d2 = {
        'a': {'1', '2'},
        'b': {'2', '3'},
        'c': {'4', '5'},
        'e': {'5', '6'},
        'f': {'6', '7'},
    }

    d = {
        'A': {'1', '2', '3'},
        'B': {'2', '3', '4', '5'},
        'C': {'5', '6', '7'},
    }

    assert compose(d1, d2) == d
