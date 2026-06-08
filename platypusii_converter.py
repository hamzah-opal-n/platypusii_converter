from modules.level_data import LevelData
from pathlib import Path
import json

LEVEL_DATA_EXTENSION = ".dat"
JSON_EXTENSION = ".json"
TITLE_TEXT = ("------------------------------------\n"
              "| Platypus II Level Data Converter |\n"
              "|        Update: 2026-06-09        |\n"
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
            if level_data.is_valid:
                output_file = input_file.with_suffix(JSON_EXTENSION)
                overwrite = overwrite_warning(output_file)
                if overwrite:
                    output_file.write_text(json.dumps(level_data.to_json(), indent=4))
                    print(f"Wrote to {output_file}")
                else:
                    print("Conversion cancelled")
            else:
                print(f"{input_file} is not a valid level data file!")
        except FileNotFoundError:
            print(f"{input_file} not found!")
        user_input = input(DECOMPILE_PROMPT)


def recompile():
    user_input = input(RECOMPILE_PROMPT)
    while user_input != "":
        input_file = Path(user_input)
        try:
            level_data = LevelData.from_json(json.loads(input_file.read_text()))
            if level_data.is_valid:
                output_file = input_file.with_suffix(LEVEL_DATA_EXTENSION)
                overwrite = overwrite_warning(output_file)
                if overwrite:
                    output_file.write_bytes(level_data.to_bytes())
                    print(f"Wrote to {output_file}")
                else:
                    print("Conversion cancelled")
            else:
                print(f"{input_file} contains invalid data!")
        except FileNotFoundError:
            print(f"{input_file} not found!")
        except json.decoder.JSONDecodeError:
            print(f"{input_file} is not a valid JSON file!")
        user_input = input(RECOMPILE_PROMPT)


def overwrite_warning(filepath: Path):
    if filepath.exists():
        choice = input(f"{filepath} already exists! Overwrite? (Y/N) ").upper()
        return choice == "Y"
    else:
        return True


main()