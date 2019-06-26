from matplotlib import pyplot as plt
import pandas as pd

# import data
data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# Live Plot
plt.plot(ages, dev_salaries, color = '#444444', linestyle='--',
			 label='All Devs')

plt.plot(ages, py_salaries, color = '#888888', 
			label='Python')

# overall_median = 57287
# Fill color between Salaries
plt.fill_between(ages, py_salaries, dev_salaries,
			where=(py_salaries > dev_salaries),
			interpolate=True, alpha = 0.3, label='Above Avg')

plt.fill_between(ages, py_salaries, dev_salaries,
			where=(py_salaries <= dev_salaries),
			interpolate=True, alpha = 0.3, label='Below Avg')

plt.legend()

plt.title("Medien Salary($) by Ages")
plt.xlabel('Ages')
plt.ylabel('Medien Salary($)')

plt.savefig('LinePlot.png')
plt.tight_layout()
# plot
plt.show()