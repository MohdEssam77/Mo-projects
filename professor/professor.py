import random
def main():
    score = 0
    lev = get_level()
    for _ in range(10):

        X = generate_integer(lev)
        Y = generate_integer(lev)
        question = f"{X} + {Y} = "
        tries = 0
        while True:
            tries += 1
            try:
                ans = int(input(f"{question}"))
                if (ans == (int(X) + int(Y))):
                    score += 1
                    break
                if (ans != (int(X) + int(Y))) and tries < 3:
                    print("EEE")
                    continue
                if tries == 3:
                    print(f"{question} {int(X) + int(Y)}")
                    break
            except ValueError:
                print("EEE")
                if tries == 3:
                    print(f"{question} {int(X) + int(Y)}")
                    break
                pass
    print(f"score: {score}")


def get_level():
    while True:
        a = input("Level: ")
        try:
            a = int(a)
        except ValueError:
            pass
        else:
            if not (1 <= a <= 3):
                continue
            else:
                break
    return a

def generate_integer(level):
    if not (1 <= level <= 3):
        raise ValueError
    if level == 1:
        return random.randint(0, 9)

    range_start = 10 ** (level - 1)
    range_end = (10 ** level) - 1
    return random.randint(range_start, range_end)


if __name__ == "__main__":
    main()
