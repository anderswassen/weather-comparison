import requests
import matplotlib.pyplot as plt
import pandas as pd
import time

# Initialize a dictionary for caching coordinates to minimize repeated API calls
coordinates_cache = {}

def get_coordinates(location_name):
    """Fetch latitude and longitude for a location using Nominatim API, with caching."""
    # Check if coordinates are already in cache
    if location_name in coordinates_cache:
        return coordinates_cache[location_name]

    url = "https://nominatim.openstreetmap.org/search"
    params = {'q': location_name, 'format': 'json', 'limit': 1}
    headers = {'User-Agent': 'WeatherComparisonApp/1.0'}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        if data:
            lat = round(float(data[0]['lat']), 4)
            lon = round(float(data[0]['lon']), 4)
            coordinates_cache[location_name] = (lat, lon)  # Cache the result
            return lat, lon
        else:
            print(f"No results found for {location_name}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {location_name}: {e}")
        return None

def get_weather_data(latitude, longitude):
    """Fetch weather data from SMHI API for specific latitude and longitude."""
    url = f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{longitude}/lat/{latitude}/data.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data for coordinates ({latitude}, {longitude}): {e}")
        return None

def parse_forecast_data(weather_data):
    """Parse weather data to extract dates, temperature, wind, humidity, and precipitation."""
    forecasts = weather_data.get("timeSeries", [])
    parsed_data = {"Date": [], "Temperature": [], "Wind": [], "Humidity": [], "Precipitation": []}

    for forecast in forecasts:
        date = pd.to_datetime(forecast["validTime"])  # Convert date here
        params = {param["name"]: param["values"][0] for param in forecast["parameters"]}

        # Append each parameter to the corresponding list, defaulting to None if missing
        parsed_data["Date"].append(date)
        parsed_data["Temperature"].append(params.get("t"))
        parsed_data["Wind"].append(params.get("ws"))
        parsed_data["Humidity"].append(params.get("r"))
        parsed_data["Precipitation"].append(params.get("pmax"))

    return parsed_data

def plot_weather_data(ax, data1_df, data2_df, y_label, title, parameter, location1, location2):
    """Plot weather data comparison for a specific parameter."""
    ax.plot(data1_df['Date'], data1_df[parameter], label=location1, marker="o")
    ax.plot(data2_df['Date'], data2_df[parameter], label=location2, marker="o")
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel(y_label)
    ax.legend()
    ax.tick_params(rotation=45)

def main():
    # Get user input for two locations
    location1 = input("Enter the first location: ")
    location2 = input("Enter the second location: ")

    # Fetch coordinates with a delay for API rate limiting
    coords1 = get_coordinates(location1)
    time.sleep(1)
    coords2 = get_coordinates(location2)

    if not coords1 or not coords2:
        print("Error fetching data for one or both locations.")
        return

    # Fetch weather data for both locations
    data1 = get_weather_data(*coords1)
    data2 = get_weather_data(*coords2)

    if not data1 or not data2:
        print("Error fetching weather data for one or both locations.")
        return

    # Parse the data and convert to DataFrames
    data1_df = pd.DataFrame(parse_forecast_data(data1))
    data2_df = pd.DataFrame(parse_forecast_data(data2))

    # Set up subplots for each weather parameter
    fig, axs = plt.subplots(2, 2, figsize=(14, 10), num="Weather Comparison for Locations")
    plot_weather_data(axs[0, 0], data1_df, data2_df, 'Temperature (°C)', 'Temperature', 'Temperature', location1, location2)
    plot_weather_data(axs[0, 1], data1_df, data2_df, 'Wind Speed (m/s)', 'Wind Speed', 'Wind', location1, location2)
    plot_weather_data(axs[1, 0], data1_df, data2_df, 'Humidity (%)', 'Humidity', 'Humidity', location1, location2)
    plot_weather_data(axs[1, 1], data1_df, data2_df, 'Precipitation (mm)', 'Precipitation', 'Precipitation', location1, location2)

    # Set main title and display attribution
    fig.suptitle(f"Weather Comparison for {location1} and {location2}")
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.figtext(0.5, 0.01, "Location data provided by OpenStreetMap via Nominatim", ha="center", fontsize=8)
    plt.show()

if __name__ == "__main__":
    main()
