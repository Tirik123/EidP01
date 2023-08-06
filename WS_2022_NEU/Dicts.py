def compose(prof_to_courses: dict[str, set[str]], course_to_students: dict[str, set[str]]) -> dict[str, set[str]]:
    result = {}
    for prof, course in prof_to_courses.items():
        if prof not in result:
            result[prof] = set()
    for courses, students in course_to_students.items():
        for profz, coursez in prof_to_courses.items():
            if courses in coursez:
                for i in students:
                    result[profz].add(i)
    return result






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