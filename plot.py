import matplotlib.pyplot as plt 
    
import numpy as np
import pandas as pd

filepath = 'teste.csv'
data = pd.read_csv(filepath)
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






