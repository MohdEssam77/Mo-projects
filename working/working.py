import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if isFormat := re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s):
        grps = isFormat.groups()
        if int(grps[1]) > 12 or int(grps[5]) > 12:
            raise ValueError
        time1 = perfect(grps[1], grps[2], grps[3])
        time2 = perfect(grps[5], grps[6], grps[7])
        return time1 + " to " + time2
    raise ValueError


def perfect(H, M, T):
    if T.lower() == "pm":
        if int(H) == 12:
            h = "12"
        else:
            h = str(int(H) + 12)
    else:
        if int(H) == 12:
            h = "00"
        else:
            h = "0"+H
    if M == None:
        m = ":00"
        Time = h + m
    else:
        Time = h + ":" + M
    return Time


if __name__ == "__main__":
    main()
