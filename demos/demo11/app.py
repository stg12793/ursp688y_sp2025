import demo11
import pandas as pd
import geopandas as gpd

import plotly.express as px
from shiny import reactive
from shiny.express import ui, input, render
from shinywidgets import render_plotly, render_widget
from ipyleaflet import GeoJSON, Map, CircleMarker, basemaps


##############
# Prepare data
##############

# Load Data
bikes_gdf, stations_gdf = demo11.load_bike_data()
bikes_gdf = pd.concat([
    bikes_gdf[['lat','lon','vehicle_type_id','timestamp','geometry']],
    demo11.expand_stations_into_bikes(stations_gdf)])
tracts_gdf = demo11.load_tracts()
eea_df = pd.read_csv('mwcog_eea_2016_2020.csv')
eea_df = demo11.clean_eea(eea_df)
nbhds_gdf = demo11.load_nbhds()

# Join equity emphasis area data to tracts
tracts_gdf = tracts_gdf.merge(eea_df, on='tract_id', how='left')

# Add tract data to nbhds with weighted average eea indices
# Also limit to nhbds with tract data
nbhds_gdf = demo11.add_tract_data_to_nbhds(nbhds_gdf, tracts_gdf)

# Attach neighborhoods to bikes
bikes_gdf = demo11.attach_points_to_points(bikes_gdf, nbhds_gdf[['nbhd','geometry']])


######################################
# Define parameters for ui & selection
######################################

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
mid_lon, mid_lat = demo11.get_gdf_midpoint(nbhds_gdf)


###########
# Define ui
###########

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

@render_plotly
def bar_chart():
    # Filter based on inputs
    filtered_bikes_df = demo11.filter_bikes(
        bikes_gdf, 
        {
            bike_type_field: input.bike_type(),
            docking_status_field: input.docking_status(),
        }
    )
    # Attach bikes to neighborhoods
    bikes_per_nbhd_df = demo11.count_bikes_per_nbhd(filtered_bikes_df)

    fig = px.bar(bikes_per_nbhd_df.reset_index(), x="nbhd", y="bikes")
    return fig
    

@render_widget  
def map():

    # Filter based on inputs
    filtered_bikes_df = demo11.filter_bikes(
        bikes_gdf, 
        {
            bike_type_field: input.bike_type(),
            docking_status_field: input.docking_status(),
        }
    )
    
    # Attach bikes to neighborhoods
    bikes_per_nbhd_df = demo11.count_bikes_per_nbhd(filtered_bikes_df)
    nbhds_with_bike_counts_gdf = demo11.attach_counts_to_nbhd_points(bikes_per_nbhd_df, nbhds_gdf) 

    # Build map
    m = Map(
        basemap=basemaps.CartoDB.Positron,
        center=(mid_lat, mid_lon), 
        zoom=12,
        scroll_wheel_zoom=True,
    )  

    multiplier = 0.2
    for nbhd in nbhds_with_bike_counts_gdf.itertuples():
        circle_marker = CircleMarker()
        lat = nbhd.geometry.y
        lon = nbhd.geometry.x
        circle_marker.location = (lat, lon)
        radius = demo11.int_at_least_one(nbhd.bikes * multiplier)
        circle_marker.radius = radius
        circle_marker.color = "red"
        circle_marker.fill_color = "#ffffff00"
        circle_marker.weight=1
        m.add(circle_marker)
        
    return m