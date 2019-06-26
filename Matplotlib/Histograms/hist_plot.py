from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, edgecolor='black', log = True)

median_age = 29
color = 'orange'

plt.axvline(median_age, color=color, label='Age Median', linewidth = 2)

plt.legend()

plt.title('Ages of Respodents')
plt.xlabel('Ages')
plt.ylabel('Total Respodents')

plt.tight_layout()
# Save figure
plt.savefig('Histograms')
# plot
plt.show()