import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
import matplotlib

# style sheet
plt.style.use("fivethirtyeight")

#import and read csv file

data = pd.read_csv("data.csv")

ids = data['Responder_id']

lang_responses = data['LanguagesWorkedWith']
#  Initialize Counter
language_counter = Counter()

for response in lang_responses:
	language_counter.update(response.split(';'))


languages = []
popularity = []

# Most Popular Programming Languages (15)
for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])

languages.reverse()
popularity.reverse()

width = 0.75
Number = [0, 10000, 20000, 30000, 40000, 50000, 60000]

ind = np.arange(len(popularity))

fig, ax = plt.subplots()
# plot
ax.barh(languages, popularity, width, color='#E6842A')
for i, v in enumerate(popularity):
    ax.text(v - 3 , i - 0.25, str(v), color='blue', fontsize=10, alpha=0.8, fontweight='bold')

ax.set_yticks(ind + width/3.5)
ax.set_yticklabels(languages, minor=False, fontsize=10)
plt.xticks(Number, fontsize=10)
plt.title("Most Popular Languages", fontsize=14)
plt.xlabel("Number of People who use", fontsize=14)

plt.tight_layout()
# Save as Image file
plt.savefig('Graph.png')

plt.show()