import folium as fol
import pandas as pd

df = pd.read_csv("Volcanoes_USA.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])

map = fol.Map(location=[48.776798, -121.810997], zoom_start=6, tiles="OpenStreetMap")

fg = fol.FeatureGroup(name="Volcanoes Map")
for i, j, k in zip(lat, lon, elev):
    fg.add_child(fol.Marker(location=[i, j], popup=k, icon=fol.Icon(color="red")))

map.add_child(fg)
map.save("volmap.html")
