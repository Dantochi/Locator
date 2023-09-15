from tkinter import *
from geopy.geocoders import Nominatim

# Geocodes by the way refer to coordinates
geolocator = Nominatim(user_agent='Tochukwu')
location = geolocator.geocode("175 5th Avenue NYC")
# print(type(location))
# print(location.address)
# print((location.latitude, location.longitude))
# print(location.raw)

coord_location = geolocator.reverse("5.3927, 6.9861")
print(coord_location.address)
print(coord_location.raw)
print(list(coord_location))

window = Tk()


window.mainloop()
