from enum import Enum


class Days(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def print_day(day):
    if isinstance(day, Days):
        print(f"The day is: {day.name} (Value: {day.value})")
    else:
        print("Not a valid day.")


print_day(Days.MONDAY)
print_day(Days.FRIDAY)
