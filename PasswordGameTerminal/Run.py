#Script for running the game on the terminal
import PasswordGame

game = PasswordGame.Game()

while True:
    playerInput = input()

    if playerInput == "play":
        game = PasswordGame.Game()
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
        except PasswordGame.InvalidInput as exc:
            print(exc.args[0])

    print(game)

    if game.status != game.PLAYING:
        game.active = False    

    