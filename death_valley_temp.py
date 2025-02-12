import csv
from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt # type: ignore
import matplotlib.dates as mdates 



path = Path('files/death_valley_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader) #reads value from iterator (reader)

dates, highs, lows = [], [], []

for row in reader:
    try:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[6])
        low = int(row[7])
    except ValueError:
        print("There were missing data in the column.")
    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(dates, highs, color="red")
ax.plot(dates, lows, color="blue")


ax.set_title("High and Low Temperatures in Death Valley, CA for 2021")
ax.set_ylabel("Temperature (F)", fontsize=8)
ax.set_xlabel("", fontsize=8)
ax.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

fig.autofmt_xdate()
ax.tick_params(labelsize=8)
plt.show()
