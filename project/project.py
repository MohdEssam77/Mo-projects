import random
import time

def main():
    languages = ["english", "german", "spanish", "arabic"]
    lang = input("Language: ")
    while lang not in languages:
        print("NOT AVAILABLE!")
        lang = input("Language: ")
    print(greeting(lang))
    DoYouWantToPlay = True
    while DoYouWantToPlay:
        print("1-> X and O     2-> Treasure chest     3-> Rock, Paper, Scissor")
        Game = input("Enter the number of the game you want to play: ")
        try:
            Game = int(Game)
        except:
            print("The value you entered is not a numerical value. ")
        while Game != 1 and Game != 2 and Game != 3 and Game != 999:
            Game = input("Number entered is wrong. Try again (if you want to exit type 999): ")
            try:
                Game = int(Game)
            except:
                print("The value you entered is not a numerical value. ")
            if Game == 999:
                DoYouWantToPlay = False
        if Game == 1:
            MainXandO()
            Y = input("If you want to play again or try another game press 1 if not then press 2: ")
            try:
                Y = int(Y)
            except:
                print("The value you entered is not a numerical value. ")
            while Y != 1 and Y != 2:
                Y = input("You entered a wrong number please choose 1 or 2: ")
                try:
                    Y = int(Y)
                except:
                    print("The value you entered is not a numerical value. ")
            if Y == 2:
                DoYouWantToPlay = False
            else:
                DoYouWantToPlay = True
        if Game == 2:
            X = 0
            Play = True
            while Play:
                Points = TreasurMain()
                X = X + Points
                DoUWant = input("If you want to continue playing enter 1 if not then enter 2: ")
                try:
                    DoUWant = int(DoUWant)
                except:
                    print("The value you entered is not a numerical value. ")
                while DoUWant != 1 and DoUWant != 2:
                    DoUWant = input("You entered a wrong number please choose 1 or 2: ")
                    try:
                        DoUWant = int(DoUWant)
                    except:
                        print("The value you entered is not a numerical value. ")
                if DoUWant == 2:
                    Play = False
                else:
                    Play = True
            print(f"Total points you got is {X}")
            z = input("If you want to play again or try another game press 1 if not then press 2: ")
            try:
                z = int(z)
            except:
                print("The value you entered is not a numerical value. ")
            while z != 1 and z != 2:
                z = input("You entered a wrong number please choose 1 or 2: ")
                try:
                    z = int(z)
                except:
                    print("The value you entered is not a numerical value. ")
            if z == 2:
                DoYouWantToPlay = False
            else:
                DoYouWantToPlay = True
        if Game == 3:
            R_P_S()
            A = input("If you want to play again or try another game press 1 if not then press 2: ")
            try:
                A = int(A)
            except:
                print("The value you entered is not a numerical value. ")
            while A != 1 and A != 2:
                A = input("You entered a wrong number please choose 1 or 2: ")
                try:
                    A = int(A)
                except:
                    print("The value you entered is not a numerical value. ")
            if A == 2:
                DoYouWantToPlay = False
            else:
                DoYouWantToPlay = True
    n = 3
    print("Thanks for choosing MoGames!")
    print(byebye(lang))
    while n > 0:
        print(n)
        time.sleep(1)
        n = n - 1

def game_validation(G):
    Game = G
    try:
        Game = int(Game)
    except:
        return ("The value you entered is not a numerical value. ")
    return Game
class TreasureChest:
    def __init__(self, que, ans, points):
        self.__Question = que
        self.__Ans = ans
        self.__Points = points
    def getQuestion(self):
        return self.__Question
    def CheckAns(self, ans):
        if ans == self.__Ans:
            return True
        else:
            return False
    def getPoint(self, Attempts):
        if Attempts > 4:
            return 0
        else:
            return int(self.__Points/Attempts)

Treasure = []
def read_data():
    Q1 = "2*2"
    A1 = 4
    P1 = 10
    New1 = TreasureChest(Q1, A1, P1)
    Treasure.append(New1)
    Q2 = "100/10"
    A2 = 10
    P2 = 15
    New2 = TreasureChest(Q2, A2, P2)
    Treasure.append(New2)
    Q3 = "4*1000"
    A3 = 4000
    P3 = 20
    New3 = TreasureChest(Q3, A3, P3)
    Treasure.append(New3)
    Q4 = "125/25"
    A4 = 5
    P4 = 25
    New4 = TreasureChest(Q4, A4, P4)
    Treasure.append(New2)
    Q5 = "3000+4000"
    A5 = 7000
    P5 = 18
    New5 = TreasureChest(Q5, A5, P5)
    Treasure.append(New5)

