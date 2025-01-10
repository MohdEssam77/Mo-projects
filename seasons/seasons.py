from datetime import date
import sys
import inflect


def main():
    birthdate = input("Date of Birth: ")
    try:
        array = birthdate.split('-')
        if len(array[0]) != 4 or len(array[1]) != 2 or len(array[2]) != 2 or not (1 <= int(array[1]) <= 12) or not (1 <= int(array[2]) <= 31):
            sys.exit("Invalid date")
        else:
            y = int(array[0])
            m = int(array[1])
            d = int(array[2])
    except:
        sys.exit("Invalid date")
    else:
        print(calculate(y, m, d))




def calculate(y, m, d):
    p = inflect.engine()
    num = date.today() - date(y, m, d)
    num = str(num)
    days, w1, w2 = num.split(' ')
    days = int(days)
    minutes = days * 24 * 60
    if minutes < 0:
        minutes = minutes * -1
    words = p.number_to_words(minutes, andword="")
    words = words.capitalize() + " minutes"
    return words


if __name__ == "__main__":
    main()
