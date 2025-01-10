def count_letters(string):
    letters = 0
    for i in range(len(string)):
        if string[i] >= 'a' and string[i] <= 'z':
            letters += 1
    return letters


def count_words(string):
    words = 0
    for i in range(len(string)):
        if string[i] == ' ':
            words += 1
    return words + 1


def count_sentences(string):
    sentences = 0
    for i in range(len(string)):
        if string[i] == '.' or string[i] == '?' or string[i] == '!':
            sentences += 1
    return sentences


# main program stars here*****
str = input("Text: ")
str = str.lower()
letters = count_letters(str)
words = count_words(str)
sentences = count_sentences(str)
L = (letters / words) * 100
S = (sentences / words) * 100
index = round(0.0588 * L - 0.296 * S - 15.8)
if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")