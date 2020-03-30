# IoT-Assignment-1 (s3557584,)
Repository of Assignment 1 for the course Internet Of Things<br/><br/>
This assignment has been produced in a group of two and the code used to produce this assignment is Python<br/><br/>
This assignment majorly focuses on producing small IoT apllications using the Raspberry Pi and the Sense Hat<br/><br/>
The assignment consists of 3 parts and it has been split into Task A, Task B and Task C
# Task A
For Task A, three emojis will be display in three diffrent colors through the LED on the Sense Hat. The three emojis are smiley emoji, sad emoji and surprised emoji. Each of the emoji will be displayed in three diffrent colors which are yellow, white and blue.<br/><br/>
This task has 2 files: animatedEmoji.py, TaskAMain.py
# Task B
For Task B, we have to read the surrounding temperature through the Sense Hat and display them through the LED on the Sense Hat. The temperature will be display in 3 diffrent colors which are Blue if the teperature is below 10, Green if the temperature is between 10 and 25 and lastly Red if its above 25.
The configurations mentioned for this task must be taken from a json file.<br/><br/>
This task has 3 files: configureAndDisplay.py, TaskBMain.py, config.json
# Task C
For Task C, we have to create a 2 player die-based mini game using the Raspberry Pi and Sense Hat. The rules of this game are each player will roll the die each turn by shaking the Raspberry Pi and who ever reaches a total score of 30 or above wins. Throughout the game instructions will be shown through the LED of the Sense Hat and the winner's score, date and time will be recorded in a csv file call "winner.csv".<br/><br/>
This task has 3 files (excluding the winner.csv): electronicDie.py, game.py, TaskCMain.py
