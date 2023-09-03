from geopy.geocoders import Nominatim

# Initialize the Nominatim geocoder
geolocator = Nominatim(user_agent="city_coordinates_app")

# Input city name
city_name = "new delhi"

try:
    # Perform geocoding
    location = geolocator.geocode(city_name)
    
    if location:
        latitude = location.latitude
        longitude = location.longitude
        print(f"Coordinates for {city_name}: Latitude={latitude}, Longitude={longitude}")
    else:
        print(f"Coordinates for {city_name} not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
