# from brain_games.scripts.prompt
import prompt


def welcome_user():

    name = prompt.string('May I have your name? ')
    print('Hello,', name)


def main():
    welcome_user()


if __name__ == '__main__':
    main()
