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

            # Populate action name
            try:
                self.action_name = ACTIONS[self.action_number][0]
            except IndexError:
                self.action_name = self.action_number

            # Populate arg names
            try:
                for i in range(len(ACTIONS[self.action_number][1])):
                    self.arg_names[i] = ACTIONS[self.action_number][1][i]
            except IndexError:
                pass

            # Enemy and scenery type and arg names
            if (self.action_number >= 21) and (self.action_number <= 23):
                object_dict = ENEMIES
                if self.action_number == 23:  # spawnScenery
                    object_dict = SCENERY
                # Enemy and scenery name
                try:
                    self.arg_values_text[0] = object_dict[self.arg_values[0]][0]
                    if self.action_number > 21:
                        for i in range(len(object_dict[self.arg_values[0]][1])):
                            self.arg_names[i+1] = object_dict[self.arg_values[0]][1][i]
                except IndexError:
                    self.arg_values_text[0] = self.arg_values[0]

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
                self.action_number = ACTION_INDEXES[self.action_name]

            # Loading argument values from json/text
            for arg_value in self.arg_values_text:
                if type(arg_value) is int:
                    self.arg_values.append(arg_value)
                else:
                    object_dict = ENEMY_INDEXES
                    if self.action_number == 23:  # spawnScenery
                        object_dict = SCENERY_INDEXES
                    self.arg_values.append(object_dict[arg_value])


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