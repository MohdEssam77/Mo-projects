# MoGames
#### Video Demo:  https://youtu.be/fYyl_px-s0I
#### Description: This is my final project for the CS50x course from Harvard.
MoGames is a program fully written in python programming language. It consists of 3 games.
* X & O
* Treasure chest and
* Rock Paper Scissor
You can choose what to play. X & O can be played against random choices by the computer as well as rock paper scissor. While treasure chest game is for children as it contains some easy mathematical questions and can be played against your friend and find who is going to get more points (Try it but be fast while solving).
The first game (X and O):
I used to play this game with my brother and sister so I said why I don't play it with the computer but actually the computer is not always playing to win because it uses the random function from the random library in python. It consists of many functions like prepareGrid() which prepare a 3*3 grid to start your game, YourTurn() which asks the user to enter where he wants to play and it also checks whether this place was chosen before or not yet by checking the public 2D array and then checks whether you have won or not yet, DisplayGrid() which is the function called after each turn to display the new grid with the chosen numbers being selected either by the computer or by the user, CompTurn() is the function that makes a random choice of numbers between 1 and 9 inclusive and then checks whether it is available or no if not then it generates another one then finaly MainXandO() which is the main function to be called in the main program to start the game.
The second game (Treasure chest):
A game for children as it contains some easy mathematical questions and can be played against your friend and find who is going to get more points. It uses the object oriented programming style where the TreasureChest is a class with question, answer, points as private attributes. ReadData() is the procedure adding 5 questions to a public array declared as Treasure. TreasureMain() is the main function of this game that returns the number of points you got in the question chosed.
The third game (Rock, Paper, Scissor):
It is a 1 procedure game where you play against the computer itself. The procedure prints who won the game after that. You basically choose on of rock, paper or scissor to play and the computer chooses a random one as well and it checks who will win or whether it is a draw.
Finally, the main program where the program is running;
It uses a while loop to keep you in the program until you say that you want to leave. It uses try except everytime it asks the user to enter any value to validate it so that program will not get cracked.
* It asks the user to choose which game he/she wants to play and accordingly calls the suitable function or procedure. after the game ends it asks the user whether he wants to play again or try another game, if the user wants to leave then it goes out of the while loop after changing the value in the condition to False, else it repeats the same thing again by asking the user which game he wants to play and continue.