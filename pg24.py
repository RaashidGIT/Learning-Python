# AIM: To create a Python-based multiple-choice quiz game that asks the user 
#      questions, collects their answers, checks correctness, 
#      and displays the final score with results.

# ---------------- QUIZ GAME ----------------

# Questions for the quiz
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

# Multiple-choice options corresponding to each question
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

# Correct answers for each question
answers = ("C", "D", "A", "A", "B")

# To store user guesses
guesses = []

# To keep track of the score
score = 0

# Index to track question number
question_num = 0

# Loop through each question
for question in questions:
    print("----------------------")
    print(question)

    # Display all options for the current question
    for option in options[question_num]:
        print(option)

    # Take user input (A/B/C/D) and convert to uppercase
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)  # store guess

    # Check if the guess is correct
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    # Move to the next question
    question_num += 1

# ---------------- RESULTS ----------------
print("----------------------")
print("       RESULTS        ")
print("----------------------")

# Print correct answers
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

# Print user guesses
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

# Calculate and print score as percentage
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
