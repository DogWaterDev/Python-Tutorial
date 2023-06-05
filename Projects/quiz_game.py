##-----------------------------------##
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)
#-----------------------------------#
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0
#-----------------------------------#
def display_score(correct, guesses):
    print("-----------------------------------")
    print("            RESULTS")
    print("-----------------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=", ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=", ")
    print()

    score = int((correct/len(questions))*100)
    print("-----------------------------------")
    print("        SCORE: {}/{}, {}%".format(correct, len(questions), score))
    print("-----------------------------------")
#-----------------------------------#
def play_again():

    response = input("Do you want to play again? (yes or no): ").upper()
    if response == "YES":
        return True
    else:
        return False

questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"

}

options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "Charles Hem"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 1995"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. Taunty Bithon"],
    ["A. Yes", "B. No", "C. Maybe", "D. Sometimes"]
    ]

new_game()

while play_again() == True:
    new_game()

print("Bye!")