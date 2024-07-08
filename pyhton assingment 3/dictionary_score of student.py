def update_score(student_scores, student_name, new_score):
    if student_name in student_scores:
        student_scores[student_name] = new_score
        print(f"Score updated for {student_name}")
    else:
        print(f"Student {student_name} not found in records")

    return student_scores

if __name__ == "__main__":
    student_scores = {
        'Pranav': 85,
        'Rahul': 70,
        'Anand': 90,
        'Anuj': 65,
    }

    student_name = 'Pranav'
    new_score = 75
    updated_scores = update_score(student_scores, student_name, new_score)

    print("\nUpdated Student Scores:")
    for student, score in updated_scores.items():
        print(f"{student}: {score}")
