import folium
import requests
import os
import json

# Function to get the latitude and longitude of a postcode
def get_lat_long_from_postcode(postcode):
    # Send a request to the postcodes.io API to retrieve the latitude and longitude of the postcode
    postcodes_url = f"https://api.postcodes.io/postcodes/{postcode}"
    response = requests.get(postcodes_url)

    print(response.status_code)
    # Check the status code to ensure the request was successful
    if response.status_code == 200:
        # Retrieve the latitude and longitude from the response
        data = response.json()
        latitude = data["result"]["latitude"]
        longitude = data["result"]["longitude"]

        # Return the latitude and longitude as a tuple
        return (latitude, longitude)
    else:
        # If the request was not successful, return None
        return None

# Get the postcode from the user
postcode = input('Enter a postcode: ')

# Get the latitude and longitude of the postcode
lat_long = get_lat_long_from_postcode(postcode)

# Check if the function returned a valid latitude and longitude
if lat_long is not None:
    # takes a postcode and returns a map of that are and saves it to a file
    
    # If the function returned a valid latitude and longitude, create a folium map object centered on that location
    map = folium.Map(location=lat_long, zoom_start=12)
    print('Map created')

    # Prompt the user to enter "yes" or "no" to indicate if they want to generate crime data
generate_crime_data = input("Generate crime data? (yes/no): ")

# Check if the user entered "yes"
if generate_crime_data.lower() == "yes":
    # Get the crime data from some source (e.g. an API or a JSON file)
    postcode_without_spaces = postcode.replace(" ", "")
    # For now, we'll just use a list of crimes from json file matching the postcode
    filename = f"crimes/{postcode_without_spaces}_crimes.json"
    with open(filename, "r") as f:
        crime_data = json.load(f)

    # Iterate over the crime data
    for crime in crime_data:
        # Get the latitude and longitude of the crime
        latitude = crime["location"]["latitude"]
        print(latitude)
        longitude = crime["location"]["longitude"]
        print(longitude)
        
        # Get the category of the crime
        details = crime["category"]
        
        # Create a marker on the map for the crime
        folium.Marker(location=(latitude, longitude), popup=details).add_to(map)

    
    # Display the map
    map

    # Create the "map" folder if it doesn't exist
    if not os.path.exists('map'):
        os.makedirs('map')

    # Set the filename and file type for the map
    postcode_without_spaces = postcode.replace(" ", "")
    filename = f"{postcode_without_spaces}_map.html"

    # Save the map to an HTML file with the specified filename
    map.save(f'map/{filename}')

    # Open the HTML file in the default web browser
    import webbrowser
    webbrowser.open(f'map/{filename}')

    
else:
    # If the function returned None, print an error message
    print('Invalid postcode')
