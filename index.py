# import streamlit as st
# import pandas as pd
# import folium
# from streamlit_folium import st_folium

# # Baca dataset CSV
# merged_regions_store_locations = pd.read_csv('merged_regions_store_locations.csv')

# # Inisialisasi peta dengan titik awal (koordinat pusat)
# center_lat = merged_regions_store_locations['Latitude'].mean()
# center_lon = merged_regions_store_locations['Longitude'].mean()
# m = folium.Map(location=[center_lat, center_lon], zoom_start=5)

# # Fungsi untuk mengatur warna marker berdasarkan region
# def get_marker_color(region):
#     if region == 'Midwest':
#         return 'blue'
#     elif region == 'West':
#         return 'green'
#     elif region == 'South':
#         return 'red'
#     else:
#         return 'gray'  # default color for other regions

# # Tambahkan marker lokasi toko ke peta dengan warna berdasarkan region
# for _, row in merged_regions_store_locations.iterrows():
#     folium.Marker(
#         location=[row['Latitude'], row['Longitude']],
#         popup=f"City: {row['City Name']}<br>Region: {row['Region']}<br>State: {row['State_x']}",
#         icon=folium.Icon(color=get_marker_color(row['Region']), icon="info-sign"),
#     ).add_to(m)

# # Tampilkan peta di Streamlit
# st.title('Visualisasi Lokasi Toko dengan Marker Berwarna Berdasarkan Region')
# st.write('Peta ini menampilkan lokasi toko berdasarkan region dengan warna marker yang berbeda.')
# st_data = st_folium(m, width=800, height=500)


# import pandas as pd
# import folium
# from folium.plugins import AntPath
# import streamlit as st
# from streamlit_folium import st_folium

# # Load dataset
# df = pd.read_csv('merged_regions_store_locations.csv')

# # Function to create color based on region
# def get_region_color(region):
#     if region == 'South':
#         return 'blue'
#     elif region == 'Midwest':
#         return 'green'
#     elif region == 'West':
#         return 'red'
#     else:
#         return 'black'

# # Streamlit app title
# st.title("Store Locations and Connections by Region")

# # Create a folium map centered on the US
# m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

# # Add store locations and paths between stores
# regions = df['Region'].unique()
# for region in regions:
#     region_data = df[df['Region'] == region]
    
#     # Get the region color
#     region_color = get_region_color(region)
    
#     # Add markers for each store in the region
#     for i, row in region_data.iterrows():
#         folium.Marker(
#             location=[row['Latitude'], row['Longitude']],
#             popup=f"{row['_StoreID']} ({row['Region']})",
#             icon=folium.Icon(color=region_color)
#         ).add_to(m)
    
#     # Create paths between stores in the same region
#     locations = region_data[['Latitude', 'Longitude']].values.tolist()
#     for i in range(len(locations) - 1):
#         AntPath(locations=[locations[i], locations[i + 1]],
#                 color=region_color, 
#                 weight=2.5,
#                 opacity=0.6).add_to(m)

# # Display the map in the Streamlit app
# st_data = st_folium(m, width=700, height=500)


import streamlit as st
import folium
from folium.plugins import Fullscreen, AntPath
from streamlit_folium import st_folium
import pandas as pd

# Load the dataset
file_path = 'merged_regions_store_locations.csv'  # Update with your file path
data = pd.read_csv(file_path)

# Streamlit app title
st.title("Penyebaran Lokasi Tokoh di Amerika Serikat berdasarkan Region")

# Map initialization
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# Add fullscreen button
Fullscreen(position='topright').add_to(m)

# Define color mapping for regions
region_colors = {
    'West': 'blue',
    'Midwest': 'green',
    'South': 'orange',
    'Northeast': 'purple'
}

# Initialize a dictionary to store coordinates by region
region_coords = {
    'West': [],
    'Midwest': [],
    'South': [],
    'Northeast': []
}

# Loop over each row to add markers, popups, and store coordinates by region
for _, row in data.iterrows():
    popup_text = f'Store ID: {row["_StoreID"]}, City: {row["City Name"]}, State: {row["State_x"]}, Region: {row["Region"]}, Population {row["Population"]}'
    color = region_colors.get(row['Region'], 'black')
    
    # Add marker with popup
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=popup_text,
        icon=folium.Icon(color=color, icon='info-sign')
    ).add_to(m)
    
    # Store coordinates for AntPath by region
    region_coords[row['Region']].append([row['Latitude'], row['Longitude']])

# Draw AntPath connecting store locations by region
for region, coords in region_coords.items():
    if len(coords) > 1:  # Ensure there are at least 2 locations to connect
        AntPath(locations=coords, color=region_colors[region], weight=2.5, dash_array=[10, 20], delay=1000).add_to(m)

# Display the map in the Streamlit app
st_data = st_folium(m, width=700, height=500)






