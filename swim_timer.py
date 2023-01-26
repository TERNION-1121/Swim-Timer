class EVENT(object):
    def __init__(self, event_number: int, event_distance: int, event_type: str, event_gender: str, heat: int):
        self.event_number = event_number
        self.event_distance = event_distance
        self.event_type = event_type
        self.event_gender = event_gender
        self.heat = heat

    def print_board(self, s1: object):
        print(f"Event {self.event_number}:     {self.event_distance}m {self.event_type} {self.event_gender}\nHeat {self.heat}")
        print(f"Lane\tName\t\tTiming\t\tRank")
        print(f"{s1.lane}\t{s1.name.ljust(15)}")

class SWIMMER(EVENT):
    def __init__(self, event_number: int, event_distance: int, event_type: str, event_gender: str, heat: int, lane: int, name: str):
        super().__init__(event_number, event_distance, event_type, event_gender, heat)
        assert lane >= 1 and lane <= 8, f"Lane {lane} is out of the range 1-8 (inclusive)!"
        self.lane = lane
        self.name = name


swimmer = SWIMMER(1, 200, "Freestyle", "Male", 1, 1, "PARTH")
event = EVENT(1, 200, "Freestyle", "Male", 1)
event.print_board(swimmer)