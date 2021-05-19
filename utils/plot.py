import numpy as np
import pandas as pd

import matplotlib.pyplot as plt 

class Plot:
    def __init__(self, filePath):
        self.filepath = 'teste.csv'
    
    def plot(self):
        data = pd.read_csv(self.filepath)
        rows = []

        for row in data:
            rows.append(row)

        x = data[rows[0]].tolist()
        y = data[rows[1]].tolist()
            
        # plotting the points  
        plt.plot(x, y) 
        plt.xlabel('Timesteps') 
        plt.ylabel('Reward') 
        plt.title('Average reward per Timesteps') 
            
        # function to show the plot 
        plt.show() 