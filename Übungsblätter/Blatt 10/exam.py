def update_points(student_points: dict[str, int], changes: dict[str, int]) -> dict[str, int]:
    new_dict = {}
    for student, grade in student_points.items():
        if student not in new_dict:
            new_dict[student] = grade
    print(new_dict)
    for students, grades in changes.items():
        for student, grade in student_points.items():
            if students in new_dict.keys():
                new_dict[students] = grades + grade
    return new_dict
                




if __name__ == '__main__':
    student_points = {"Adam": 63, "John": 112, "Donald": 43}
    changes = {"Adam": 3, "John": -7}
    print(update_points(student_points, changes))
