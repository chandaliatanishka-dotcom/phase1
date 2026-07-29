def calculate_average(scores):
    return sum(scores) / len(scores)


def highest_score(scores):
    return max(scores)


def lowest_score(scores):
    return min(scores)


def rank_students(students):
    return sorted(
        students.items(),
        key=lambda x: x[1],
        reverse=True
    )


def display_summary(students):

    scores = list(students.values())

    print("\n--- STUDENT REPORT ---")

    print(f"Average Score: {calculate_average(scores)}")
    print(f"Highest Score: {highest_score(scores)}")
    print(f"Lowest Score: {lowest_score(scores)}")

    print("\n--- RANKINGS ---")

    rankings = rank_students(students)

    for rank, (name, score) in enumerate(rankings, start=1):
        print(f"{rank}. {name} -> {score}")


students = {
    "Aarav": 87,
    "Riya": 92,
    "Kabir": 76,
    "Meera": 95
}

display_summary(students)
