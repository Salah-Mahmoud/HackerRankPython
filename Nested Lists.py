if __name__ == '__main__':
    students = []
    scores = set()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.add(score)

    second_min_score = sorted(scores)[1]
    names = sorted([student[0] for student in students if student[1] == second_min_score])

    print("\n".join(names))
