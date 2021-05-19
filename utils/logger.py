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
    
    @staticmethod
    def printAvgRewards(count, r):
        print(count, ": ", str(sum(r / 100)))

    @staticmethod
    def newEpisode(episode):
        print("*** EPISODE {} ***".format(episode))

    @staticmethod
    def finishStep(step):
        print("Found Solution - Step: {}".format(step))

    @staticmethod
    def finish(rewards_all_episodes, num_episodes, exploration_rate):
        print("Performace: " +  str(sum(rewards_all_episodes)/num_episodes))
        print("Exploration Rate: ", exploration_rate)

    @staticmethod
    def errorArgs():
        print("Bad arguments\nUsage:")
        print(" main.py [ALGORITHM] [CONFIG] {<-log> <-render> <-default>}\n\n")
        print("Configuration Files:")
        print("     - More information on README. You can also use one of your config file, by passing \"default.json\" without quotes\n")
        print("Algorithms:")
        print("     - qlearning")
        print("     - sarsa\n")
        print("OPTIONS:")
        print("     -log")
        print("     -render")
        print("     -render")

    @staticmethod
    def fileNotFound(file):
        print("-> {} file not found. More information on README".format(file))




