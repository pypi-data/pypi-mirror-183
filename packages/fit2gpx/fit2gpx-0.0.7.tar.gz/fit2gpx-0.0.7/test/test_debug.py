from src.fit2gpx import StravaConverter, Converter
import fitdecode

# conv = StravaConverter('./')
# conv.unzip_activities()
#
conv_simple = Converter()

f_in1 = './activities/8718041686.fit'
f_out1 = './activities/8718041686.gpx'

f_in2 = './activities/6224452127.fit'
f_out2 = './activities/6224452127.gpx'

f_in3 = './activities/9969649032.fit'
f_out3 = './activities/9969649032.gpx'

df_laps, df_points = conv_simple.fit_to_dataframes(f_in1)
conv_simple.fit_to_gpx(f_in1, f_out1)


