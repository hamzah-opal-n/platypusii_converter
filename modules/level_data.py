from modules.event import Event

class LevelData:
    """Level Data"""
    def __init__(self, input_data):
        self._length = len(input_data)
        if self.is_valid():
            self.events = []
            for offset in range(0, len(input_data), 40):
                self.events.append(Event.from_bytes(input_data[offset:offset + 40]))

    def __str__(self):
        if self.is_valid():
            return "Platypus II level data"
        else:
            return "Invalid level data file"

    def __repr__(self):
        self.__str__()

    def is_valid(self):
        return self._length % 4 == 0

    def to_json(self):
        output_json = []
        for event in self.events:
            output_json.append(event.to_json())
        return output_json