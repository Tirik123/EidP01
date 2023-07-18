def compose(prof_to_courses: dict[str, set[str]], courses_to_students: dict[str, set[str]]) -> dict[str, set[str]]:
    new_dict = {}
    for prof, course in prof_to_courses.items():
        new_dict[prof] = set()
        for Kurs in course:
            for courses, students in course_to_students.items():
                for student in students:
                    if courses == Kurs:
                        new_dict[prof].add(student)
    return (new_dict)




if __name__ == '__main__':
    prof_to_courses = {
        "Prof A": {"Course A", "Course B"},
        "Prof B": {"Course B", "Course C"},
    }

    course_to_students = {
        "Course A": {"Student A", "Student B"},
        "Course B": {"Student B", "Student C"},
        "Course C": {"Student D", "Student E"},
    }
    print(compose(prof_to_courses, course_to_students))




# 10/10