import random
import math

def welcome():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def run_brain_prime(name, rounds=3):
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")

    correct_answers = 0

    for _ in range(rounds):
        question_number = random.randint(1, 100)
        print(f"Question: {question_number}")
        user_answer = input("Your answer: ").lower()

        if (user_answer == "yes" and is_prime(question_number)) or \
           (user_answer == "no" and not is_prime(question_number)):
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect. Game over.")
            break

    if correct_answers == rounds:
        print(f"Congratulations, {name}! You've win!")

def main():
    name = welcome()
    run_brain_prime(name)

if __name__ == "__main__":
    main()
