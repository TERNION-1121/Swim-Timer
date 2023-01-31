import time

class EVENT(object):
    def __init__(self, event_number: int, event_distance: int, event_type: str, event_gender: str, heat: int):
        self.event_number = event_number
        self.event_distance = event_distance
        self.event_type = event_type
        self.event_gender = event_gender
        self.heat = heat

    def print_board(self, s1 = None, s2 = None, s3 = None, s4 = None):
        print(f"Event {self.event_number}:     {self.event_distance}m {self.event_type} {self.event_gender}\nHeat {self.heat}")
        print(f"Lane\tName\t\tTiming\t\tRank")
        if s1:
            print(f"{s1.lane}\t{s1.name.ljust(15)}\t{s1.timing}")
        if s2:
            print(f"{s2.lane}\t{s2.name.ljust(15)}\t{s2.timing}")
        if s3:
            print(f"{s3.lane}\t{s3.name.ljust(15)}\t{s3.timing}")
        if s4:
            print(f"{s4.lane}\t{s4.name.ljust(15)}\t{s4.timing}")

    def start_event(self):
        pass
class SWIMMER(EVENT):
    def __init__(self, event_number: int, event_distance: int, event_type: str, event_gender: str, heat: int, lane: int, name: str):
        super().__init__(event_number, event_distance, event_type, event_gender, heat)
        assert lane >= 1 and lane <= 4, f"Lane {lane} is out of the range 1-4 (inclusive)!"
        self.lane = lane
        self.name = name
        self.rank = None
        self.timing = None


s1 = SWIMMER(1, 200, "Freestyle", "Male", 1, 1, "PARTH")
s2 = SWIMMER(1, 200, "Freestyle", "Male", 1, 2, "AVIRAL")
s3 = SWIMMER(1, 200, "Freestyle", "Male", 1, 3, "KRISHNA")
s4 = SWIMMER(1, 200, "Freestyle", "Male", 1, 4, "VIKRANT")

event = EVENT(1, 200, "Freestyle", "Male", 1)
event.print_board(s1, s2, s3)