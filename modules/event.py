from modules.names import *

import struct

class Event:

    def __init__(self, input_format, input_data):
        self.arg_values = []
        self.arg_names = []
        self.arg_values_text = []
        for i in range(8):
            self.arg_names.append(f"arg{i + 1}")

        if input_format == "bytes":
            self.wait, self.action_number = struct.unpack("<ii", input_data[:8])
            arg_data = struct.unpack("<iiiiiiii", input_data[8:])

            for arg in arg_data:
                self.arg_values.append(arg)
            if self.action_number in ACTION_NAMES:
                self.action_name = ACTION_NAMES[self.action_number]
            else:
                self.action_name = f"unknownAction{self.action_number}"

            if self.action_name in ARG_NAMES:
                for i in range(len(ARG_NAMES[self.action_name])):
                    self.arg_names[i] = ARG_NAMES[self.action_name][i]

            for i in range(8):
                if self.arg_names[i] == "object":
                    object_dict = ENEMY_NAMES
                    if self.action_name == "spawnScenery":
                        object_dict = SCENERY_NAMES
                    self.arg_values_text.append(object_dict[self.arg_values[i]])
                else:
                    self.arg_values_text.append(self.arg_values[i])

        elif input_format == "json":
            self.wait = input_data["wait"]
            self.action_name = input_data["action"]

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
        return cls("json", input_json)