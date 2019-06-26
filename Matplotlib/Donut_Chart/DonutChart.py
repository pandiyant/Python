from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# Pie Chart
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['Javascript', 'HTML/CSS', 'SQL', 'Python', 'Java']

# Only "explode" the 2nd slice (i.e. "Pyhton")
explode = [0.05, 0.05, 0.05, 0.05, 0.05]

# plot
Fig, ax = plt.subplots()
ax.pie(slices, labels = labels, explode=explode, shadow=True, 
	autopct = "%1.1f%%", startangle = 90)

# draw Circle
centre_circle =plt.Circle((0,0),0.7, fc = 'white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("My Awesome Popular Progamming language(s) Donut Chart", fontsize = 14 )

plt.savefig('DonutChart.png')

plt.tight_layout()
plt.show()


