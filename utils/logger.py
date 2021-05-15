from datetime import datetime

class Logger:
    def __init__(self, algorithm):
        self._dir = "logs/"

        time = datetime.now().strftime("%H_%M_%S")
        self.log = open(self._dir + algorithm + '-' + time + '-log.csv', "x")
        self.avg = open(self._dir + algorithm + '-' + time + '-log_average_rewards.csv', "x")
        self.info = open(self._dir + algorithm + '-' + time + '-info.txt', "x")

    def writeInfo(self):
        pass
        
    def writeLog(self, episode, rewards):
        self.log.write(str(episode) + "," + str(rewards) + "\n")

    def writeAvgRewards(self, count, r):
        self.avg.write(str(count) + "," + str(sum(r / 100)) + "\n")
