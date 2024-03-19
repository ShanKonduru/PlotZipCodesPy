import folium
import pandas as pd

class PlotMe:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.map = None

    def create_map(self):
        # Initialize the map centered around the USA
        self.map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

    def add_markers(self):
        # Add markers for each city
        for index, row in self.data.iterrows():
            lat = row['lat']
            lng = row['lng']
            city = row['city']
            zip = row['zip']
            popup_text = f"City:<strong>{city}</strong>"
            folium.Marker([lat, lng], popup=popup_text).add_to(self.map)

    def generate_map(self, output_file):
        self.create_map()
        self.add_markers()
        self.map.save(output_file)

# Example usage:
data_path = "uszips.csv"
plotter = PlotMe(data_path)
plotter.generate_map("output_map.html")
