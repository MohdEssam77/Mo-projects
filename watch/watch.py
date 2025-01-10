import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        if URL := re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-zA-z0-9]+)", s):
            array = URL.groups()
            return "https://youtu.be/" + array[3]





if __name__ == "__main__":
    main()
