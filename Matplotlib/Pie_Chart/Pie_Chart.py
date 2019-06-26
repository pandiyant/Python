from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# Pie Chart
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['Javascript', 'HTML/CSS', 'SQL', 'Python', 'Java']

# Only "explode" the 2nd slice (i.e. "Pyhton")
explode = [0, 0, 0, 0.1, 0]

# plot
Fig, ax = plt.subplots()
ax.pie(slices, labels = labels, explode=explode, shadow=True, 
	autopct = "%1.1f%%", startangle = 90, 
	 wedgeprops={'edgecolor': 'white'})

plt.title("My Awesome Popular Progamming language(s) Pie Chart", fontsize = 14 )

plt.savefig('PieChart.png')

plt.tight_layout()
plt.show()


