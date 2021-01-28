import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# set parameters for all future graphs
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['figure.figsize'] = [15, 8]
plt.rcParams['font.size'] = 15

# read data
df=pd.read_csv("data/menu.csv", parse_dates=True)

# Data to plot
mean_protein = round(np.mean(df['Protein']), 2)
mean_fat = round(np.mean(df['Total Fat']), 2)
mean_carb = round(np.mean(df['Carbohydrates']), 2)

mean_values = [mean_protein, mean_carb, mean_fat]

labels = 'Protein', 'Carbohydrates', 'Fat'
colors = ['#decbe4', '#ccebc5', '#ffffb3']
explode = (0.1, 0, 0)

# Plot
plt.pie(mean_values, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')

#add title
plt.title('Nutrition in McDonalds meals')

#save plot
plt.savefig('Nutrition_McDonalds_meals.png')
