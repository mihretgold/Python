def new_game():
    # WELCOMING SESSION

    print("------------------------------------------------\n")
    print('          Welcome            \n\nNow it is time for a quick quiz on the concepts of python.\n')
    option = input("Do you want to take the QUIZ? YES or NO: ")
    if option.upper() == 'YES':
        print("Good Luck!")
        guesses = []
        # Variable to keep track of all correct guesses
        correct_guesses = 0
        # Variable to represent indexes of all the questions
        question_num = 1

        # Prints all the Questions
        for key in questions:
            print("---------------------------")
            print(key)
            # Print the options to the respective questions
            for i in options[question_num - 1]:
                print(i)
            # Accepts the users guess
            while True:
                guess = input("Enter (A, B, C, D): ")
                # changes the users guess to upper case
                guess = guess.upper()
                if guess not in ('A', 'B', 'C', 'D'):
                    print("Please enter only A, B, C or D.")
                else:
                    break
            # We add all the users guess to the guesses list
            guesses.append(guess)

            correct_guesses += check_answer(questions.get(key), guess)
            question_num += 1
        # Calls the display_score function and displays your score
        display_score(correct_guesses, guesses)
    # ---------------------------
    elif option.upper() == 'NO':
        print("Good Bye!")
    else:
        print('Invalid input')


    # List to store all guesses of the user

def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        # returns 1 to add 1 to number of correct guesses on the new_game function
        return 1
    else:
        print("WRONG!")
        print("CORRECT ANSWER IS:", answer)
        return 0
# ---------------------------
# Function to display correct answers and the total score user got
def display_score(correct_guesses, guesses):
    print("--------------------------")
    print("RESULTS")
    print("--------------------------")
    # Displays the correct answers
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    # Displays the guesses of the user
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("You got", correct_guesses, "/", len(questions))
    print("Your score is:", score, "% ")
    if (score > 90 and score <= 100):
        print("You passed: with grade A")
    elif (score > 80):
        print("You passed: with grade B")
    elif (score > 70):
        print("You passed: with grade C")
    elif (score > 60):
        print("You passed: with warrnig")
    elif (score < 59 and score >= 0):
        print("You failed")
    else:
        print("Invalid score")

# ---------------------------
# Function to try again
def try_again():

    response = input("Do you want to play again? (yes or no: )")
    # Converts user response to upper case
    response= response.upper()

    if response == "YES":
        return True
    else:
        return False

# ---------------------------

# Dictionary of Questions
questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

# 2D array of option answers for each questions
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

# Calling the new_game function to display the question
new_game()
# Checks if the user wants to try again
while try_again():
    new_game()

print("The Quiz is Over Thank you!!!")