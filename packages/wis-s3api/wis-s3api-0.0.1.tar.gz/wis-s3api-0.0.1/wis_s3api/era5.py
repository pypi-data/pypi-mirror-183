import __init__
import os
import s3fs
import numpy as np
import xarray as xr

endpoint_url = __init__.endpoint_url
access_key = __init__.access_key
secret_key = __init__.secret_key
bucket_path = __init__.bucket_path

fs = s3fs.S3FileSystem(
    client_kwargs={"endpoint_url": endpoint_url}, 
    key=access_key, 
    secret=secret_key
)


start = np.datetime64('2015-01-01T00:00:00.000000000')
end = np.datetime64('2021-12-31T23:00:00.000000000')
box = (115,38,136,54)
variables=[
    '10 metre U wind component',
    '10 metre V wind component',
    '2 metre dewpoint temperature',
    '2 metre temperature',
    'Evaporation',
    'Evaporation from bare soil',
    'Evaporation from open water surfaces excluding oceans',
    'Evaporation from the top of canopy',
    'Evaporation from vegetation transpiration',
    'Forecast albedo',
    'Lake bottom temperature',
    'Lake ice total depth',
    'Lake ice surface temperature',
    'Lake mix-layer depth',
    'Lake mix-layer temperature',
    'Lake shape factor',
    'Lake total layer temperature',
    'Leaf area index, high vegetation',
    'Leaf area index, low vegetation',
    'Potential evaporation',
    'Runoff',
    'Skin reservoir content',
    'Skin temperature',
    'Snow albedo',
    'Snow cover',
    'Snow density',
    'Snow depth',
    'Snow depth water equivalent',
    'Snow evaporation',
    'Snowfall',
    'Snowmelt',
    'Soil temperature level 1',
    'Soil temperature level 2',
    'Soil temperature level 3',
    'Soil temperature level 4',
    'Sub-surface runoff',
    'Surface latent heat flux',
    'Surface net solar radiation',
    'Surface net thermal radiation',
    'Surface pressure',
    'Surface runoff',
    'Surface sensible heat flux',
    'Surface solar radiation downwards',
    'Surface thermal radiation downwards',
    'Temperature of snow layer',
    'Total precipitation',
    'Volumetric soil water layer 1',
    'Volumetric soil water layer 2',
    'Volumetric soil water layer 3',
    'Volumetric soil water layer 4'
]


def open(data_variables=variables, start_time=start, end_time=end, bbox=box):

    ds = xr.open_dataset(
        "reference://", 
        engine="zarr", 
        backend_kwargs={
            "consolidated": False,
            "storage_options": {
                "fo": fs.open('s3://' + bucket_path + 'era5_land/era5_land.json'), 
                "remote_protocol": "s3",
                "remote_options": {
                    'client_kwargs': {'endpoint_url': endpoint_url}, 
                    'key': access_key, 
                    'secret': secret_key}
            }
        }      
    )
    
    ds = ds.filter_by_attrs(long_name=lambda v: v in data_variables)
    ds = ds.rename({"longitude": "lon", "latitude": "lat"})
    ds = ds.transpose('time','lon','lat')
    
    if start_time < start:
        start_time = start
    
    if end_time > end:
        end_time = end
    
    
    times = slice(start_time, end_time)
    ds = ds.sel(time=times)
    
    if bbox[0] < box[0]:
        left = box[0]
    else:
        left = bbox[0]
        
    if bbox[1] < box[1]:
        bottom = box[1]
    else:
        bottom = bbox[1]
    
    if bbox[2] > box[2]:
        right = box[2]
    else:
        right = bbox[2]
    
    if bbox[3] > box[3]:
        top = box[3]
    else:
        top = bbox[3]
    
    longitudes = slice(left - 0.00001, right + 0.00001)
    latitudes = slice(bottom - 0.00001, top + 0.00001)
    
    ds = ds.sortby('lat', ascending=True)
    ds = ds.sel(lon=longitudes, lat=latitudes)
    
    return ds