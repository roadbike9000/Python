"""
Using this list of student names and grades [["Mark", 78], ["Kate", 55], ["Sara", 87]]
Calculate the average score of the students
Find the student with the highest score
Find the student with the lowest score
Count the number of students with pass marks (>= 50)
"""
student_grades = [["Mark", 78], ["Kate", 55], ["Sara", 87]]
student_with_the_highest_score = ""
student_with_the_lowest_score = ""
average_grade = 0
grade_totals = 0
lowest_score = 0
highest_score = 0
number_of_students_with_passing_grade = 0
passing_grade = 50
grade_list = []
age_name_pairs = []


def student_performance(class_grades, passing_grade: int, average_grade, grade_totals, student_with_the_highest_score, student_with_the_lowest_score, number_of_students_with_passing_grade):
    for student in class_grades:
        grade_totals += student[1]
        grade_list.append(student[1])
        # create list of tuples with grade as the key
        age_name_pairs.append((student[1], student[0]))
        if student[1] >= passing_grade:
            number_of_students_with_passing_grade += 1
    average_grade = grade_totals / len(class_grades)

    # Find the tuple with the highest and lowest grade
    highest_score = max(age_name_pairs)
    lowest_score = min(age_name_pairs)

    # Extract the name from the tuples
    student_with_the_highest_score = highest_score[1]
    student_with_the_lowest_score = lowest_score[1]
    print(f"average_grade = {average_grade: .2f} student_with_the_highest_score = {student_with_the_highest_score} student_with_the_lowest_score = {student_with_the_lowest_score} number_of_students_with_passing_grade = {number_of_students_with_passing_grade}")


student_performance(student_grades, passing_grade, average_grade, grade_totals, student_with_the_highest_score, student_with_the_lowest_score, number_of_students_with_passing_grade)
