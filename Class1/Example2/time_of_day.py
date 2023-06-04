from datetime import datetime


def what_time_it_is(current_time):
    if 4 <= current_time < 12:
        return "Morning"
    elif 12 <= current_time < 18:
        return "Day"
    elif 18 <= current_time < 22:
        return "Evening"
    elif (22 <= current_time < 24) or (0 <= current_time < 4):
        return "Night"


current = datetime.now().time().hour
print(what_time_it_is(current))
