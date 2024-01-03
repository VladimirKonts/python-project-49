import random

def welcome_user():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    return user_name

def is_even(number):
    return number % 2 == 0

def play_game(user_name):
    correct_answers_count = 0

    while correct_answers_count < 3:
        question_number = random.randint(1, 20)
        print("Answer 'yes' if the number is even, otherwise answer 'no'.")
        print(f"Question: {question_number}")
        
        user_answer = input("Your answer: ").lower()

        if (user_answer == 'yes' and is_even(question_number)) or (user_answer == 'no' and not is_even(question_number)):
            print("Correct!")
            correct_answers_count += 1
        else:
            correct_answer = 'yes' if is_even(question_number) else 'no'
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
