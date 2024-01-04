import random
import math

def welcome_user():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    return user_name

def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def play_game(user_name):
    correct_answers_count = 0

    while correct_answers_count < 3:
        num1, num2 = generate_question()
        print("Find the greatest common divisor of given numbers.")
        print(f"Question: {num1} {num2}")

        user_answer = int(input("Your answer: "))

        correct_answer = math.gcd(num1, num2)

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
