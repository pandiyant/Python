from matplotlib import pyplot as plt
from datetime import timedelta, datetime
from matplotlib import dates as mpl_dates
import pandas as pd

plt.style.use('fivethirtyeight')

# Import data
data = pd.read_csv('data.csv')

# Convert data string to datetime
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace = True)

# Set axis
price_data = data['Date']
price_close = data['Close']

plt.plot_date(price_data, price_close, linestyle = 'solid')
# get current figure
plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()
plt.savefig('TimeSeriesPlot.png')

plt.show()