questions = ["What is the captial of france?", "What is the formula for pressure?", "Who is credited with inventing the World Wide Web?"]
answers = [["Paris", "Italy", "Germany", "London"], ["p=f*a", "a=p/f", "p=f/a", "P=a/f"], ["Tim Berners-Lee", "Bill Gates", "Steve Jobs", "Mark Zuckerberg"]]
correct = [1, 3, 1]
score = 0
class start_quiz ():
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
    quiz_questions = len(questions)
    print("your score is {}".format(score) + " out of ", quiz_questions)



start_quiz()
