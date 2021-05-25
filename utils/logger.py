
# -- Imports -- #

import os
from datetime import datetime


class Logger:
    """
    Class for representing the logs of the algorithms
    """
    def __init__(self, algorithm):
        self._dir = "logs/"
        
        try:
            os.mkdir(self._dir)
        except FileExistsError:
            pass
        
        time = datetime.now().strftime("%H_%M_%S")
        self._logAllFile = self._dir + algorithm + '-' +time + '-all.csv'
        self._logAvgFile = self._dir + algorithm + '-' +time + '-avg.csv'
        self.log = open(self._logAllFile, "w")
        self.avg = open(self._logAvgFile, "w")
    
    def closeLogs(self):
        self.log.close()
        self.avg.close()

        return self._logAllFile, self._logAvgFile

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
        print("Done - Step: {}".format(step))

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
    def error(message):
        print("[ERROR] {}".format(message))


