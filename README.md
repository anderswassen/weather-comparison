
# 🌦️ Location-Based Weather Comparison Tool 🌦️

This Python application provides a side-by-side comparison of weather data for two user-specified locations. Using the SMHI and OpenStreetMap Nominatim APIs, the tool fetches and visualizes daily metrics such as temperature, wind speed, humidity, and precipitation, making it ideal for those interested in analyzing environmental conditions across different regions.

## Features

- **Location Search with Caching**: Efficiently fetches and caches geographic coordinates via the Nominatim API, minimizing repeated requests.
- **Comprehensive Weather Data**: Retrieves daily weather data, parsed and visualized with Matplotlib, for intuitive trend analysis.
- **Flexible Data Visualization**: Compares key weather metrics side-by-side in a clear, multi-plot layout.
- **Error Handling and Rate Limiting**: Smooth operation with API rate-limiting, caching, and detailed error messages.
- **Docker-Ready**: Includes Docker support for easy setup and deployment.

## Prerequisites

- **Python 3.8+**
- **API Keys**:
  - SMHI for weather data (no API key required)
  - Nominatim (no API key required, but it’s essential to provide a unique `User-Agent`)

Install required packages:

```bash
pip install -r requirements.txt
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anderswassen/weather-comparison.git
   cd weather-comparison
   ```

2. **Set up Docker (optional)**:
   Build the Docker image:
   ```bash
   docker build -t weather-comparison .
   ```

3. **Run the tool**:
   ```bash
   python main.py
   ```

## Usage

1. Run the application, which will prompt you to enter two locations.
2. The application fetches latitude and longitude for each location, retrieves weather data, and visualizes it across four key metrics: Temperature, Wind Speed, Humidity, and Precipitation.
3. The output is displayed as a multi-plot figure in a window titled "Weather Comparison for Locations."

## Example

After running the program and entering two locations (e.g., "Stockholm" and "Gothenburg"), the tool will display:

- Temperature trends
- Wind speed variations
- Humidity percentages
- Precipitation levels

Each metric is plotted separately, with dates on the x-axis for easy comparison.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **SMHI API**: For providing detailed weather data.
- **OpenStreetMap Nominatim API**: For geographic data.

**Note**: Remember to use the application responsibly and adhere to the API rate limits to avoid service interruptions.
