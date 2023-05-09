questions = ["What is the captial of france?", "What is the formula for pressure?"]
answers = [["Paris", "Italy", "Germany", "London"], ["p=f*a", "a=p/f", "p=f/a", "P=a/f"]]
correct = [1, 3]


def print_answers(answer):
    index = questions.index(answer)
    print("Answers")
    print("----------------------------")
    for answer in answers[index]:
        print(str(answer))
    print("----------------------------")


def print_question(question):
    print("----------------------------")
    print(question)
    print("----------------------------")

score = 0
for i in questions:
    print_question(i)
    print_answers(i)
    choice = input("1, 2, 3, 4: ")
    if int(choice) == correct[questions.index(i)]:
        print("correct")
        score += 1
    else:
        print("incorrect")
    print("----------------------------")
