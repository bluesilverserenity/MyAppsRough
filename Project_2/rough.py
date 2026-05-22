import folium as fol
map = fol.Map(location=[37.55043934921041, 126.99701154232895], zoom_start=12, TileLayer="Mapbox Bright")

fg = fol.FeatureGroup(name="My Map")

fg.add_child(fol.Marker(location=[37.55043934921041, 126.99701154232895], popup="This is SEOUL", icon=fol.Icon(color="blue")))

map.add_child(fg)
map.save("map.html")
