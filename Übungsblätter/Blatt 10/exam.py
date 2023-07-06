def update_points(student_points: dict[str, int], changes: dict[str, int]) -> dict[str, int]:
    for name, additional_points in changes.items():
        if name in student_points:
            new_points = student_points[name] + additional_points
            if new_points > 120 or new_points < 0:
                raise ValueError(
                    "Die Gesamtpunktzahl muss zwischen 0 und 120 liegen")
            student_points[name] = new_points
        else:
            raise KeyError(name + " wurde nicht gefunden")




if __name__ == '__main__':
    student_points = {"Adam": 63, "John": 112, "Donald": 43}
    changes = {"Adam": 3, "John": -7}
    print(update_points(student_points, changes))
