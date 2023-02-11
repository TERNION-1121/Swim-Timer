<h1 align="center">Swim Timer</h1>

A *Timing System for Swimming*[^1] made in Python.

![image](https://user-images.githubusercontent.com/97667653/218270221-9a2a1684-0fe7-4345-82f6-9ed8f7488246.png)


## `class EVENT()`
This class houses the event details, such as:
- Event Number
- Heat Number
- Event Type
- Event Distance
- Event Gender, etc.

For the sake of simplicity, rather than having 8 swimmer lanes, the project has 4 swimmer lanes.

## `class SWIMMER()`

The objects of this class houses details of each swimmer:
- Swimmer's lane
- Swimmer's name
- Swimmer's rank and timing (upon finishing the race)

### `print_board()`

It prints/displays the board that consists of the Event's details, with its corresponding participants.

```py
s1 = SWIMMER(1, "PARTH")
s2 = SWIMMER(2, "AVIRAL")
s3 = SWIMMER(3, "KRISHNA")
s4 = SWIMMER(4, "VIKRANT")

BS = EVENT(1, 100, "Breaststroke", "Male", 1, s1, s2, s3, s4)
```
<br>

![image](https://user-images.githubusercontent.com/97667653/218269894-dbf645ef-b166-4163-956b-4c335b2d8555.png)

> Example use case of the `print_board()` function with the above code

### `start_event()`

To start a event, press `enter`. Doing so starts the timer. As per the distance of the race, we get the number of laps of 100m each swimmer has to make.
Using the statement `self.event_distance // 100 if self.event_distance`. If the distance is 50m, the number of laps is set to 1.

<br>

Now after the start, each lane number has to be entered as that lane's swimmer touches the touchpad.
So the timer stops as soon as `number of lanes * number of laps` lines of input has been entered after start.

See the below example.

> would be soon added

### `show_result()`

As soon as the `start_event()` function terminates, the partcipants, who were earlier sorted on the basis of their lane numbers, are now sorted on the basis of their rank numbers.

![image](https://user-images.githubusercontent.com/97667653/218270753-a1fb4d42-844b-4c7c-96d8-26cff63fd431.png)

> Example use case where the above shown event, has finished

<hr>

#### P.S.

This thus concludes our basic Swim Timer in Python. I got the idea for this project while I was out for a swimming competition. It was fun back then, thinking about how such a system would operate. And now I tried recreating it :) I hope I could work on a similar project, but as a real-time one. Soon probably!

[^1]: To understand how does a Timing System in the sport of swimming works, watch this [video](https://www.youtube.com/watch?v=wvvun6Muc6E)
