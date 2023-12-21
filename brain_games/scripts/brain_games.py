#!/usr/bin/env python3
from ast import main
from cli import welcome_user


def show_greeting():
    text = 'Welcome to the Brain Games!'
    print(text)

def main():
    show_greeting()

    welcome_user()    

if __name__ == '__main__':

    main()
    
    
