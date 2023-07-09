#a)

def update_points(student_points: dict[str, int], changes: dict[str, int]) -> dict[str, int]:
    for name, change in changes.items():
        if name in student_points:
            student_points[name] += change
    for name in changes:
        if name not in student_points:
            raise KeyError(f'{name} wurde nicht gefunden')
    for values in student_points.values():
        if values > 120 or values < 0:
            raise ValueError(f'Die Gesamtpunktzahl muss zwischen 0 und 120 liegen')
    return student_points


'''def compute_grade(student_points: dict[str, int], max_points: int, student_name: str) -> int:
    pass_points = max_points // 2
    for name in student_points:
        if name == student_name:
            if student_points[name] < pass_points:
                return 5
            elif student_points[name] >= pass_points and student_points[name] <= (pass_points + max_points * 0.25):
                return 4
            elif student_points[name] >= (pass_points + max_points * 0.25) and student_points[name] <= (pass_points + max_points * 0.5):
                return 3
            elif student_points[name] >= (pass_points + max_points * 0.5) and student_points[name] <= (pass_points + max_points * 0.75):
                return 2
            elif student_points[name] > (pass_points + max_points * 0.75):
                return 1
    if gt_40(student_points, max_points) is True:
        while gt_40(student_points, max_points) is True and pass_points > 0:
            pass_points = pass_points - 1
            (compute_grade(student_points, max_points, student_name))
        return (compute_grade(student_points, max_points, student_name))
    return (compute_grade(student_points, max_points, student_name))


def failed_students(student_points, max_points):
    failed_students_list = []
    for name in student_points:
        if compute_grade(student_points, max_points, name) == 5:
            failed_students_list.append(name)
    return failed_students_list


def gt_40(student_points, max_points):
    students_list = []
    for name in student_points:
        students_list.append(name)
    if len(failed_students(student_points, max_points)) / len(students_list) > 0.4:
        return True
    return False'''


def compute_grade(student_points: dict[str, int], max_points: int, student_name: str) -> int:
    pass_points = max_points // 2
    students_count = len(student_points)
    passed_count = len([name for name, points in student_points.items() if points >= pass_points])
    while (passed_count / students_count) < 0.4 and pass_points > 0:
        pass_points -= 1
        passed_count = len([name for name, points in student_points.items() if points >= pass_points])

    if student_name in student_points:
        points = student_points[student_name]
        if points < pass_points:
            return 5
        elif points <= (pass_points + max_points * 0.25):
            return 4
        elif points <= (pass_points + max_points * 0.5):
            return 3
        elif points <= (pass_points + max_points * 0.75):
            return 2
        else:
            return 1
    else:
        return -1  # Return a default value when student name is not found


def failed_students(student_points, max_points):
    failed_students_list = []
    for name in student_points:
        if compute_grade(student_points, max_points, name) == 5:
            failed_students_list.append(name)
    return failed_students_list


def gt_40(student_points, max_points):
    students_count = len(student_points)
    passed_count = len([name for name, points in student_points.items() if compute_grade(student_points, max_points, name) != 5])
    return (passed_count / students_count) >= 0.4



if __name__ == '__main__':
    student_points = {"Adam": 63, "John": 112, "Donald": 43}
    changes = {"Adam": 3, "John": -7}
    #update_points(student_points, changes)
    #print(student_points)
    print(compute_grade(student_points, 120, "Adam"))
    print(failed_students(update_points(student_points, changes), 120))
    print(gt_40(student_points, 120))

