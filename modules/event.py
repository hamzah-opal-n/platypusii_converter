from modules.names import *

import struct

class Event:

    def __init__(self, input_format, input_data):
        self.arg_values = []
        self.arg_names = []
        self.arg_values_text = []

        # Create event from bytes
        if input_format == "bytes":
            self.wait, self.action_number = struct.unpack("<ii", input_data[:8])
            self.arg_values = list(struct.unpack("<iiiiiiii", input_data[8:]))
            self.arg_values_text = [value for value in self.arg_values]
            for i in range(8):
                self.arg_names.append(f"arg{i + 1}")

            # Population action name
            if self.action_number in ACTION_NAMES:
                self.action_name = ACTION_NAMES[self.action_number]
            else:
                self.action_name = self.action_number

            # Populate arg names
            if self.action_number in ACTION_ARG_NAMES:
                for i in range(len(ACTION_ARG_NAMES[self.action_number])):
                    self.arg_names[i] = ACTION_ARG_NAMES[self.action_number][i]

            # Enemy and scenery type and arg names
            if self.arg_names[0] == "object":
                object_dict = ENEMY_NAMES
                arg_dict = ENEMY_ARG_NAMES
                if self.action_number == 23:  # spawnScenery
                    object_dict = SCENERY_NAMES
                    arg_dict = SCENERY_ARG_NAMES
                # Enemy and scenery name
                if self.arg_values[0] in object_dict:
                    self.arg_values_text[0] = object_dict[self.arg_values[0]]
                else:
                    self.arg_values_text[0] = self.arg_values[0]
                # Enemy and scenery arg names
                if self.arg_values[0] in arg_dict:
                    for i in range(len(arg_dict[self.arg_values[0]])):
                        self.arg_names[i+1] = arg_dict[self.arg_values[0]][i]

        # Create event from JSON
        elif input_format == "JSON":
            self.wait = input_data["wait"]
            self.action_name = input_data["action"]
            for arg_name, arg_value in input_data["args"].items():
                self.arg_names.append(arg_name)
                self.arg_values_text.append(arg_value)

            # Get action number from name
            if type(self.action_name) is int:
                self.action_number = self.action_name
            else:
                try:
                    self.action_number = [number for number, name in ACTION_NAMES.items() if self.action_name == name][0]
                except IndexError:
                    print(f"Error loading event: unknown action: {self.action_name} encountered")

            # Loading argument values from json/text
            for arg_value in self.arg_values_text:
                if type(arg_value) is int:
                    self.arg_values.append(arg_value)
                else:
                    object_dict = ENEMY_NAMES
                    if self.action_number == 23:  # spawnScenery
                        object_dict = SCENERY_NAMES
                    try:
                        self.arg_values.append([number for number, name in object_dict.items() if arg_value == name][0])
                    except IndexError:
                        print(f"Error loading event: unknown object: {arg_value} encountered")


        # If no format specified - use dummy values
        else:
            self.wait = 0
            self.action_number = 0
            self.action_name = "None"
            for i in range(8):
                self.arg_values.append(0)
                self.arg_names.append(f"arg{i+1}")


    def __str__(self):
        event_string = (f"[EVENT INFORMATION]\n"
                        f"Wait: {self.wait}\n"
                        f"Action: {self.action_number} - {self.action_name}\n"
                        f"Args:\n")
        for i in range(8):
            event_string += f"\t{self.arg_names[i]}: {self.arg_values[i]}\n"
        return event_string


    def __repr__(self):
        self.__str__()


    def to_json(self):
        output_json = {
            "wait": self.wait,
            "action": self.action_name,
            "args": dict(zip(self.arg_names, self.arg_values_text))
        }
        return output_json


    def to_bytes(self):
        data_to_pack = [self.wait, self.action_number] + self.arg_values
        output_bytes = struct.pack("<iiiiiiiiii", *data_to_pack)
        return output_bytes


    @classmethod
    def from_bytes(cls, input_bytes):
        return cls("bytes", input_bytes)


    @classmethod
    def from_json(cls, input_json):
        return cls("JSON", input_json)