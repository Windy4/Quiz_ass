#Declare the variables for the second quiz
questions_2 = ["What is the largest planet in our solar system?", "Which animal is known for its black and white stripes?"]
answers_2 = [["Earth", "Mars", "Jupiter", "Saturn"], ["Elephant", "Tiger", "Zebra", "Giraffe"]]
correct_2 = [3, 3]
#Declare the variables for the first quiz
questions_1 = ["What is the captial of france?", "What is the formula for pressure?", "Who is credited with inventing the World Wide Web?"]
answers_1 = [["Paris", "Italy", "Germany", "London"], ["p=f*a", "a=p/f", "p=f/a", "P=a/f"], ["Tim Berners-Lee", "Bill Gates", "Steve Jobs", "Mark Zuckerberg"]]
correct_1 = [1, 3, 1]
#Declare the variable for the differance between quizes
minage = 10

def print_question(question):
    #Prints the required question
    #used to make code more efficient
    print("----------------------------")
    print(question)
    print("----------------------------")

def print_answers(answer, age):
    if age <= int(minage):
        index = questions_2.index(answer)
        print("Answers")
        print("----------------------------")
        for answer in answers_2[index]:
            print(str(answer))
        print("----------------------------")
    else:
        index = questions_1.index(answer)
        print("Answers")
        print("----------------------------")
        for answer in answers_1[index]:
            print(str(answer))
        print("----------------------------")



def start_young_quiz(age):
    score_2 = 0
    for i in questions_2:
        print_question(i)
        print_answers(i, age)
        choice = input("1, 2, 3, 4: ")
        if int(choice) == correct_2[questions_2.index(i)]:
            print("correct")
            score_2 += 1
        else:
            print("incorrect")
        print("----------------------------")
    quiz_questions = len(questions_2)
    print("your score is {}".format(score_2) + " out of ", quiz_questions)

def start_quiz (age):
    """
    Had problem with score, used gpt to tell me to move the score outside of for loop,
    this is the answer gpt gave me

    "I see that you're having an issue with the score count section.
     Let's take a closer look at the code and identify the problem.

    In both the start_young_quiz and start_quiz functions,
    there is a variable named score that is initialized to 0 inside the loop.
    This causes the score to reset to 0 for each question. To fix this issue,
    you need to move the score variable initialization outside the loop,
    before the loop begins."
    """
    score = 0
    for i in questions_1:
        print_question(i)
        print_answers(i, age)
        choice = input("1, 2, 3, 4: ")
        if int(choice) == correct_1[questions_1.index(i)]:
            print("correct")
            score += 1
        else:
            print("incorrect")
        print("----------------------------")
    quiz_questions = len(questions_1)
    print("your score is {}".format(score) + " out of ", quiz_questions)


class age_verification ():
    check = 1
    while check == 1:
        age = input("How old are you?: ")
        if isinstance(age, int):
            check -= 0
            if int(age) <= int(minage):
                start_young_quiz(age)
            else:
                start_quiz(age)
        else:
            print("Non Integer, try again")

