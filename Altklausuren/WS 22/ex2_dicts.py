# Aufgabe 2 (Dictionaries und Sets) ###########################################

def compose(prof_to_courses: dict[str, set[str]], course_to_students: dict[str, set[str]]) ->  dict[str, str]:
    prof_to_students = {} # new list containing prof with students
    for prof, courses in prof_to_courses.items(): 
        if prof not in prof_to_students: 
            prof_to_students[prof] = set() # adding the profs as keys to the empty list with "set()" as values
        for course in courses:
            if course in course_to_students: # now we want to filter the course pairs from profs with the course pairs from students
                for student in course_to_students[course]: # iterates the students in the courses that correspond to the courses in prof_to_courses
                    prof_to_students[prof].add(student) # the keys (profs) 
    return(prof_to_students)
            
            
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
