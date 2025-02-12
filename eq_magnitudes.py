import json
from pathlib import Path
import plotly.express as px



path = Path('files/eq_data_1_day_m1.geojson')
content = path.read_text(encoding="utf-8", errors="replace")
all_data = json.loads(content)

mags, lats, lons, titles = [], [], [], []
for data in all_data['features']:
    mags.append(data.get('properties','').get('mag',''))
    titles.append(data.get('properties','').get('title',''))
    lons.append(data.get('geometry','').get('coordinates','')[0])
    lats.append(data.get('geometry','').get('coordinates','')[1])

fig = px.scatter_geo(lat=lats, 
                     lon=lons, 
                     size=mags, 
                     title="Magnitude of Earthquakes around the World last 24 Hours",
                     hover_name=titles,
                     projection='natural earth',
                     labels={'color': 'Magnitude'},
                     color=mags,
                     color_continuous_scale='Viridis'
                    )
fig.show()