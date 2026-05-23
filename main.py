#!/usr/bin/env python3
import sys

from db_services.db_text import create
from functions.add import handle_add
from functions.ask import handle

create()

def main():
    words = sys.argv
    lword = len(words)
    word_pass = len(words[2:])
    if word_pass > 3 or word_pass == 0:
        print("\n--- Project DocuMind ---")
        print("\nSetup: alias DocuMind(or Docu)='/your_path/main.py' in .bashrc")
        print('''\n Available commands in DocuMind: 
        1. Docu add <file_name> <file_path>. \nwill add your file, that it can be worked with \nwithout specifying a path it will search on the desktop
        2. Docu ask <file_name> <your_question>. \nWill answer your question. The file MUST be added via Document Add.''')
        sys.exit(1)
    if words[1] == "add":
        command = words[2:]
        command_len = len(command)
        if command_len == 1:
            handle_add(command[0])
        elif command_len == 2:
            handle_add(command[0], command[1])
    elif words[1] == "ask":
        try:
            final_answer = handle(words[2], words[3])
            print(final_answer)
        except Exception as e:
            print("Sorry! Something went wrong!")
            print("If you want to add file or question, please write: \n Docu add <file_name> <file_path")
            print(f"Error's name: {e}")
    else:
        print("Somethind went wrong... Work commands: add, ask")

if __name__ == "__main__":
    main()