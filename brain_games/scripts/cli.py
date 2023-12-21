from prompt_toolkit import prompt

def welcome_user():

    name = prompt('May I have your name? ')
    print('Hello,', name)

def main():
    welcome_user()

if __name__ == '__main__':
    main()

