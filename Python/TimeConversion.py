import sys

#time = raw_input().strip()

time = "02:00:00PM"

hms = time.split(":")

hours = int(hms[0])

if hms[2][2] == 'P':

    if hours != 12:
        hours += 12
        hms[0] = str(hours)

if hms[2][2] == 'A' and hours == 12:
    hms[0] = "00"

hms[2] = hms[2][:-2]

print ":".join(hms)
