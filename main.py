#!/usr/bin/env python3
import sys
import os

from functions.add import handle_add
from db_services.db_text import create

create()

def main():
    words = sys.argv
    lword = len(words)
    if lword <= 1 or lword >= 5:
        print("\n--- Project DocuMind ---")
        print("Usage: Docu add <file_name> OR Docu add <file_name> <file_path>")
        print("\nSetup: alias Docu='/your_path/main.py' in .bashrc")
        sys.exit(1)
    command = words[2:]
    command_len = len(command)
    if command_len == 1:
        handle_add(command[0])
    elif command_len == 2:
        handle_add(command[0], command[1])

if __name__ == "__main__":
    main()