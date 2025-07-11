
import pickle
import numpy as np
from enterprise.DeckFour import GeoAnalytics
import concurrent.futures

ds=pickle.load(open('data_model.pkl','rb'))
lons=ds['lon']
lats=ds['lat']

filt=np.ones(np.shape(ds['val']))*0

def is_in(x):
    lon,lat,i,j=x
    print(lon)
    if GeoAnalytics.is_inside(lat, lon,shapefile='/home/lakshman/Desktop/States/Admin2.shp'):
        return [1,i,j]
    else:
        return [0,i,j]


with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
    vals=[[lon,lat,i,j] for i,lon in enumerate(lons) for j,lat in enumerate(lats)]
    results = executor.map(is_in, vals)
    for result in results:
        val,i1,j1=result
        filt[j1,i1]=val

pickle.dump({'lon':lons,
             'lat':lats,
             'val':filt},open('filter_model_d03.pkl','wb'))
