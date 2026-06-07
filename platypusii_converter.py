from modules.level_data import LevelData
from pathlib import Path
import json

LEVEL_DATA_EXTENSION = ".dat"
JSON_EXTENSION = ".json"
TITLE_TEXT = ("------------------------------------\n"
              "| Platypus II Level Data Converter |\n"
              "|        Update: 2026-06-08        |\n"
              "|    Developed by ASTRAN FELINE    |\n"
              "------------------------------------")
MENU = (f"\n(D)ecompile {LEVEL_DATA_EXTENSION} files\n"
        f"(R)ecompile {JSON_EXTENSION} files\n"
        f"(Q)uit")
DECOMPILE_PROMPT = f"Enter {LEVEL_DATA_EXTENSION} filename, leave blank to go back: "
RECOMPILE_PROMPT = f"Enter {JSON_EXTENSION} filename, leave blank to go back: "
QUIT_MESSAGE = "Goodbye!"


def main():
    print(TITLE_TEXT)
    print(MENU)
    user_choice = input(">>> ").upper()
    while user_choice != "Q":
        if user_choice == "D":
            decompile()
        elif user_choice == "R":
            recompile()
        else:
            print("Invalid choice!")
        print(MENU)
        user_choice = input(">>> ").upper()
    print(QUIT_MESSAGE)


def decompile():
    user_input = input(DECOMPILE_PROMPT)
    while user_input != "":
        input_file = Path(user_input)
        try:
            level_data = LevelData.from_bytes(input_file.read_bytes())
            if level_data.is_valid_bytes():
                input_file.with_suffix(JSON_EXTENSION).write_text(json.dumps(level_data.to_json(), indent=4))
        except FileNotFoundError:
            print(f"{input_file} not found!")
        user_input = input(DECOMPILE_PROMPT)


def recompile():
    user_input = input(RECOMPILE_PROMPT)
    while user_input != "":
        input_file = Path(user_input)
        try:
            level_data = LevelData.from_json(json.loads(input_file.read_text()))
            input_file.with_suffix(LEVEL_DATA_EXTENSION).write_bytes(level_data.to_bytes())
        except FileNotFoundError:
            print(f"{input_file} not found!")
        user_input = input(RECOMPILE_PROMPT)


main()