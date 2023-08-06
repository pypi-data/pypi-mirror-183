"""File to test functionalities of the Converter class"""

# %% IMPORT PACKAGES
import fit2gpx

# %% DIR
DIR_STRAVA = 'C:/Users/doria/Documents/03_Training_and_Learning/Python/Datasets/Strava/strava_20210725/'

# %% USE STRAVA CONVERTER TO UNZIP AND CONVERT FITS TO GPX
conv = fit2gpx.Converter()

# Test: fit_to_dataframes()
# fname = DIR_STRAVA + 'activities/' + '3323369944.fit'
# df_lap, df_point = conv.fit_to_dataframes(fname)
#
# # Test: dataframe_to_gpx()
# gpx1 = conv.dataframe_to_gpx(df_point)
#
# # Test: fit_to_gpx()
# gpx2 = conv.fit_to_gpx(
#     f_in=fname,
#     f_out='gpx.gpx'
# )
#
# # Test: fit_to_gpx_bulk()
# conv.fit_to_gpx_bulk(
#     dir_in=DIR_STRAVA + 'activities',
#     dir_out='delete'
# )