def TreasurMain():
    read_data()
    Choice = input("Enter Number between 1 and 5 inclusive: ")
    try:
        Choice = int(Choice)
    except:
        print("The value you entered is not a numerical value. ")
    count = 0
    while True:
        count += 1
        print(Treasure[Choice - 1].getQuestion())
        Answer = int(input("Ans: "))
        reply = Treasure[Choice - 1].CheckAns(Answer)
        if reply == True:
            break
    pointsAwarded = Treasure[Choice - 1].getPoint(count)
    print(f"You made {count} attempts before you got the final answer.")
    print(f"You got {pointsAwarded}!")
    return pointsAwarded
#make it in a loop


#NEW GAME Rock Paper Scissor


def R_P_S():
    Name = input("Enter your name: ")
    print("1. Rock     2. Paper     3. Scissor")

    Choice = input(f"{Name}! Choose what you want to play. 1, 2 or 3: ")
    try:
        Choice = int(Choice)
    except:
        print(f"{Name}! You entered a non numerical value! ")
    while Choice != 1 and Choice != 2 and Choice != 3:

        Choice = input(f"{Name}! You entered a wrong answer, please try again. ")
        try:
            Choice = int(Choice)
        except:
            print(f"{Name}! You entered a non numeric value! ")
    CompReply = random.randint(1,3)
    print(f"The computer choice was {CompReply}")
    if (Choice==1 and CompReply==3) or (Choice==2 and CompReply==1) or (Choice==3 and CompReply==2):
        print(f"{Name} Won! Computer lost!")
    elif (Choice==1 and CompReply==2) or (Choice==2 and CompReply==3) or (Choice==3 and CompReply==1):
        print(f"Computer won! {Name} lost! Try again.")
    else:
        print("Draw!")


#NEW GAME X and O

Grid = [[0 for x in range(3)] for y in range(3)]
array = [1,2,3,4,5,6,7,8,9]
CheckArray = [["1", "True"], ["2", "True"], ["3", "True"], ["4", "True"], ["5", "True"], ["6", "True"], ["7", "True"], ["8", "True"], ["9", "True"]]
def prepareGride():
    Num = input("Enter the number of rows and columns in the grid: ")
    try:
        Num = int(Num)
    except:
        print("The value you entered is not a numerical value. ")
    while Num != 3:
        Num = input("SORRY! only 3*3 grid is available. Try again: ")
        try:
            Num = int(Num)
        except:
            print("The value you entered is not a numerical value. ")
    Count = 0
    for i in range(Num):
        for j in range(Num):
            Grid[i][j] = Count + 1 + j
        Count += Num
    for x in range(Num):
        for y in range(Num):
            print(Grid[x][y], end="    ")
        print()


def YourTurn():
    ReturnedValue = "False"
    NumberToSearch = input("Enter the number where you want to play: ")
    try:
        NumberToSearch = int(NumberToSearch)
    except:
        print("The value you entered is not a numerical value. ")
    while NumberToSearch not in array:
        NumberToSearch = input("Number is unavailable! TRY AGAIN: ")
        try:
            NumberToSearch = int(NumberToSearch)
        except:
            print("The value you entered is not a numerical value. ")
    while CheckArray[NumberToSearch-1][1] != "True":
        NumberToSearch = input("This number was played before! TRY ANOTHER ONE: ")
        try:
            NumberToSearch = int(NumberToSearch)
        except:
            print("The value you entered is not a numerical value. ")
    for i in range(3):
        for j in range(3):
            if Grid[i][j] == NumberToSearch:
                Grid[i][j] = "x"
                CheckArray[NumberToSearch-1][1] = "x"
                #Vertical win check
                if (CheckArray[0][1]=="x") and (CheckArray[3][1]=="x") and (CheckArray[6][1]=="x"):
                    print("You won!")
                    ReturnedValue = "True"
                if (CheckArray[1][1]=="x") and (CheckArray[4][1]=="x") and (CheckArray[7][1]=="x"):
                    print("You won!")
                    ReturnedValue = "True"
                if (CheckArray[2][1]=="x") and (CheckArray[5][1]=="x") and (CheckArray[8][1]=="x"):
                    print("You won!")
                    ReturnedValue = "True"
                #Horizontal win check
                if (CheckArray[0][1] == "x") and (CheckArray[1][1] == "x") and (CheckArray[2][1] == "x"):
                    print("You won!")
                    ReturnedValue = "True"
                if (CheckArray[3][1] == "x") and (CheckArray[4][1] == "x") and (CheckArray[5][1] == "x"):
                    print("You won!")
                    ReturnedValue = "True"
                if (CheckArray[6][1] == "x") and (CheckArray[7][1] == "x") and (CheckArray[8][1] == "x"):
                    print("You won!")
                    ReturnedValue = "True"
                #Diagonal win check
                if (CheckArray[0][1] == "x") and (CheckArray[4][1] == "x") and (CheckArray[8][1] == "x"):
                    print("You won!")
                    ReturnedValue = "True"
                if (CheckArray[2][1] == "x") and (CheckArray[4][1] == "x") and (CheckArray[6][1] == "x"):
                    print("You won!")
                    ReturnedValue = "True"
                return ReturnedValue
    return ReturnedValue

