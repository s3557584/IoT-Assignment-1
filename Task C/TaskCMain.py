from game import Game
player1 = 0
player2 = 0

#Creating an object pointing to the Game class
gameObj = Game(player1, player2)

#Display instructions
gameObj.displayInstructions()

#Starts the game
gameObj.gameLogic()
