from models.student import Student

def get_average(students: list) -> float:
    return sum(s.score for s in students) / len(students)

def get_highest(students: list) -> str:
    return max(students, key=lambda s: s.score).name

def get_lowest(students: list) -> str:
    return min(students, key=lambda s: s.score).name

def get_ranked(students: list) -> list:
    return sorted(students, key=lambda s: s.score, reverse=True)

def print_report(students: list) -> None:
    print("\n--- STUDENT REPORT ---")
    print(f"Average Score: {get_average(students):.1f}")
    print(f"Highest: {get_highest(students)}")
    print(f"Lowest: {get_lowest(students)}")
    print("\n--- RANKINGS ---")
    for i, s in enumerate(get_ranked(students), 1):
        print(f"{i}. {s}")