numberOfDay = int(input())

def weekDays (argument):
    switcher = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    return switcher.get(argument, "Error")
print(weekDays(numberOfDay))




