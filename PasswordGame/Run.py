#Script for running the game on the terminal
from Game import Game
from InputField import InvalidInput

game = Game()

while True:
    playerInput = input()

    if playerInput == "play":
        game = Game()
    elif playerInput == "stop":
        break
    elif playerInput == "next":
        if game.status == game.WON:
            game.startNextLevel()
        else:
            print("You haven't beat this level yet")
    elif game.status == game.PLAYING:
        try:
            game.attempt(playerInput)
        except InvalidInput as exc:
            print(exc.args[0])

    print(game)

    if game.status != game.PLAYING:
        game.active = False    

    