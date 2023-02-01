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
    
    @staticmethod
    def convert_time(time):
        if time < 60:
            return round(time, 2)
        else:
            min, sec = divmod(time, 60)
            return f'{int(min)}:{sec:.3}'

    def print_board(self):
        os.system('cls')
        print(f"Event {self.event_number}:     {self.event_distance:3}m {self.event_type} {self.event_gender}\t{EVENT.convert_time(self.timer)}s\nHeat {self.heat}")
        print(f"Lane\tName\t\tTiming\t\tRank")
        if self.swimmers[0]:
            print(f"{self.swimmers[0].lane}\t{self.swimmers[0].name.ljust(15)}\t{EVENT.convert_time(self.swimmers[0].timing) if self.swimmers[0].timing else ''}\t\t{self.swimmers[0].rank if self.swimmers[0].rank else ''}")
        if self.swimmers[1]:
            print(f"{self.swimmers[1].lane}\t{self.swimmers[1].name.ljust(15)}\t{EVENT.convert_time(self.swimmers[1].timing) if self.swimmers[1].timing else ''}\t\t{self.swimmers[1].rank if self.swimmers[1].rank else ''}")
        if self.swimmers[2]:
            print(f"{self.swimmers[2].lane}\t{self.swimmers[2].name.ljust(15)}\t{EVENT.convert_time(self.swimmers[2].timing) if self.swimmers[2].timing else ''}\t\t{self.swimmers[2].rank if self.swimmers[2].rank else ''}")
        if self.swimmers[3]:
            print(f"{self.swimmers[3].lane}\t{self.swimmers[3].name.ljust(15)}\t{EVENT.convert_time(self.swimmers[3].timing) if self.swimmers[3].timing else ''}\t\t{self.swimmers[3].rank if self.swimmers[3].rank else ''}")

    def start_event(self):
        self.print_board()
        input('Press Enter to start the event ')

        laps = self.event_distance // 100 if self.event_distance != 50 else 1
        rounds = {obj.lane:[obj, 0, True] for obj in self.swimmers}
        
        is_end = False
        finished = 0
        start = time.time()
        while not(is_end):
            self.timer = time.time() - start
            self.print_board()
            lane_touched = int(input())

            if rounds[lane_touched][2]: 
                rounds[lane_touched][1]+=1
                rounds[lane_touched][0].timing = round((time.time()) - start, 2)

                if rounds[lane_touched][1] == laps:
                        rounds[lane_touched][2] = False
                        finished += 1
                        rounds[lane_touched][0].rank = finished
                        self.print_board()

            if finished == 4:
                is_end = True
        end = time.time()
        self.timer = end - start
        self.print_board()
    
    def show_results(self):
        os.system('cls')
        self.swimmers.sort(key= lambda obj: obj.rank)
        self.print_board()
        input()

    def __repr__(self):
        return f"{self.event_number}- Heat {self.heat}: {self.event_distance}m {self.event_type} {self.event_gender}"

class SWIMMER():
    def __init__(self, lane: int, name: str):
        assert lane >= 1 and lane <= 4, f"Lane {lane} is out of the range 1-4 (inclusive)!"
        self.lane = lane
        self.name = name
        self.rank = None
        self.timing = None
    
    def __repr__(self):
        return f'SWIMMER({self.lane}, {self.name}, {self.rank})'

s1 = SWIMMER(1, "PARTH")
s2 = SWIMMER(2, "AVIRAL")
s3 = SWIMMER(3, "KRISHNA")
s4 = SWIMMER(4, "VIKRANT")

sf1 = SWIMMER(1, "AASHNA")
sf2 = SWIMMER(2, "DIKSHA")
sf3 = SWIMMER(3, "GARGI")
sf4 = SWIMMER(4, "AVNI")

BS = EVENT(1, 100, "Breaststroke", "Male", 1, s1, s2, s3, s4)
FS = EVENT(2, 50, "Freestyle", "Female", 1, sf1, sf2, sf3, sf4)
events = (BS, FS)

for eve in events:
    eve.start_event()
    eve.show_results()