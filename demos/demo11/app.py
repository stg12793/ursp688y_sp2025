import demo11
import pandas as pd
import geopandas as gpd

import plotly.express as px
from shiny import reactive
from shiny.express import input, ui
from shinywidgets import render_widget
from ipyleaflet import GeoJSON, Map, CircleMarker, basemaps

# Retrieve bike data and join with tracts
tracts_gdf = demo11.load_tracts()
bikes_gdf, stations_gdf = demo11.load_bike_data()
bikes_gdf = pd.concat([
    bikes_gdf[['lat','lon','vehicle_type_id','timestamp','geometry']],
    demo11.expand_stations_into_bikes(stations_gdf)])
bikes_gdf = demo11.attach_tracts_to_bikes(bikes_gdf, tracts_gdf)

# Specify fields and codes for selection
## Bike Type
bike_type_field = 'vehicle_type_id'
bike_type_codes = {
    1: 'Regular Bike',
    2: 'Electric Bike',
}
bikes_gdf[bike_type_field] = bikes_gdf[bike_type_field].map(bike_type_codes)

## Docking Status
bikes_gdf['docking_status'] = bikes_gdf['station_id'].notnull().astype(int)
docking_status_field = 'docking_status'
docking_status_codes = {
    1: 'At Station',
    0: 'Dockless',
}
bikes_gdf[docking_status_field] = bikes_gdf[docking_status_field].map(docking_status_codes)

# Calculate midpoint for mapping
mid_lon, mid_lat = demo11.get_gdf_midpoint(tracts_gdf)


with ui.sidebar():
    
    ui.input_checkbox_group(
        id='bike_type',
        label=ui.HTML('<b>Bike Type</b>'),
        choices=list(bike_type_codes.values()),
        selected=list(bike_type_codes.values()),
        # inline=False,
        # width=None,
    )

    ui.input_checkbox_group(
        id='docking_status',
        label=ui.HTML('<b>Docking Status</b>'),
        choices=list(docking_status_codes.values()),
        selected=list(docking_status_codes.values()),
        # selected=['At Station'],
        # inline=False,
        # width=None,
    )

@render_widget  
def map():

    print(f'Raw bikes: {len(bikes_gdf)}')

    # Filter bikes based on ui criteria (electric/non-electric; docked/undocked)  
    bikes_to_map_df = bikes_gdf[
        (bikes_gdf[bike_type_field].isin(input.bike_type()))
        & (bikes_gdf[docking_status_field].isin(input.docking_status()))
    ].copy()

    print(f'Filtered bikes: {len(bikes_to_map_df)}')

    # Count bikes per tract for mapping
    bikes_per_tract_df = demo11.count_bikes_per_tract(bikes_to_map_df)
    tracts_with_bike_counts_gdf = demo11.attach_counts_to_tract_polygons(bikes_per_tract_df, tracts_gdf)
    tracts_with_bike_counts_gdf = demo11.polygons_to_points(tracts_with_bike_counts_gdf)

    print(f'Bikes being mapped: {tracts_with_bike_counts_gdf.bikes.sum()}')
    print(f'Tracts being mapped: {len(tracts_with_bike_counts_gdf)}')
    
    m = Map(
        basemap=basemaps.CartoDB.Positron,
        center=(mid_lat, mid_lon), 
        zoom=12,
        scroll_wheel_zoom=True,
    )  

    multiplier = 0.2
    tract_counter = 0
    for tract in tracts_with_bike_counts_gdf.itertuples():
        circle_marker = CircleMarker()
        lat = tract.geometry.y
        lon = tract.geometry.x
        print(f'lat: {lat}, lon:{lon}')
        circle_marker.location = (lat, lon)
        radius = demo11.int_at_least_one(tract.bikes * multiplier)
        circle_marker.radius = radius
        circle_marker.color = "red"
        circle_marker.fill_color = "#ffffff00"
        circle_marker.weight=1
        m.add(circle_marker)
        tract_counter += 1
    print(f'Tracts mapped: {tract_counter}')
        
    return m