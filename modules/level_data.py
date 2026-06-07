from modules.event import Event

class LevelData:
    """Level Data"""
    def __init__(self, input_format, input_data):
        self.events = []
        self._length = len(input_data)
        if input_format == "bytes":
            if self.is_valid_bytes():
                for offset in range(0, len(input_data), 40):
                    self.events.append(Event.from_bytes(input_data[offset:offset + 40]))
        elif input_format == "JSON":
            for item in input_data:
                self.events.append(Event.from_json(item))

    def __str__(self):
        if self.is_valid_bytes():
            return "Platypus II level data"
        else:
            return "Invalid level data file"

    def __repr__(self):
        self.__str__()

    @classmethod
    def from_bytes(cls, input_bytes):
        return cls("bytes", input_bytes)

    @classmethod
    def from_json(cls, input_json):
        return cls("JSON", input_json)

    def is_valid_bytes(self):
        return self._length % 4 == 0

    def to_json(self):
        output_json = []
        for event in self.events:
            output_json.append(event.to_json())
        return output_json

    def to_bytes(self):
        output_string = b""
        for event in self.events:
            output_string += event.to_bytes()
        return output_string