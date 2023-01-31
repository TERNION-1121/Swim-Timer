import time
import os

class EVENT():
    def __init__(self, event_number: int, event_distance: int, event_type: str, event_gender: str, heat: int, s1 = None, s2 = None, s3 = None, s4 = None):
        self.event_number = event_number
        self.event_distance = event_distance
        self.event_type = event_type
        self.event_gender = event_gender
        self.heat = heat
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.timer = 0.00

        self.swimmers = [self.s1, self.s2, self.s3, self.s4]

    def print_board(self):
        os.system('cls')
        print(f"Event {self.event_number}:     {self.event_distance}m {self.event_type} {self.event_gender}\t{self.timer:.2}\nHeat {self.heat}")
        print(f"Lane\tName\t\tTiming\t\tRank")
        if self.s1:
            print(f"{self.s1.lane}\t{self.s1.name.ljust(15)}\t{self.s1.timing}")
        if self.s2:
            print(f"{self.s2.lane}\t{self.s2.name.ljust(15)}\t{self.s2.timing}")
        if self.s3:
            print(f"{self.s3.lane}\t{s3.name.ljust(15)}\t{self.s3.timing}")
        if self.s4:
            print(f"{self.s4.lane}\t{s4.name.ljust(15)}\t{self.s4.timing}")

    def start_event(self):
        self.print_board()
        laps = self.event_distance // 100 
        rounds = { obj.lane:[obj, 0, True] for obj in self.swimmers }
        is_end = False
        finished = 0
        start = time.time()
        while not(is_end):
            lane_touched = int(input()) # enter lane number
            if rounds[lane_touched][2]:
                rounds[lane_touched][1]+=1
                rounds[lane_touched][0].timing = round(time.time() - start, 2)

                if rounds[lane_touched][1] == laps:
                        rounds[lane_touched][2] = False
                        finished += 1
                        self.print_board()

            if finished == 4:
                is_end = True
        end = time.time()
        self.timer = end - start

class SWIMMER():
    def __init__(self, lane: int, name: str):
        assert lane >= 1 and lane <= 4, f"Lane {lane} is out of the range 1-4 (inclusive)!"
        self.lane = lane
        self.name = name
        self.rank = None
        self.timing = None


s1 = SWIMMER(1, "PARTH")
s2 = SWIMMER(2, "AVIRAL")
s3 = SWIMMER(3, "KRISHNA")
s4 = SWIMMER(4, "VIKRANT")

event = EVENT(1, 200, "Freestyle", "Male", 1, s1, s2, s3, s4)
running = True
while running:
    event.start_event()