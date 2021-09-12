def add_time(start, duration, *args):
    [S, AP] = start.split(" ")
    [H, M] = S.split(":")
    [HD, MD] = duration.split(":")

    Days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

    minutes = int(M) + int(MD)
    hours = int(H) + int(HD)

    if minutes >= 60:
        hours = hours + 1
        minutes = minutes - 60

    # finding the total number of days
    days_later = round(hours / 24)
    # making the hours to 12 and using count to find AM or PM (odd/even)
    count = 0
    while hours >= 12:
        count = count + 1
        hours = hours - 12

    if hours == 0:
        hours = 12

    if count % 2 == 0:
        AP = "AM" if AP == "AM" else "PM"
    else:
        AP = "PM" if AP == 'AM' else "AM"

    # adding zeros in front of a number
    minutes_str = str(minutes)
    zero_fill_minutes = minutes_str.zfill(2)

    new_time = str(hours) + ":" + zero_fill_minutes + " {}".format(AP)

    if args:
        day = args[0].title()
        # [0] in the end to get the key out of the list
        key = [k for k, v in Days.items() if v == day][0]

        x = key + days_later
        # print(x)
        if x <= 7:
            y = Days.get(x)
            # print(y)
            new_time = new_time + ", {}".format(y)
        else:
            while x > 7:
                x = x - 7
                y = Days.get(x)
            # attention to where line 54 starts! If it starts earlier it will be under the first if(We will get: DAY,
            # DAY)
            new_time = new_time + ", {}".format(y)

    # last we print the days later if they exist. AP = "AM" because the day changes from PM to AM!
    if days_later == 1 and AP == "AM":
        new_time = new_time + " (next day)"
    elif days_later > 1:
        new_time = new_time + " ({} days later)".format(days_later)

    return new_time

