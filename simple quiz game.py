# List of questions, choices, and correct answers
questions = [
    {
        "question": "Who is the best person in the whole entire universe??",
        "choices": ["A) ur mom", "B) albert einstien", "C) Siyona Ghanate", "D) Edgar Allen Poe"],
        "correct_answer": "C"
    },
    {
        "question": "Is Python a programming language? (True/False)",
        "choices": ["A) True", "B) False"],
        "correct_answer": "A"
    },
    {
        "question": "what is the best book ever?",
        "choices": ["A) ur mom", "B) powerless", "C) percy jackson", "D) inheritance games"],
        "correct_answer": "B"
    },
    {
        "question": "Who wrote the best book ever ?",
        "choices": ["A) lauren roberts", "B) Dickens", "C) ur mom", "D) Shaksphere"],
        "correct_answer": "A"
    }
]


def ask_question(question):
    print(question['question'])
    for choice in question['choices']:
        print(choice)

    answer = input("Your answer (A, B, C, D): ").upper()
    return answer == question['correct_answer']


def start_quiz():
    score = 0
    for q in questions:
        if ask_question(q):
            print("Correct!\n")
            score += 1
        else:
            print("Wrong!\n")

    print(f"Your final score is: {score}/{len(questions)}")


if __name__ == "__main__":
    start_quiz()
