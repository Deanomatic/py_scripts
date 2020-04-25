# main list to loop over and get GPA
grade_list = ["Abbey", "100", "79", "85", "91", "Bill", "67", "101", "95", "91", "Steve", "93", "79", "80", "97"]
# counter used to end the while loop after 3 iterations
counter = 0
# established empty list
student_grades = list()
while counter < 3:
    # looping through the first 5 index points in grade_list
    # then break out of the for loop
    for student in grade_list[:5]:
        # adding first 5 index points to the empty list
        student_grades.append(student)
    # remove the first five index points from the grade_list so
    # we don't use them again
    del grade_list[0:5]
    # get the students name
    student_name = str(student_grades[0])
    # get and calculate the student's GPA
    gpa = (int(student_grades[1]) + int(student_grades[2]) + int(student_grades[3]) + int(student_grades[4])) / 4
    print(student_name + " got a " + str(gpa) + " grade point average.")
    # reset the student grades list to empty so we can move to
    # the next student
    student_grades = list()
    # moving the counter up one until it hits 3
    counter += 1
