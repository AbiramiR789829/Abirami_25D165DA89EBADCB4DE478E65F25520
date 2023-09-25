class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the list of students in descending order of CGPA
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:
students = [
    Student("Abirami", "A123", 7.8),
    Student("Ramya", "A124", 8.9),
    Student("Sneha", "A125", 9.1),
    Student("manimegalai", "A126", 9.2),
]

# Print the sorted list of students
for student in sort_students(students):
    print("Name: {}, Roll number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))
