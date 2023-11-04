import pygrib
import matplotlib.pyplot as plt
import numpy as np

# Path to the GRIB file
grib_file = 'mars_data_0.grib'

# Open the GRIB file
grbs = pygrib.open(grib_file)

# Choose the specific GRIB message (field) you want to display
# You may need to inspect the GRIB file to determine the message number
message_number = 1  # Change this to the appropriate message number

# Read the chosen GRIB message
grb = grbs.message(message_number)

# Extract the data and metadata from the GRIB message
data, lats, lons = grb.data()

# Create a contour plot of the data using matplotlib
plt.contourf(lons, lats, data)
plt.colorbar()
plt.title(grb['name'])
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Close the GRIB file
grbs.close()