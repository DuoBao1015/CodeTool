import pandas as pd
from geopy.geocoders import GoogleV3
import geopy.distance
import googlemaps

import tqdm
API = "(here type your googlemap API code)"
geolocator = GoogleV3(api_key=API)
# print(type(geolocator))

file = "(here type your file path)"
df = pd.read_excel(file)
for i in tqdm.tqdm(df.index[:]):
    location = df.loc[i,'School']
    # here is type location list name,For example my list name is School,
    if not pd.isna(location) and location[0] != " ":
        res = geolocator.geocode(location)
        if res:
            df.loc[i,'latitude'] = res.latitude
            df.loc[i,'longitude'] = res.longitude
df.to_excel("3.xlsx", index=False)# Write your code here :-)
#here is output file and only out with xlsx you can change to other file type by other way.
