from models.student import Student, InvalidScoreError
from utils import print_report

data = {
    "Aarav": 87,
    "Riya": 92,
    "Kabir": 76,
    "Meera": 95,
    "Invalid": 150
}

students = []
for name, score in data.items():
    try:
        students.append(Student(name, score))
    except InvalidScoreError as e:
        print(f"Skipping {name}: {e}")

print_report(students)