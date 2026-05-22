# Air Quality Analysis

## Team Members

- Siddhesh Tripathi — KU2407U378
- Rehan Khan — KU2407U363
- Niraj Matai — KU2407U341
- Niyati Joshi — KU2407U342
- Nidhi Kotian — KU2407U339

---

## Project Overview

Air Quality Analysis is a Python-based application developed to analyze and visualize air quality trends using PM2.5, PM10, and AQI data.

The project focuses on transforming raw air quality datasets into meaningful visual representations that help users better understand pollution trends over time across different cities.

The application provides an interactive graphical interface that allows users to load datasets, select cities, and generate analytical visualizations.

---

## Objectives

The main objectives of this project are:

- Analyze air quality data using PM2.5 and PM10 concentration levels
- Visualize AQI trends over different time periods
- Compare PM2.5 and PM10 pollutant levels
- Highlight AQI categories for easier interpretation of air quality conditions
- Provide interactive visualizations for improved data exploration

This project focuses entirely on data analysis and visualization and does not include predictive modeling.

---

## Features

- CSV-based dataset loading
- Data cleaning and preprocessing
- Monthly aggregation of AQI and pollutant values
- Interactive city selection
- Visualization of:
  - PM2.5 trends
  - PM10 trends
  - AQI trends
  - AQI category trends
- Scrollable graph display window
- Error handling for invalid or incomplete data

---

## Libraries Used

### Pandas
Used for:
- Reading CSV datasets
- Handling missing values
- Data manipulation and aggregation

### Matplotlib
Used for:
- Plot generation
- Data visualization
- Graph customization

### Seaborn
Used for:
- Statistical data visualization
- Enhanced graph styling and trend analysis

### Tkinter
Used for:
- Building the graphical user interface
- Creating buttons, labels, and dialogs

### Tkinter.ttk
Used for:
- Themed UI widgets
- Dropdown menus and modern interface elements

### FigureCanvasTkAgg
Used for:
- Embedding Matplotlib plots into the Tkinter application window

---

## Application Workflow

### 1. Data Loading
The application loads AQI datasets from CSV files using Pandas.

### 2. Data Cleaning
The dataset is cleaned by:
- Removing rows with missing PM2.5, PM10, or AQI values
- Converting date columns into proper datetime format

### 3. Data Aggregation
The data is grouped monthly to calculate average:
- PM2.5 levels
- PM10 levels
- AQI values

### 4. Visualization
The application generates graphical visualizations for the selected city.

---

## Visualizations

### PM2.5 and PM10 Trend Analysis
Displays monthly trends in PM2.5 and PM10 pollutant concentrations.

### AQI Trend Analysis
Shows variations in Air Quality Index values over time.

### AQI Category Analysis
Visualizes AQI category distributions such as:
- Good
- Moderate
- Poor
- Severe

---

## GUI Components

The graphical interface includes:

- File upload button
- City selection dropdown menu
- Analyze button
- Scrollable graph window
- Dynamically rendered plots

---

## Error Handling

The application includes multiple error-handling mechanisms, including:

- Invalid file detection
- Missing data handling
- Warning messages for insufficient data
- Exception handling during processing and visualization

---

## Project Structure

```plaintext
Air-Quality-Analysis/
│
├── main.py
├── dataset.csv
├── README.md
└── assets/
```

---

## How to Run the Project

### Clone the Repository

```bash
git clone <repository-link>
cd Air-Quality-Analysis
```

### Install Required Libraries

```bash
pip install pandas matplotlib seaborn
```

### Run the Application

```bash
python main.py
```

---

## Future Improvements

Possible future enhancements include:

- Real-time AQI API integration
- Interactive dashboards
- Geographic AQI mapping
- Advanced filtering options
- Predictive AQI analysis using machine learning
- Exportable reports and graphs

---

## Conclusion

This project demonstrates the use of Python for environmental data analysis and visualization through an interactive desktop application.

It combines data processing, graphical visualization, and GUI development to provide users with an effective way to explore and understand air quality trends.
