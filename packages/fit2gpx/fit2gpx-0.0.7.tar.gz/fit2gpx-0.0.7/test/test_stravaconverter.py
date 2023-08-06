"""File to test the functionalities of the StravaConverter class"""

# %% IMPORT PACKAGES
from fit2gpx import StravaConverter

# %% DIR
DIR_STRAVA = 'C:/Users/doria/Documents/03_Training_and_Learning/Python/Datasets/Strava/strava_20210725'

# %% USE STRAVA CONVERTER TO UNZIP AND CONVERT FITS TO GPX
strava_conv = StravaConverter(
    dir_in=DIR_STRAVA
)

# 1. Unzip activities
strava_conv.unzip_activities()

# 2. Add metadata to existing GPX files
strava_conv.add_metadata_to_gpx()

# 3. Convert FIT to GPX
strava_conv.strava_fit_to_gpx()
