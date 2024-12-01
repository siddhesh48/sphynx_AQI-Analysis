import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk


# Load data
def load_data(file_path):
    """Load the air quality data from a CSV file."""
    return pd.read_csv(file_path)

# Clean data
def clean_data(df):
    """Clean the air quality data by handling missing values and ensuring proper types."""
    df = df.dropna(subset=['PM2.5', 'PM10', 'AQI']).copy()
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])
    return df

# Aggregate PM data
def aggregate_pm_data(df):
    """Aggregate PM2.5 and PM10 data by month."""
    df['YearMonth'] = df['Date'].dt.to_period('M')
    return df.groupby(['YearMonth', 'City'])[['PM2.5', 'PM10', 'AQI']].mean().reset_index()

# Visualize PM2.5 and PM10 trends
def visualize_pm_trends(df, city_name):
    """Visualize PM2.5 and PM10 trends for a specific city."""
    city_data = df[df['City'] == city_name].copy()
    city_data['YearMonth'] = city_data['YearMonth'].astype(str)

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=city_data, x='YearMonth', y='PM2.5', label='PM2.5', marker='o')
    sns.lineplot(data=city_data, x='YearMonth', y='PM10', label='PM10', marker='o')
    plt.title(f'Air Quality Trends (PM2.5 and PM10) in {city_name}')
    plt.xlabel('Year-Month')
    plt.ylabel('Concentration (µg/m³)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Visualize AQI trend
def visualize_aqi_trends(df, city_name):
    """Visualize AQI trends for a specific city."""
    city_data = df[df['City'] == city_name].copy()
    city_data['YearMonth'] = city_data['YearMonth'].astype(str)

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=city_data, x='YearMonth', y='AQI', label='AQI', color='red', marker='o')
    plt.title(f'AQI Trends in {city_name}')
    plt.xlabel('Year-Month')
    plt.ylabel('AQI')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# GUI for the application
class AirQualityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Air Quality Data Analysis")
        self.root.geometry("500x300")

        self.df = None
        self.pm_data = None

        # Load file button
        self.load_button = tk.Button(root, text="Load Air Quality Data", command=self.load_file)
        self.load_button.pack(pady=20)

        # City selection
        self.city_label = tk.Label(root, text="Select a City:")
        self.city_label.pack()

        self.city_combobox = ttk.Combobox(root, state="disabled")
        self.city_combobox.pack(pady=10)

        # Analyze button
        self.analyze_button = tk.Button(root, text="Analyze", state="disabled", command=self.analyze_data)
        self.analyze_button.pack(pady=10)

    def load_file(self):
        """Load the CSV file and process the data."""
        file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))

        if file_path:
            try:
                # Load and process data
                self.df = load_data(file_path)
                self.df = clean_data(self.df)

                # Aggregate data for PM trends
                self.pm_data = aggregate_pm_data(self.df)

                # Enable the city selection combobox and analyze button
                cities = self.pm_data['City'].unique()
                self.city_combobox['values'] = cities
                self.city_combobox.set(cities[0])  # Default to first city
                self.city_combobox.config(state="normal")
                self.analyze_button.config(state="normal")
            except FileNotFoundError:
                messagebox.showerror("File Error", "File not found.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def analyze_data(self):
        """Analyze and visualize data based on the selected city."""
        selected_city = self.city_combobox.get()

        if selected_city in self.pm_data['City'].values:
            visualize_pm_trends(self.pm_data, selected_city)
            visualize_aqi_trends(self.pm_data, selected_city)
        else:
            messagebox.showwarning("City Not Found", "Selected city is not available in the data.")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = AirQualityApp(root)
    root.mainloop()
