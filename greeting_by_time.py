import time

timestamp = int(time.strftime("%H"))

if timestamp >= 1 and timestamp < 12:
    print("Good morning")
elif timestamp >= 12 and timestamp < 16:
    print("Good Afternoon")
else:
    print("Good Evening")



