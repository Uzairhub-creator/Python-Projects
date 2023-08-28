import phonenumbers, opencage, folium
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
key = "Your API key from opencage.com Available for  1  time use only"

geocoderr =  OpenCageGeocode(key)
number = "Numberyouwant to trace with country code"

pepnum = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnum, "en")
carr= carrier.name_for_number(pepnum, "en")
print(location)
print(carr)

query = str(location)
results = geocoderr.geocode(query)
# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("myLocation.html")
