from electronicDie import ElectronicDie
from sense_hat import SenseHat
import time
import csv
import os.path
from os import path
from datetime import datetime

#Creating an object pointing to the SenseHat class
sense = SenseHat()

#Creating an object pointing to the ElectronicDie class
electronicDieObj = ElectronicDie()

class Game:
    player1 = 0
    player2 = 0
    playerTurn = True
    
    #Constructor for the class 
    #The two parameters are the starting score for the two players
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
    #This function records the winner score to the winner.csv file
    def recordResult(self, player, score, date, time):
        
        #To check if the winner.csv file exists
        if path.exists("winner.csv") == True:
             
             #If the file exists append result to existing file
             with open('winner.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([player, score, date, time])
                
        #If file does not exists create the file and append the result
        else:
            with open('winner.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerow([player, score, date, time])
        
    #This function gets the accelorometer values from the sensehat
    def getAccelerometer(self):
        
        #Gets the values of 3 diffrent axis from the sensehat
        a, b, c = sense.get_accelerometer_raw().values()
        
        a = abs(a)
        b = abs(b)
        c = abs(c)
        
        return a,b,c
    
    #This function is a wait for user input function
    #The following code will wait until user shakes the PI before continueing the code
    def wait_until(self):
            
        #Calls the getAccelerometer() function
        x = self.getAccelerometer()
        
        #Check if user shakes the PI
        if x[0] > 1.4 or x[1] > 1.4 or x[2] > 1.4:
            return True
        else:
            return False
    
    #This function is to display instructions through the sense hat before starting the game
    def displayInstructions(self):
        sense.show_message("Welcome!")
        sense.show_message("This is a simple two player electronic die-based game created for the Raspberry Pi")
        sense.show_message("Each player will take turns rolling the die by shaking the Raspberry Pi")
        sense.show_message("Whoever reaches a total score of 30 or above wins")
        sense.show_message("Are you ready? Shake to start!!!")
        
        #Wait for the user to shake the PI before continueing
        while not self.wait_until():
                time.sleep(0.01)
    
    #This function contains the code for the game
    def gameLogic(self):
        
        #While both of the player's score is below 30 keep looping
        while self.player1 < 30 and self.player2 < 30:
            
            #Check for which player's turn
            #Player 1 = True, Player 2 = False
            if self.playerTurn == True:
                
                #Telling the user is Player 1's turn
                sense.show_message("Player 1's Turn!!!")
                
                #Wait for the user to shake the PI before continueing
                while not self.wait_until():
                    time.sleep(0.01)
                
                #Updates player's total score after shaking the dice
                self.player1 = self.player1 + electronicDieObj.roll_dice()
                
                #Display player's current total score on the console
                print "Player 1's Current Score:",self.player1
                time.sleep(2)
                sense.clear()
                
                #Assign turn to player 2
                self.playerTurn = False
                
            #Check if its player 2's turn
            elif self.playerTurn == False:
                
                #Telling the user is Player 2's turn
                sense.show_message("Player 2's Turn!!!")
                
                #Wait for the user to shake the PI before continueing
                while not self.wait_until():
                    time.sleep(0.01)
                
                #Updates player's total score after shaking the dice
                self.player2 = self.player2 + electronicDieObj.roll_dice()
                
                #Display player's current total score on the console
                print "Player 2's Current Score:",self.player2
                time.sleep(2)
                sense.clear()
                
                #Assign turn to player 1
                self.playerTurn = True
                
        #If either one of the players has reached a total score of 30 display game over        
        sense.show_message("Game Over!")
        
        #Record the winner's score, time and date to the winner.csv file
        #Check which player won
        if self.player1 >= 30:
            
            #Display message if player 1 wins
            sense.show_message("Player 1 Wins!!!")
            
            #Record the results
            self.recordResult("Player 1", self.player1, datetime.date(datetime.now()), datetime.time(datetime.now()))
        else:
            #Display message if player 2 wins
            sense.show_message("Player 2 Wins!!!")
            
            #Record the results
            self.recordResult("Player 2", self.player2, datetime.date(datetime.now()), datetime.time(datetime.now()))
