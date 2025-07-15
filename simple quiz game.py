# List of questions, choices, and correct answers
questions = [
    {
        "question": "Who is the best person in the whole entire universe??",
        "choices": ["A) ur mom", "B) albert einstien", "C) Siyona", "D) Edgar Allen Poe"],
        "correct_answer": "C"
    },
    {
        "question": "Is Python a programming language? (True/False)",
        "choices": ["A) True", "B) False"],
        "correct_answer": "A"
    },
    {
        "question": "what is the only planet that has life on it?",
        "choices": ["A) mars", "B) pluto", "C) earth", "D) the moon"],
        "correct_answer": "C"
    },
    {
        "question": "Who wrote the harry potter series ?",
        "choices": ["A) jk rowling", "B) Dickens", "C) Rick riodorn", "D) Shaksphere"],
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
