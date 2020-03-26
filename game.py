from electronicDie import ElectronicDie
from sense_hat import SenseHat
import time
import csv
import os.path
from os import path
from datetime import datetime
sense = SenseHat()
electronicDieObj = ElectronicDie()

class Game:
    player1 = 0
    player2 = 0
    status = True
    
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def recordResult(self, player, score, date, time):
        if path.exists("winner.csv") == True:
             with open('winner.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([player, score, date, time])
        else:
            with open('winner.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerow([player, score, date, time])
        
    def getAccelerometer(self):
        a, b, c = sense.get_accelerometer_raw().values()
        
        a = abs(a)
        b = abs(b)
        c = abs(c)
        
        return a,b,c

    def wait_until(self):
        x = self.getAccelerometer()
        if x[0] > 1.4 or x[1] > 1.4 or x[2] > 1.4:
            return True
        else:
            return False
    
    def gameLogic(self):
        while self.player1 < 30 and self.player2 < 30:
            if self.status == True:
                #sense.show_message("Player 1's Turn!!!")
                while not self.wait_until():
                    time.sleep(0.01)
                self.player1 = self.player1 + electronicDieObj.roll_dice()
                print "Player 1's Current Score:",self.player1
                time.sleep(1)
                sense.clear()
                self.status = False
            elif self.status == False:
                #sense.show_message("Player 2's Turn!!!")
                while not self.wait_until():
                    time.sleep(0.01)
                self.player2 = self.player2 + electronicDieObj.roll_dice()
                print "Player 2's Current Score:",self.player2
                time.sleep(1)
                sense.clear()
                self.status = True
        sense.show_message("Game Over!")
        if self.player1 >= 30:
            sense.show_message("Player 1 Wins!!!")
            self.recordResult("Player 1", self.player1, datetime.date(datetime.now()), datetime.time(datetime.now()))
        else:
            sense.show_message("Player 2 Wins!!!")
            self.recordResult("Player 2", self.player2, datetime.date(datetime.now()), datetime.time(datetime.now()))
