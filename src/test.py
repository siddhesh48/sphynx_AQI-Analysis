import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
                cleaned_cities = [city.strip("'") for city in cities]  # Remove single quotes
                self.city_combobox['values'] = cleaned_cities
                self.city_combobox.set(cleaned_cities[0])  # Default to first city

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
            # Create a new window for the graphs
            graph_window = tk.Toplevel(self.root)
            graph_window.title(f"Air Quality Analysis: {selected_city}")
            graph_window.geometry("1000x800")  # Window size

            # Create a scrollable frame with vertical scrolling
            canvas = tk.Canvas(graph_window, width=1000, height=800)
            scroll_y = tk.Scrollbar(graph_window, orient="vertical", command=canvas.yview)
            frame = tk.Frame(canvas)

            frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            canvas.create_window((0, 0), window=frame, anchor="nw")
            canvas.configure(yscrollcommand=scroll_y.set)

            # Bind the mouse wheel for smooth scrolling
            def _on_mouse_wheel(event):
                canvas.yview_scroll(-1 * int(event.delta / 120), "units")

            canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

            # Place the canvas and scrollbar in the window
            canvas.pack(side="left", fill="both", expand=True)
            scroll_y.pack(side="right", fill="y")

            # Plot PM2.5 and PM10 trends
            city_data = self.pm_data[self.pm_data['City'] == selected_city].copy()
            city_data['YearMonth'] = city_data['YearMonth'].astype(str)

            fig1, ax1 = plt.subplots(figsize=(13, 6))  # Keep graphs compact
            sns.lineplot(data=city_data, x='YearMonth', y='PM2.5', label='PM2.5', marker='o', ax=ax1)
            sns.lineplot(data=city_data, x='YearMonth', y='PM10', label='PM10', marker='o', ax=ax1)
            ax1.set_title(f'Air Quality Trends (PM2.5 and PM10) in {selected_city}')
            ax1.set_xlabel('Year-Month')
            ax1.set_ylabel('Concentration (µg/m³)')
            ax1.set_xticks(city_data['YearMonth'][::3])  # Show every 3rd month
            ax1.tick_params(axis='x', rotation=45)
            ax1.legend()
            ax1.grid(True)

            canvas1 = FigureCanvasTkAgg(fig1, frame)
            canvas1.get_tk_widget().pack(pady=10)

            # Plot AQI trends
            fig2, ax2 = plt.subplots(figsize=(13, 6))
            sns.lineplot(data=city_data, x='YearMonth', y='AQI', label='AQI', color='red', marker='o', ax=ax2)
            ax2.set_title(f'AQI Trends in {selected_city}')
            ax2.set_xlabel('Year-Month')
            ax2.set_ylabel('AQI')
            ax2.set_xticks(city_data['YearMonth'][::3])  # Show every 3rd month
            ax2.tick_params(axis='x', rotation=45)
            ax2.grid(True)

            canvas2 = FigureCanvasTkAgg(fig2, frame)
            canvas2.get_tk_widget().pack(pady=10)

            # Plot AQI_Bucket trends
            aqi_bucket_data = self.df[self.df['City'] == selected_city].dropna(subset=['AQI_Bucket'])
            aqi_bucket_data['Month'] = pd.to_datetime(aqi_bucket_data['Date']).dt.strftime('%Y-%m')

            bucket_mapping = {
                "Good": 1,
                "Satisfactory": 2,
                "Moderate": 3,
                "Poor": 4,
                "Very Poor": 5,
                "Severe": 6
            }
            aqi_bucket_data['AQI_Bucket_Num'] = aqi_bucket_data['AQI_Bucket'].map(bucket_mapping)
            bucket_trend = aqi_bucket_data.groupby('Month')['AQI_Bucket_Num'].mean().reset_index()

            fig3, ax3 = plt.subplots(figsize=(13, 6))
            sns.lineplot(data=bucket_trend, x='Month', y='AQI_Bucket_Num', marker='o', ax=ax3)
            ax3.set_title(f'AQI Bucket Trends (Monthly Average) in {selected_city}')
            ax3.set_xlabel('Month')
            ax3.set_ylabel('AQI Bucket (1=Good, 6=Severe)')
            ax3.set_xticks(bucket_trend['Month'][::3])  # Show every 3rd month
            ax3.tick_params(axis='x', rotation=45)
            ax3.grid(True)

            canvas3 = FigureCanvasTkAgg(fig3, frame)
            canvas3.get_tk_widget().pack(pady=10)

        else:
            messagebox.showwarning("City Not Found", "Not enough data is available for this city.")






# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = AirQualityApp(root)
    root.mainloop()
