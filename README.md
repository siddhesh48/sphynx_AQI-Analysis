           AIR QUALITY ANALYSIS
GROUP MEMBERS –
•	Siddhesh Tripathi  - ku2407u378
•	Rehan Khan           - ku2407u363
•	Niraj Matai            - ku2407u341
•	Niyati Joshi            -ku2407u342
•	Nidhi Kotian          -ku2407u339

OBJECTIVE-
The objective of the project to visualize the AQI graph for PM2.5 and PM10 is to:
1.	Analyze Air Quality Data: Use collected data for PM2.5 and PM10 concentration levels to assess air quality over time.
2.	Visualize AQI Trends: Create clear, interpretable visualizations (e.g., line charts, bar graphs, or heatmaps) to show the variations in PM2.5 and PM10 concentrations over different time periods (daily, weekly, or monthly).
3.	Compare PM2.5 and PM10 Levels: Display side-by-side comparisons of PM2.5 and PM10 concentrations to understand the differences in their impact on air quality.
4.	Highlight AQI Categories: Color-code or annotate the graph based on AQI levels (e.g., good, moderate, unhealthy) to make it easier to understand the air quality status.
5.	Provide Interactive Visualizations: If applicable, create an interactive dashboard for users to explore different locations, time ranges, and pollutant levels.
This project focuses purely on presenting the AQI data for PM2.5 and PM10 visually, allowing for better interpretation and analysis of air quality without predictive modeling.

LIBRARIES USED- 
1. pandas:
•	Purpose: Data manipulation.
•	Functions: Reads CSV files, handles missing values, aggregates data (e.g., by city and month).
2. matplotlib.pyplot:
•	Purpose: Plotting graphs.
•	Functions: Creates line plots, sets titles, labels, and grid for visualization.
3. seaborn:
•	Purpose: Advanced statistical plotting.
•	Functions: Creates line plots for visualizing trends (e.g., PM2.5, PM10, AQI).
4. tkinter:
•	Purpose: GUI creation.
•	Functions: Builds windows, buttons, labels, and file dialog for user interaction.
5. tkinter.ttk:
•	Purpose: Themed widgets for tkinter.
•	Functions: Creates modern UI elements like comboboxes.
6. matplotlib.backends.backend_tkagg.FigureCanvasTkAgg:
•	Purpose: Embed matplotlib figures into tkinter.
•	Functions: Renders plots as widgets within the tkinter window.



SUMMARY-
The provided Python code is for an interactive air quality data analysis application built with tkinter for the graphical user interface (GUI), and pandas, matplotlib, and seaborn for data processing and visualization. Here's a summary of the key components:
1. Data Loading and Processing:
•	load_data(file_path): Reads a CSV file containing air quality data into a pandas DataFrame.
•	clean_data(df): Cleans the data by dropping rows with missing values in important columns (PM2.5, PM10, AQI), and ensuring that the Date column is in the correct format.
•	aggregate_pm_data(df): Aggregates the data by month, calculating the average PM2.5, PM10, and AQI values for each city.
2. GUI Components:
•	File Load Button: Lets the user load a CSV file.
•	City Selection Dropdown: Displays a dropdown of cities after loading and processing the data.
•	Analyze Button: When clicked, analyzes the data for the selected city and displays three visualizations.
3. Visualizations:
•	PM2.5 and PM10 Trends: A line graph showing trends in PM2.5 and PM10 levels over time.
•	AQI Trends: A line graph showing trends in the Air Quality Index (AQI) over time.
•	AQI Bucket Trends: A line graph showing the average AQI category (e.g., Good, Moderate, Severe) for each month.
4. Error Handling:
•	The program handles file-related errors and shows appropriate error messages if something goes wrong (e.g., file not found or data issues).
•	It shows a warning if the selected city has insufficient data for analysis.
5. Scrollable Graph Window:
•	The plots are displayed in a new window, which is scrollable to accommodate large or multiple graphs.
6. User Experience Features:
•	After the file is loaded and processed, the city selection and analyze button are enabled.
•	The graphs are displayed with options for smooth scrolling.
This application enables users to load air quality data, select a city, and visualize air quality trends over time with detailed plots for PM levels, AQI, and AQI categories.





