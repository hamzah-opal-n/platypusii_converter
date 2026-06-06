from modules.level_data import LevelData
from modules.event import Event
import os
import json
import struct

TEST_EVENT_BYTES = b'\x00\x00\x00\x00\x07\x00\x00\x00h\x01\x00\x00\xfe\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
LEVEL_DATA_EXTENSION = ".dat"
JSON_EXTENSION = ".json"
TITLE_TEXT = ("------------------------------------\n"
              "| Platypus II Level Data Converter |\n"
              "|        Update: 2026-03-06        |\n"
              "|    Developed by ASTRAN FELINE    |\n"
              "------------------------------------")
MENU = (f"\n(D)ecompile {LEVEL_DATA_EXTENSION} file\n"
        f"(R)ecompile {JSON_EXTENSION} files (Not working yet!)\n"
        f"(Q)uit")
DECOMPILE_PROMPT = "Enter level data filename, leave blank to go back: "
RECOMPILE_PROMPT = "Enter json filename, leave blank to go back: "
ERROR_MESSAGE = "Invalid file!"
QUIT_MESSAGE = "Goodbye!"
SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


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
    input_file = input(DECOMPILE_PROMPT)
    while input_file != "":
        if input_file[-len(LEVEL_DATA_EXTENSION):] != LEVEL_DATA_EXTENSION:
            input_file = input_file + LEVEL_DATA_EXTENSION
        try:
            convert_level_data(input_file)
        except FileNotFoundError:
            print(f"{input_file} does not exist!")
        input_file = input(DECOMPILE_PROMPT)


def convert_level_data(filename):
    with open(filename, "rb") as input_file:
        raw_data = input_file.read()
    level_data = LevelData(raw_data)
    if level_data.is_valid():
        with open(f"{os.path.join(filename[:-len(LEVEL_DATA_EXTENSION)])}{JSON_EXTENSION}", "w") as out_file:
            out_file.write(json.dumps(level_data.to_json(), indent=4))

    else:
        print(ERROR_MESSAGE)


def recompile():
    print("This doesn't work yet! Please use the old version in the Claymatic Discord server if you want to recompile data, or wait for this to be implemented at a later date!")


def recompile_old():
    input_file = input(RECOMPILE_PROMPT)
    while input_file != "":
        if input_file[-len(JSON_EXTENSION):] != JSON_EXTENSION:
            input_file = input_file + JSON_EXTENSION
        try:
            convert_json(input_file)
        except FileNotFoundError:
            print(f"{input_file} does not exist!")
        input_file = input(RECOMPILE_PROMPT)


def convert_json(filename):
    with open(filename) as input_file:
        json_data = json.load(input_file)
    output_string = b""
    for event in json_data:
        event_bytes = struct.pack("<iiiiiiiiii",
                                  event["wait"],
                                  event["cmd"],
                                  event["arg1"],
                                  event["arg2"],
                                  event["arg3"],
                                  event["arg4"],
                                  event["arg5"],
                                  event["arg6"],
                                  event["arg7"],
                                  event["arg8"])
        output_string += event_bytes
    with open(f"{os.path.join(filename)}.dat", "wb") as out_file:
        out_file.write(output_string)


def test_decompile():
    convert_level_data("level0.dat")
    convert_level_data("level1.dat")
    convert_level_data("level2.dat")
    convert_level_data("level3.dat")
    convert_level_data("level4.dat")
    convert_level_data("level5.dat")


main()
# test_decompile()