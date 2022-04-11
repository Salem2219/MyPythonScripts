# Importing the geodesic module from the library
from geopy.distance import geodesic

# Loading the lat-long data for Kolkata & Delhi
kolkata = (22.5726, 88.3639)
delhi = (28.7041, 77.1025)

# Print the distance calculated in km
print(geodesic(kolkata, delhi).km)
