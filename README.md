# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: DESHNA

*INTERN ID*: CT04DM184

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH
## TASK DESCRIPTION

Weather API Integration and Data Visualization This project focuses on integrating a public API to fetch real-time weather data and visualizing it using Python libraries such as Matplotlib and Seaborn. The goal is to create a clear and visually appealing weather dashboard that displays temperature and humidity information for multiple global cities.

API Integration Weather data is sourced from the OpenWeatherMap API, which offers real-time weather statistics for any global location. The user registers on the platform to obtain an API key, which is used to authenticate and fetch data. HTTP GET requests are made for selected cities with the unit system set to metric (°C).
The response is in JSON format and contains comprehensive weather details. The script extracts: Temperature (°C) Humidity (%)

A diverse set of cities is chosen to represent different geographical and climatic zones, including New York, London, Tokyo, Sydney, Mumbai, Cairo, and Rio de Janeiro.

Data Handling The script iterates through each city, calls the API, and stores the temperature and humidity in a structured list of dictionaries. It includes error handling to manage API failures, invalid city names, or connectivity issues, ensuring the program remains robust and informative in case of partial failures.
Extracted data is then parsed into lists: cities, temperatures, and humidity, which serve as the input for visualization.

Data Visualization Using Seaborn and Matplotlib, the data is displayed in a dashboard with two main bar charts:
Temperature Bar Chart (with a red-yellow color scheme)

Humidity Bar Chart (with a blue-green color scheme)

Each bar is labeled with its respective value for improved readability. The visual layout uses Seaborn themes for a clean appearance and Matplotlib’s layout controls to organize the charts clearly. The dashboard includes:

A descriptive title: "Global Weather Dashboard"

Rotated city names for readability

Annotations above each bar

Stylish and accessible fonts for better compatibility

Applications This project has several real-world applications:
Educational Use: A great mini-project to teach students about REST APIs, JSON parsing, and data visualization in Python.

Weather Monitoring Tools: Can be scaled to monitor real-time weather across various cities for logistics, travel agencies, or agriculture.

Dashboards for IoT Devices: Useful for smart home or smart city systems that track environmental conditions.

Business Analytics: Companies with global operations can integrate this to understand local weather trends affecting transportation or productivity.

Data Journalism: Journalists and bloggers can use similar scripts to present weather trends interactively and visually.

This task successfully demonstrates how to integrate external APIs with Python and present meaningful data through interactive visualizations. It blends software development, data analysis, and visual design into one cohesive and practical application. The project is beginner-friendly yet scalable, offering a solid foundation for more advanced dashboards or automation-based weather systems.

OUTPUT:

![Image](https://github.com/user-attachments/assets/81faa581-8083-4ceb-84b1-6d63448cdd61)
