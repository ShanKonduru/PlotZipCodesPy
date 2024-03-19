import folium
import pandas as pd
import numpy as np
import random

class PlotMe:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.map = None

    def create_map(self):
        # Initialize the map centered around the USA
        self.map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

    def add_markers(self, num_samples, random_seed=None):
        # Set a random seed for reproducibility
        if random_seed is not None:
            np.random.seed(random_seed)

        # Sample a random subset of data
        sampled_indices = np.random.choice(self.data.index, size=num_samples, replace=False)
        sampled_data = self.data.loc[sampled_indices]

        # Add markers for each randomly selected city
        for index, row in sampled_data.iterrows():
            lat = row['lat']
            lng = row['lng']
            city = row['city']
            popup_text = f"City: {city}"
            folium.Marker([lat, lng], popup=popup_text).add_to(self.map)

    def generate_map(self, output_file, num_samples, random_seed=None):
        self.create_map()
        self.add_markers(num_samples, random_seed)
        self.map.save(output_file)

# Example usage:
data_path = "uszips.csv"
plotter = PlotMe(data_path)
plotter.generate_map("output_map.html", num_samples=10, random_seed=random.randint(1, 50))
