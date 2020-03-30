from sense_hat import SenseHat
import time
import json

sense = SenseHat()


class monitorAndDisplay:
    
    def __init__(self, colour):
        self.colour = colour
        
    #open config data to get the constants     
    def getColour(self):
        with open('config.json') as config_file:
            data = json.load(config_file)

        #data from json file
        cold_max = data['cold_max']
        comfortable_min = data['comfortable_min']
        comfortable_max = data['comfortable_max']
        hot_min = data['hot_min']
        

        #while loop to show the temperature in the required colour every 10s
        while True:
            temp = sense.get_temperature()
            
            if temp < cold_max:
                sense.show_message(str(temp), text_colour = (0, 0, 255), back_colour = (0 ,0 ,0))
            elif comfortable_min < temp < comfortable_max:
                sense.show_message(str(temp), text_colour = (0, 255, 0), back_colour = (0 ,0 ,0))
            elif temp > hot_min:
                sense.show_message(str(temp), text_colour = (255, 0, 0), back_colour = (0 ,0 ,0))
            time.sleep(10)
