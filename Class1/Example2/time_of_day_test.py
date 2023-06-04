import time_of_day


def test_what_time_it_is():
    morning = 9
    day = 13
    evening = 19
    night = 2
    assert time_of_day.what_time_it_is(morning) == "Morning"
    assert time_of_day.what_time_it_is(day) == "Day"
    assert time_of_day.what_time_it_is(evening) == "Evening"
    assert time_of_day.what_time_it_is(night) == "Night"
