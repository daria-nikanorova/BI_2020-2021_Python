import pandas as pd
import matplotlib.pyplot as plt

#read data
df = pd.read_csv("data/menu.csv", parse_dates = True)

#select only meat meals
df = df[df.Category == 'Beef & Pork']

#set parameters for all future graphs
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['figure.figsize'] = [15, 8]
plt.rcParams['font.size'] = 15

#draw a plot
plt.plot(df['Item'], df['Total Fat'], color = '#ff7f00', label = 'Fat')
plt.plot(df['Item'], df['Carbohydrates'], color = '#33a02c', label = 'Carbohydrates')
plt.plot(df['Item'], df['Protein'], color = '#1f78b4', label = 'Protein')

#rotate labels on x axis
plt.xticks(rotation = 45, ha = 'right')

#add title
plt.title('Nutrition in McDonalds meals')

#add axes labels
plt.xlabel('Meals')
plt.ylabel('Nutrition')

#add legend
plt.legend()

#add grid
plt.grid()

#show plot
#plt.show()

#save plot
plt.savefig('McDonalds_nutrition.png')