def DisplayGrid():
    for x in range(3):
        for y in range(3):
            print(Grid[x][y], end="    ")
        print()


def CompTurn():
    ReturnedValue = "False"
    num = random.randint(1,9)
    while CheckArray[num-1][1] != "True":
        num = random.randint(1, 9)
    for i in range(3):
        for j in range(3):
            if Grid[i][j] == num:
                Grid[i][j] = "o"
                CheckArray[num-1][1] = "o"
                # Vertical win check
                if (CheckArray[0][1] == "o") and (CheckArray[3][1] == "o") and (CheckArray[6][1] == "o"):
                    print("Computer won!")
                    ReturnedValue = "True"
                if (CheckArray[1][1] == "o") and (CheckArray[4][1] == "o") and (CheckArray[7][1] == "o"):
                    print("Computer won!")
                    ReturnedValue = "True"
                if (CheckArray[2][1] == "o") and (CheckArray[5][1] == "o") and (CheckArray[8][1] == "o"):
                    print("Computer won!")
                    ReturnedValue = "True"
                # Horizontal win check
                if (CheckArray[0][1] == "o") and (CheckArray[1][1] == "o") and (CheckArray[2][1] == "o"):
                    print("Computer won!")
                    ReturnedValue = "True"
                if (CheckArray[3][1] == "o") and (CheckArray[4][1] == "o") and (CheckArray[5][1] == "o"):
                    print("Computer won!")
                    ReturnedValue = "True"
                if (CheckArray[6][1] == "o") and (CheckArray[7][1] == "o") and (CheckArray[8][1] == "o"):
                    print("Computer won!")
                    ReturnedValue = "True"
                # Diagonal win check
                if (CheckArray[0][1] == "o") and (CheckArray[4][1] == "o") and (CheckArray[8][1] == "o"):
                    print("Computer won!")
                    ReturnedValue = "True"
                if (CheckArray[2][1] == "o") and (CheckArray[4][1] == "o") and (CheckArray[6][1] == "o"):
                    print("Computer won!")
                    ReturnedValue = "True"
                return ReturnedValue
    return ReturnedValue


def MainXandO():
    prepareGride()
    Won = False
    print("1. You     2. Computer")

    First = input("Who will play first? ")
    try:
        First = int(First)
    except:
        print("The value you entered is not a numerical value. ")
    while First != 1 and First != 2:
        First = input("You entered a wrong answer, try again: ")
        try:
            First = int(First)
        except:
            print("The value you entered is not a numerical value. ")
    if First == 1:
        while not Won:
            You = YourTurn()
            DisplayGrid()
            if You == "True":
                Won = True
            else:
                print()
                print("Computer played. ")
                Computer = CompTurn()
                if Computer == "True":
                    Won = True
                DisplayGrid()
        if not Won:
            print("Draw!")
    else:
        while not Won:
            Computer = CompTurn()
            if Computer != "True":
                print("Computer played.")
            DisplayGrid()
            if Computer == "True":
                Won = True
                return
            else:
                print()
                print("Your Turn.")
                You = YourTurn()
                if You == "True":
                    Won = True
                    DisplayGrid()
                    return
                DisplayGrid()
        if not Won:
            print("Draw!")
            return

def greeting(lang):
    if lang.lower() == "english":
        return "HELLO!"
    if lang.lower() == "german":
        return "HALLO!"
    if lang.lower() == "spanish":
        return "HOLA!"
    if lang.lower() == "arabic":
        return "!مرحبا"

def byebye(lang):
    if lang.lower() == "english":
        return "BYE!"
    if lang.lower() == "german":
        return "TSCHUSS"
    if lang.lower() == "spanish":
        return "ADIOS!"
    if lang.lower() == "arabic":
        return "!الوداع"
#**********MAIN STARTS HERE**********#
if __name__ == "__main__":
    main()
