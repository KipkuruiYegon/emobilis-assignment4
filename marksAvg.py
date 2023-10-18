maths_grade = int(input("Please enter Maths grade: "))
physics_grade = int(input("Please enter Physics grade: "))
geography_grade = int(input("Please enter Geography grade: "))
chemistry_grade = int(input("Please enter Chemistry grade: "))


avg_final = (maths_grade + physics_grade + geography_grade + chemistry_grade) / 4

def avg_grade_scoring(avg_final):
    if avg_final < 0 or avg_final > 100:
        return 'Unrecognized marks/avg'
    elif avg_final >= 71:
        return 'A'
    elif avg_final >= 51:
        return 'B'
    elif avg_final >= 31:
        return 'C'
    else:
        return 'D'

student_avg = avg_grade_scoring(avg_final)

print(f"The Student Avegrage is:  {student_avg}")