QnA_List = [
    {
        "question": "What is the capital of France?",
        "answers": [
            {"answer": "paris", "is_correct": True},
        ]
        },
    {
        "question": "What is the largest planet in our solar system?",
        "answers": [
            {"answer": "jupiter", "is_correct": True},
            
        ]
    },
    {
        "question": "What is the chemical symbol for water?",
        "answers": [
            {"answer": "h2o", "is_correct": True}
            ]
    },
    {
        "question": "What is the largest mammal on Earth?",
        "answers": [
            {"answer": "blue whale", "is_correct": True}
        ]
    },
    {
        "question": "Who is known as the father of modern physics?",
        "answers": [
            {"answer": "albert einstein", "is_correct": True}
        ]
    },
    {
        "question": "Who is Prime Minister of Pakistan?",
        "answers": [
            {"answer": "shahbaz sharif", "is_correct": True}
        ]
    }

]

def check_answer(question, user_answer):
    for answer in question["answers"]:
        if answer["answer"] == user_answer.lower():
            return answer["is_correct"]
    return False

def ask_questions(questions):
    score = 0
    for question in questions:
        print(question["question"])
        user_answer = input("Your answer: ")
        if check_answer(question, user_answer):
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score}/{len(questions)}.")


print("Welcome to the Bonus Quiz!")
ask_questions(QnA_List)
print("Thank you for participating!")