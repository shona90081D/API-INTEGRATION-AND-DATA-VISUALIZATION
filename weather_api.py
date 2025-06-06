import requests  # For making HTTP requests to the API
import matplotlib.pyplot as plt  # For plotting the graphs
import seaborn as sns  # For creating attractive and informative plots

# Your valid API key from OpenWeatherMap (replace with actual key)
API_KEY = 'd3ba11319f2cf77a746db77036f4e085'

# OpenWeatherMap API endpoint to fetch weather data
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# List of cities to get weather data for
CITIES = ['New York', 'London', 'Tokyo', 'Sydney', 'Mumbai', 'Cairo', 'Rio de Janeiro']

# Function to fetch weather data from OpenWeatherMap API for a given city
def get_weather_data(city):
    # Parameters to send in the API request (city name, API key, and unit for temperature)
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Fetch data in Celsius
    }
    
    # Send GET request to OpenWeatherMap API
    response = requests.get(BASE_URL, params=params)
    
    # Parse the response JSON
    data = response.json()
    
    # If the response is successful, extract relevant data
    if response.status_code == 200 and 'main' in data:
        return {
            'city': city,
            'temperature': data['main']['temp'],  # Temperature in Celsius
            'humidity': data['main']['humidity']   # Humidity in percentage
        }
    else:
        # Raise an exception if the API request failed
        raise Exception(data.get("message", "API Error"))

# Fetch weather data for all the cities
weather_data = []
for city in CITIES:
    try:
        # Fetch data for each city
        weather = get_weather_data(city)
        weather_data.append(weather)
    except Exception as e:
        # Print error message if data for a city cannot be fetched
        print(f"Could not fetch data for {city}: {e}")

# Exit if no data was fetched (due to API key issues or network problems)
if not weather_data:
    print("No data available. Check your API key or network.")
    exit()

# Extract the cities, temperatures, and humidity values for plotting
cities = [entry['city'] for entry in weather_data]
temperatures = [entry['temperature'] for entry in weather_data]
humidity = [entry['humidity'] for entry in weather_data]

# Set the style for the plots (Seaborn style)
sns.set(style="white", context='talk')

# Create a figure and adjust layout for the subplots
plt.figure(figsize=(16, 7))
plt.subplots_adjust(top=0.85)

# Simple text labels for temperature, humidity, and global weather
globe_label = "Global Weather Dashboard"
temp_label = "Temperature (°C)"
humidity_label = "Humidity (%)"

# Update Matplotlib's font to 'DejaVu Sans', which has better emoji support
plt.rcParams['font.family'] = 'DejaVu Sans'

# Set the main title for the plot with the globe label
plt.suptitle(f'{globe_label}', fontsize=24, fontweight='bold', color='#333')

# Temperature subplot: Create a bar plot for temperatures in the cities
plt.subplot(1, 2, 1)
# Create a barplot with custom color palette and hue based on cities
sns.barplot(x=cities, y=temperatures, hue=cities, palette='rocket', legend=False)
plt.title(f'{temp_label}', fontsize=18, fontweight='bold')  # Title for the temperature plot
plt.ylabel('Temperature (°C)', fontsize=14)  # Y-axis label for temperature
plt.xlabel('')  # No label for X-axis since cities will be labeled below
plt.xticks(rotation=30, ha='right', fontsize=12)  # Rotate X-axis labels for readability

# Annotate the bars with temperature values
for i, temp in enumerate(temperatures):
    plt.text(i, temp + 0.5, f"{temp:.1f}°", ha='center', fontsize=12, color='black')

# Humidity subplot: Create a bar plot for humidity in the cities
plt.subplot(1, 2, 2)
# Create a barplot with custom color palette and hue based on cities
sns.barplot(x=cities, y=humidity, hue=cities, palette='cool', legend=False)
plt.title(f'{humidity_label}', fontsize=18, fontweight='bold')  # Title for the humidity plot
plt.ylabel('Humidity (%)', fontsize=14)  # Y-axis label for humidity
plt.xlabel('')  # No label for X-axis since cities will be labeled below
plt.xticks(rotation=30, ha='right', fontsize=12)  # Rotate X-axis labels for readability

# Annotate the bars with humidity values
for i, hum in enumerate(humidity):
    plt.text(i, hum + 1.5, f"{hum}%", ha='center', fontsize=12, color='black')

# Adjust layout and make sure there’s no overlap
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plot
plt.show()
