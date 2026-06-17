import folium as fol
import pandas as pd

df = pd.read_csv("Volcanoes_USA.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])

def color_marker(elev):
    if elev < 1000:
        return "green"
    elif 1000 <= elev < 3000:
        return "orange"
    else:
        return "red"
    
map = fol.Map(location=[48.776798, -121.810997], zoom_start=6, tiles="OpenStreetMap")

fg = fol.FeatureGroup(name="Volcanoes Map")
for i, j, k in zip(lat, lon, elev):
    fg.add_child(fol.Marker(location=[i, j], popup=str(k)+" m", icon=fol.Icon(color=color_marker(k))))

fg.add_child(fol.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), style_function=lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000 else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))

map.add_child(fg)
map.save("volmap.html")
