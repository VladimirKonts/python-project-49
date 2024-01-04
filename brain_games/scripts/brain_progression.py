import random

def welcome_user():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    return user_name

def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    length = random.randint(5, 10)
    
    progression = [start + step * i for i in range(length)]
    
    hidden_index = random.randint(0, length - 1)
    hidden_number = progression[hidden_index]
    
    progression[hidden_index] = '..'
    
    return progression, hidden_number

def play_game(user_name):
    correct_answers_count = 0

    while correct_answers_count < 3:
        progression, hidden_number = generate_progression()
        print("What number is missing in the progression?")
        print(f"Question: {' '.join(map(str, progression))}")

        user_answer = int(input("Your answer: "))

        if user_answer == hidden_number:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{hidden_number}'.")
            print(f"Let's try again, {user_name}!")
            return False

    print(f"Congratulations, {user_name}!")
    return True

def main():
    user_name = welcome_user()
    play_game(user_name)

if __name__ == "__main__":
    main()
