import folium as fol
map = fol.Map(location=[37.55043934921041, 126.99701154232895], zoom_start=12  , tiles="CartoDB positron")

fg = fol.FeatureGroup(name="My Map")

for coordinates in [[37.5, 126.9], [37.6, 126.8]]:
    fg.add_child(fol.Marker(location=coordinates, popup="This is SEOUL", icon=fol.Icon(color="blue")))

map.add_child(fg)
map.save("map1.html")
