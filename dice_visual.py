from dice import Dice
import plotly.express as px # type: ignore


die_1 = Dice()
die_2 = Dice(10)

results = []
for num in range(50000):
    rand_side= die_1.roll() + die_2.roll()
    results.append(rand_side)

frequency = []
max_result = die_1.num_of_side + die_2.num_of_side
sides = range(2, max_result+1)
for side in sides:
    count = results.count(side)
    frequency.append(count)

title = "Results of Rolling a D6 and D10 after 50,000 Times"
labels = {"x": "Side", "y": "Frequency"}
fig = px.bar(x=sides, y=frequency, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)

# fig.show()
fig.write_html("dice_results.html")