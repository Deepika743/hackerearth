if __name__ == '__main__':
    # Read the number of students
    n = int(input().strip())

    # Create a list to store students
    students = []

    # Read each student's name and grade
    for _ in range(n):
        name = input().strip()
        grade = float(input().strip())
        students.append([name, grade])

    # Sort the students list based on grades
    students.sort(key=lambda x: (x[1], x[0]))

    # Find the second lowest grade
    second_lowest_grade = min([s[1] for s in students if s[1] != students[0][1]])

    # Print the names of students with the second lowest grade
    for student in students:
        if student[1] == second_lowest_grade:
            print(student[0])
