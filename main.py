from tkinter import *
# from geopy.geocoders import Nominatim

LIGHT_GREEN = "#C8E4B2"
GREEN = "#9ED2BE"
DARK_GREEN = "#FFB000"
CREAM = "#FFCF9D"
FONT_COLOR = "#373331"
FONT = "Space Mono"

# Geocodes by the way refer to coordinates
# geolocator = Nominatim(user_agent='Tochukwu')
# location = geolocator.geocode("175 5th Avenue NYC")
# print(type(location))
# print(location.address)
# print((location.latitude, location.longitude))
# print(location.raw)

# coord_location = geolocator.reverse("5.3927, 6.9861")
# print(coord_location.address)
# print(coord_location.raw)
# print(list(coord_location))

window = Tk()
window.config(bg=LIGHT_GREEN, padx=100)
window.title("Phone Locator")
window.minsize(width=500, height=300)

locator_Label = Label(text="Pinpoint-Locator", fg=FONT_COLOR, font=(FONT, 20, "bold"), bg=LIGHT_GREEN, pady=50)
locator_Label.grid(column=2, row=0)

Longitude_Label = Label(text="Longitude", fg=FONT_COLOR, font=(FONT, 10, "bold"), bg=LIGHT_GREEN)
Longitude_Label.grid(column=0, row=3)
Longitude_entry = Entry(width=25)
Longitude_entry.grid(column=1, row=3)

dummy_widget = Label(text="", pady=5, bg=LIGHT_GREEN)
dummy_widget.grid(column=2, row=3)

Latitude_Label = Label(text="Latitude", fg=FONT_COLOR, font=(FONT, 10, "bold"), bg=LIGHT_GREEN, pady=20)
Latitude_Label.grid(column=3, row=3)
Latitude_entry = Entry(width=25)
Latitude_entry.grid(column=4, row=3)

google_maps_button = Button(text="📍", fg="green", width=8, height=2, font=("", 20))
google_maps_button.grid(column=2, row=5)

window.mainloop()
