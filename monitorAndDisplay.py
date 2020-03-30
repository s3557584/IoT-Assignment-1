from sense_hat import SenseHat
import time
import json

sense = SenseHat()


class monitorAndDisplay:
    
    def __init__(self, colour):
        self.colour = colour
        
        
    def getColour(self):
        with open('config.json') as config_file:
            data = json.load(config_file)
    
        cold_max = data['cold_max']
        comfortable_min = data['comfortable_min']
        comfortable_max = data['comfortable_max']
        hot_min = data['hot_min']
        
        #temp = sense.get_temperature()

        
        while True:
            temp = sense.get_temperature()
            
            if temp < cold_max:
                #sense.clear((0, 0, 255))
                sense.show_message(str(temp), text_colour = (0, 0, 255), back_colour = (0 ,0 ,0))
            elif comfortable_min < temp < comfortable_max:
                #sense.clear((0, 255, 0))
                sense.show_message(str(temp), text_colour = (0, 255, 0), back_colour = (0 ,0 ,0))
            elif temp > hot_min:
                sense.show_message(str(temp), text_colour = (255, 0, 0), back_colour = (0 ,0 ,0))
            time.sleep(10)
