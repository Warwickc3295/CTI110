# CTI-110
# M6HW1 - Test Grading Program
# Cameron Warwick
# 11/19/17



# Calls other functions, holds input
def main():
    print('Welcome to the Grade Giver 9000!')
    print('--------------------------------')
    print('Please enter the five grades that you would like averaged: ')
    grades = []
    keepGoing = 0
    while keepGoing < 5:
        new_grade = int(input('Grade: '))
        grades.append(new_grade)
        keepGoing = keepGoing + 1
    calc_average(grades)
    average = calc_average(grades)
    determine_grade(average)
    finalGrade = determine_grade(average)
    print(finalGrade)
    

# Does exactly as described
def calc_average(grades):
    total = sum(grades)
    average = total / 5
    return average


# Does exactly as described
def determine_grade(average):
    if average >= 90:
        finalGrade = 'A'
    elif 90 > average >= 80:
        finalGrade = 'B'
    elif 80 > average >= 70:
        finalGrade = 'C'
    elif 70 > average >= 60:
        finalGrade = 'D'
    else:
        finalGrade = 'F'
    return finalGrade
    
main()

