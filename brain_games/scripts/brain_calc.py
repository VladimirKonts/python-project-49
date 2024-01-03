import random

def welcome_user():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    return user_name

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    expression = f"{num1} {operator} {num2}"
    correct_answer = str(eval(expression))
    return expression, correct_answer

def play_game(user_name):
    correct_answers_count = 0

    while correct_answers_count < 3:
        expression, correct_answer = generate_question()
        print("What is the result of the expression?")
        print(f"Question: {expression}")

        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return False

    print(f"Congratulations, {user_name}!")
    return True

def main():
    user_name = welcome_user()
    play_game(user_name)

if __name__ == "__main__":
    main()
