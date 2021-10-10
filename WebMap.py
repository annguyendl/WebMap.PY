from branca.element import IFrame
import folium
import pandas

data = pandas.read_csv("QuanNgonSaigon.csv", delimiter="|")
lon = list(data["Longtitude"])
lat = list(data["Latitude"])
nam = list(data["Name"])
addr = list(data["Address"])
ggmap = list(data["GoogleMap"])
loctype = list(data["LocType"])

popuptmpl = """<h4>%s</h4>
Địa chỉ: %s<br/>
Link: <a href=https://goo.gl/maps/%s target=_blank>Google Map</a>
"""

map = folium.Map(location=[10.81159794894754, 106.78583346205473], zoom_start=12)

fg = folium.FeatureGroup(name="Quán ngon")
for ln, lt, nm, ad, gg, ltype in zip(lon, lat, nam, addr, ggmap, loctype):
    if ltype=='QA':
        iframe = folium.IFrame(html=popuptmpl % (nm, ad, gg),width=200, height=100)
        fg.add_child(folium.Marker(location=[float(ln), float(lt)], popup=folium.Popup(iframe), icon=folium.Icon(color='green')))

map.add_child(fg)

#fgp = folium.FeatureGroup(name="Dân số 2005")
#fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),
#style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
#else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
#map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("QuanNgonSaigon.html")