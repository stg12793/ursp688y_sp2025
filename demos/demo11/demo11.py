import json
import requests
import geopandas as gpd
import pandas as pd
import numpy as np


UTM18 = 26918

def save_json(data, file_name, timestamp=False):
    """Save data as json file
    data: json-compatable data structure (nested dicts and lists)
    file_name: string for file name; DO NOT include file extension (e.g., ".json")
    """
    if timestamp:
        file_name = f'{file_name}_{timestamp}.json'
    else:
        file_name = f'{file_name}.json'
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)

def get_and_save_cabi_data():
    """Get current data from the CABI API and save as a timestamped JSON
    """
    # Making a "GET" request
    # response = requests.get('https://gbfs.lyft.com/gbfs/1.1/dca-cabi/en/free_bike_status.json')

    bike_status = requests.get('https://gbfs.lyft.com/gbfs/2.3/dca-cabi/en/free_bike_status.json').json()
    
    
    
    # Get JSON content
    data = response.json()
    return data

def load_tracts():
    """Load tracts from geojson and return as geodataframe
    """
    # Load tracts and clean up table with only the columns we need
    tracts_gdf = gpd.read_file('dc_tracts.geojson')
    tracts_gdf = tracts_gdf[tracts_gdf.geoid.str.len() == 18]
    tracts_gdf = tracts_gdf.rename(columns={
        'geoid':'tract_id',
        'B01003001':'pop'
    })
    tracts_gdf =tracts_gdf[['tract_id','pop','geometry']]
    return tracts_gdf

def load_bike_data():
    """Load bikes from CABI API and return as geodataframe
    """
    bikes_json = requests.get('https://gbfs.lyft.com/gbfs/2.3/dca-cabi/en/free_bike_status.json').json()
    station_status_json = requests.get('https://gbfs.lyft.com/gbfs/2.3/dca-cabi/en/station_status.json').json()
    station_info_json = requests.get('https://gbfs.lyft.com/gbfs/2.3/dca-cabi/en/station_information.json').json()
    
    # Bikes (only includes ebikes)
    bikes_df = pd.DataFrame(bikes_json['data']['bikes'])
    bikes_df['timestamp'] = bikes_json['last_updated']
    bikes_df['timestamp'] = pd.to_datetime(bikes_df['timestamp'], unit='s')
    bikes_gdf = gpd.GeoDataFrame(
        bikes_df, 
        geometry=gpd.points_from_xy(bikes_df.lon, bikes_df.lat), 
        crs=4326
    )
    bikes_gdf['vehicle_type_id'] = bikes_gdf['vehicle_type_id'].astype(int)
    # Stations (includes both e-bikes and regular bikes)
    station_status_df = pd.DataFrame(station_status_json['data']['stations'])    
    station_info_df = pd.DataFrame(station_info_json['data']['stations'])
    stations_df = station_status_df.merge(station_info_df, on='station_id')
    stations_df = stations_df.rename(columns={'last_reported':'timestamp'})
    stations_df['timestamp'] = pd.to_datetime(stations_df['timestamp'], unit='s')
    stations_gdf = gpd.GeoDataFrame(
        stations_df, 
        geometry=gpd.points_from_xy(stations_df.lon, stations_df.lat), 
        crs=4326
    )    
    return bikes_gdf, stations_gdf

def expand_stations_into_bikes(stations_gdf):
    station_bikes = []
    for row in stations_gdf.itertuples():
        for vehicle_type in row.vehicle_types_available:
            for i in range(int(vehicle_type['count'])):
                station_bikes.append({
                    'lat':row.lat,
                    'lon':row.lon,
                    'vehicle_type_id':int(vehicle_type['vehicle_type_id']),
                    'station_id':row.station_id,
                    'timestamp': row.timestamp,
                    'geometry': row.geometry,
                }) 
    return gpd.GeoDataFrame(pd.DataFrame(station_bikes), geometry='geometry', crs=4326)

def attach_tracts_to_bikes(bikes_gdf, tracts_gdf):
    """Spatially join tract IDs to bikes
    """
    bikes_gdf = gpd.sjoin(bikes_gdf, tracts_gdf[['tract_id','geometry']])
    bikes_gdf = bikes_gdf.drop(columns='index_right')
    return bikes_gdf

def count_bikes_per_tract(bikes_gdf):
    return pd.DataFrame(bikes_gdf.groupby('tract_id').size().rename('bikes'))
    
    # return bikes_gdf
    
    # # Count bikes available in each tract
    # bikes_per_tract = bikes_gdf.groupby('tract_id').agg({'index':'nunique', 'timestamp':'first'})
    # bikes_per_tract = bikes_per_tract.rename(columns={'index':'available_bikes'})
    # return bikes_per_tract

# Attach counts to tract polygons
def attach_counts_to_tract_polygons(bikes_per_tract_df, tracts_gdf):
     return tracts_gdf.merge(bikes_per_tract_df, left_on='tract_id', right_index=True)

def proportional_circles_radii(values, multiplier=1):
    """Calculate radii of proportional circles from a column of values given a multiplier
    """
    return np.sqrt(values / 3.14) * multiplier

def replace_polygons_with_proportional_circles(polgyon_gdf, value_col, multiplier=1, calc_crs=UTM18):
    initial_crs = polgyon_gdf.crs
    point_gdf = polgyon_gdf.copy()
    point_gdf = point_gdf.to_crs(calc_crs)
    point_gdf['geometry'] = point_gdf.centroid
    point_gdf['geometry'] = point_gdf.buffer(
        proportional_circles_radii(point_gdf[value_col], multiplier))
    point_gdf = point_gdf.to_crs(initial_crs)
    return point_gdf

def polygons_to_points(polgyon_gdf, calc_crs=UTM18):
    initial_crs = polgyon_gdf.crs
    point_gdf = polgyon_gdf.copy()
    point_gdf = point_gdf.to_crs(calc_crs)
    point_gdf['geometry'] = point_gdf.centroid
    point_gdf = point_gdf.to_crs(initial_crs)
    return point_gdf

def get_gdf_midpoint(gdf):
    """
    Calculate the midpoint of the x and y extents of a GeoDataFrame
    """
    # Get the total bounds: (minx, miny, maxx, maxy)
    minx, miny, maxx, maxy = gdf.total_bounds
    
    # Calculate midpoint values for x and y coordinates.
    mid_x = (minx + maxx) / 2
    mid_y = (miny + maxy) / 2
    
    return float(mid_x), float(mid_y)

def int_at_least_one(num):
    num = int(num)
    if num < 1:
        num = 1
    return num