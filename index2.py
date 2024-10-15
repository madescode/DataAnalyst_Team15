import streamlit as st
import pandas as pd
import pydeck as pdk

# Load the dataset
file_path = 'merged_regions_store_locations.csv'  # Path to your dataset
data = pd.read_csv(file_path)

# Ensure latitude and longitude columns are correctly named
if 'Latitude' in data.columns and 'Longitude' in data.columns:
    data.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'}, inplace=True)
else:
    st.error("Latitude and Longitude columns not found in the dataset.")

# Define color mapping for regions
region_colors = {
    'West': [0, 0, 255],      # Blue for West
    'Midwest': [0, 255, 0],    # Green for Midwest
    'South': [255, 165, 0],    # Orange for South
    'Northeast': [128, 0, 128],  # Purple for Northeast
}

# Assign region colors dynamically
if 'Region' in data.columns:
    data['color'] = data['Region'].map(region_colors)
    # Fill missing values manually using apply
    data['color'] = data['color'].apply(lambda x: [255, 0, 0] if x is None else x)  # Red for missing regions
else:
    st.error("Region column not found in the dataset.")

# Center and scale the elevation data (if 'elevation' column exists)
if 'elevation' in data.columns:
    data['elevation'] = (data['elevation'] - data['elevation'].mean()) / data['elevation'].std()

# Create a 3D HexagonLayer to represent the store distribution with extruded height (population or store count)
hexagon_layer = pdk.Layer(
    'HexagonLayer',
    data=data,
    get_position='[lon, lat]',
    radius=15000,  # Reduced radius for better visual separation
    elevation_scale=50,
    elevation_range=[0, 3000],
    pickable=True,
    extruded=True,
)

# Create a ScatterplotLayer for store locations
scatterplot_layer = pdk.Layer(
    'ScatterplotLayer',
    data=data,
    get_position='[lon, lat]',
    get_color='color',
    get_radius=4000,  # Reduced marker size for better visual separation
    get_fill_color='color',  # Fill the markers with region color
    pickable=True,
    auto_highlight=True,
)

# Define the initial view state of the map
view_state = pdk.ViewState(
    latitude=37.0902,
    longitude=-95.7129,
    zoom=3,  # Reduced initial zoom for a wider view
    pitch=40,
)

# Create a Deck instance combining both layers and customize the tooltip
deck = pdk.Deck(
    layers=[hexagon_layer, scatterplot_layer],
    initial_view_state=view_state,
    tooltip={
        "html": "<b>Store ID:</b> {_StoreID}<br>"
              "<b>State:</b> {State}<br>"
              "<b>Region:</b> {Region}",
        "style": {"backgroundColor": "steelblue", "color": "white"}
    },
)

# Render the map in Streamlit
st.pydeck_chart(deck)