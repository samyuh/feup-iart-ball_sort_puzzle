import os

from datetime import datetime
import matplotlib.pyplot as plt

class Logger:
    def __init__(self, algorithm):
        self._dir = "logs/"
        
        try:
            os.mkdir(self._dir)
        except FileExistsError:
            pass
        
        time = datetime.now().strftime("%H_%M_%S")
        self.log = open('all.csv', "w")
        self.avg = open('teste.csv', "w")
     
    def writeLog(self, episode, rewards):
        self.log.write(str(episode) + "," + str(rewards) + "\n")

    def writeAvgRewards(self, count, r):
        self.avg.write(str(count) + "," + str(sum(r / 100)) + "\n")



