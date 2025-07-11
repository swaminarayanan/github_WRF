import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Load datasets
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/ferrier_20190421.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/data/ferrier_20200303.nc')
ds3 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20190421.nc')
ds4 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20200303.nc')
ds5 = xr.open_dataset(r'/media/lab/My Passport/hail/data/morrison_20190421.nc')
ds6 = xr.open_dataset(r'/media/lab/My Passport/hail/data/morrison_20200303.nc')
ds7 = xr.open_dataset(r'/media/lab/My Passport/hail/data/thompson_20190421.nc')
ds8 = xr.open_dataset(r'/media/lab/My Passport/hail/data/thompson_20200303.nc')
ds9 = xr.open_dataset(r'/media/lab/My Passport/hail/data/wsm6_20190421.nc')
ds10 = xr.open_dataset(r'/media/lab/My Passport/hail/data/wsm6_20200303.nc')
##########################33
da = ds1.sel(lon=slice(86.6, 87), lat=slice(20.9, 21.5)).isel(time=17)
db = ds2.sel(lon=slice(84, 86), lat=slice(22, 24)).isel(time=16)
dc = ds3.sel(lon=slice(86.6, 87), lat=slice(20.9, 21.5)).isel(time=17)
dd = ds4.sel(lon=slice(84, 86), lat=slice(22, 24)).isel(time=17)
de = ds5.sel(lon=slice(86.6, 87), lat=slice(20.9, 21.5)).isel(time=17)
df = ds6.sel(lon=slice(84, 86), lat=slice(22, 24)).isel(time=15)
dg = ds7.sel(lon=slice(86.6, 87), lat=slice(20.9, 21.5)).isel(time=17)
dh = ds8.sel(lon=slice(84, 86), lat=slice(22, 24)).isel(time=17)
di = ds9.sel(lon=slice(86.6, 87), lat=slice(20.9, 21.5)).isel(time=17)
dj = ds10.sel(lon=slice(84, 86), lat=slice(22, 24)).isel(time=17)
do = ds3.sel(lon=slice(86, 88), lat=slice(20, 22)).isel(time=19)
# # Extract vapor values
# va = ds1['qvapor'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+03# This case actual time is 17 step
# vb = ds2['qvapor'].sel(lon=84.87, lat=22.82, method='nearest').isel(time=16).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# vc = ds3['qvapor'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# vd = ds4['qvapor'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# ve = ds5['qvapor'].sel(lon=86.9, lat=21.36, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# vf = ds6['qvapor'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+03# This case actual time is 17 step
# vg = ds7['qvapor'].sel(lon=86.91, lat=21.5, method='nearest').isel(time=16).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# vh = ds8['qvapor'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# vi = ds9['qvapor'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+03# This case actual time is 17 step
# vj = ds10['qvapor'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# ################ vapour mixing ratio Extract rain values
va = da['qvapor']
vb = db['qvapor']
vc = dc['qvapor']
vd = dd['qvapor']
ve = de['qvapor']
vf = df['qvapor']
vg = dg['qvapor']
vh = dh['qvapor']
vi = di['qvapor']
vj = dj['qvapor']
va = va.isel(lon=19, lat=6).squeeze()/ 1*1.0e+03
vb = vb.isel(lon=47, lat=80).squeeze()/ 1*1.0e+03
vc = vc.isel(lon=21, lat=26).squeeze()/ 1*1.0e+03
vd = vd.isel(lon=58, lat=51).squeeze()/ 1*1.0e+03
ve = ve.isel(lon=18, lat=6).squeeze()/ 1*1.0e+03
vf = vf.isel(lon=9, lat=68).squeeze()/ 1*1.0e+03
vg = vg.isel(lon=19, lat=5).squeeze()/ 1*1.0e+03
vh = vh.isel(lon=15, lat=80).squeeze()/ 1*1.0e+03
vi = vi.isel(lon=17, lat=11).squeeze()/ 1*1.0e+03
vj = vj.isel(lon=15, lat=80).squeeze()/ 1*1.0e+03

# ra = ds1['qrain'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+03# This case actual time is 17 step
# rb = ds2['qrain'].sel(lon=84.87, lat=22.82, method='nearest').isel(time=16).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# rc = ds3['qrain'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# rd = ds4['qrain'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# re = ds5['qrain'].sel(lon=86.9, lat=21.36, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# rf = ds6['qrain'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+03# This case actual time is 17 step
# rg = ds7['qrain'].sel(lon=86.91, lat=21.5, method='nearest').isel(time=16).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# rh = ds8['qrain'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# ri = ds9['qrain'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+03# This case actual time is 17 step
# rj = ds10['qrain'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
###########rain mixing ratio##################### 
ra = da['qrain']
rb = db['qrain']
rc = dc['qrain']
rd = dd['qrain']
re = de['qrain']
rf = df['qrain']
rg = dg['qrain']
rh = dh['qrain']
ri = di['qrain']
rj = dj['qrain']
ra = ra.isel(lon=15, lat=10).squeeze()/ 1*1.0e+03
rb = rb.isel(lon=2, lat=89).squeeze()/ 1*1.0e+03
rc = rc.isel(lon=7, lat=26).squeeze()/ 1*1.0e+03
rd = rd.isel(lon=62, lat=50).squeeze()/ 1*1.0e+03
re = re.isel(lon=5, lat=20).squeeze()/ 1*1.0e+03
rf = rf.isel(lon=41, lat=78).squeeze()/ 1*1.0e+03
rg = rg.isel(lon=3, lat=25).squeeze()/ 1*1.0e+03
rh = rh.isel(lon=67, lat=72).squeeze()/ 1*1.0e+03
ri = ri.isel(lon=5, lat=19).squeeze()/ 1*1.0e+03
rj = rj.isel(lon=77, lat=55).squeeze()/ 1*1.0e+03

#### Extract cloud values
# ca = ds1['qcloud'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+03# This case actual time is 17 step
# cb = ds2['qcloud'].sel(lon=84.87, lat=22.82, method='nearest').isel(time=16).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# cc = ds3['qcloud'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# cd = ds4['qcloud'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# ce = ds5['qcloud'].sel(lon=86.9, lat=21.36, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# cf = ds6['qcloud'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+03# This case actual time is 17 step
# cg = ds7['qcloud'].sel(lon=86.91, lat=21.5, method='nearest').isel(time=16).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# ch = ds8['qcloud'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# ci = ds9['qcloud'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+03# This case actual time is 17 step
# cj = ds10['qcloud'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
####cloud mixing ratio##################
ca = da['qcloud']
cb = db['qcloud']
cc = dc['qcloud']
cd = dd['qcloud']
ce = de['qcloud']
cf = df['qcloud']
cg = dg['qcloud']
ch = dh['qcloud']
ci = di['qcloud']
cj = dj['qcloud']
ca = ca.isel(lon=1, lat=1).squeeze()/ 1*1.0e+03
cb = cb.isel(lon=17, lat=73).squeeze()/ 1*1.0e+03
cc = cc.isel(lon=12, lat=7).squeeze()/ 1*1.0e+03
cd = cd.isel(lon=17, lat=69).squeeze()/ 1*1.0e+03
ce = ce.isel(lon=11, lat=9).squeeze()/ 1*1.0e+03
cf = cf.isel(lon=34, lat=82).squeeze()/ 1*1.0e+03
cg = cg.isel(lon=12, lat=9).squeeze()/ 1*1.0e+03
ch = ch.isel(lon=14, lat=71).squeeze()/ 1*1.0e+03
ci = ci.isel(lon=1, lat=3).squeeze()/ 1*1.0e+03
cj = cj.isel(lon=73, lat=69).squeeze()/ 1*1.0e+03

# # Extract graupel values
# # ga = ds1['qgraup'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+03# This case actual time is 17 step
# # gb = ds2['qgraup'].sel(lon=84.87, lat=22.82, method='nearest').isel(time=16).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# gc = ds3['qgraup'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# gd = ds4['qgraup'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# ge = ds5['qgraup'].sel(lon=86.9, lat=21.36, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# gf = ds6['qgraup'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+03# This case actual time is 17 step
# gg = ds7['qgraup'].sel(lon=86.91, lat=21.5, method='nearest').isel(time=16).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# gh = ds8['qgraup'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# gi = ds9['qgraup'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+03# This case actual time is 17 step
# gj = ds10['qgraup'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
############graupel mixing ratio # Extract ice values
# ga = da['qgraup']
# gb = dc['qgraup']
gc = dc['qgraup']
gd = dd['qgraup']
ge = de['qgraup']
gf = df['qgraup']
gg = dg['qgraup']
gh = dh['qgraup']
gi = di['qgraup']
gj = dj['qgraup']
# ga = ga.isel(lon=69, lat=51).squeeze()/ 1*1.0e+03
# gb = gb.isel(lon=2, lat=89).squeeze()/ 1*1.0e+03
gc = gc.isel(lon=8, lat=23).squeeze()/ 1*1.0e+03
gd = gd.isel(lon=66, lat=55).squeeze()/ 1*1.0e+03
ge = ge.isel(lon=6, lat=23).squeeze()/ 1*1.0e+03
gf = gf.isel(lon=29, lat=79).squeeze()/ 1*1.0e+03
gg = gg.isel(lon=3, lat=25).squeeze()/ 1*1.0e+03
gh = gh.isel(lon=16, lat=60).squeeze()/ 1*1.0e+03
gi = gi.isel(lon=6, lat=22).squeeze()/ 1*1.0e+03
gj = gj.isel(lon=71, lat=71).squeeze()/ 1*1.0e+03

# i_a = ds1['qice'].sel(lon=86.95, lat=21.54, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+01# This case actual time is 17 step
# i_b = ds2['qice'].sel(lon=84.87, lat=22.82, method='nearest').isel(time=16).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# i_c = ds3['qice'].sel(lon=87.04, lat=21.474, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# i_d = ds4['qice'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# i_e = ds5['qice'].sel(lon=86.9, lat=21.36, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# i_f = ds6['qice'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+03# This case actual time is 17 step
# i_g = ds7['qice'].sel(lon=86.91, lat=21.5, method='nearest').isel(time=16).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# i_h = ds8['qice'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# i_i = ds9['qice'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+03# This case actual time is 17 step
# i_j = ds10['qice'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
##################ice mixing ratio
i_a = da['qice']
i_b = db['qice']
i_c = do['qice']
i_d = dd['qice']
i_e = de['qice']
i_f = df['qice']
i_g = dg['qice']
i_h = dh['qice']
i_i = di['qice']
i_j = dj['qice']
i_a = i_a.isel(lon=21, lat=slice(2, 4)).squeeze().mean(dim=['lat']) / 1*1.0e+03
i_b = i_b.isel(lon=55, lat=62).squeeze()/ 1*1.0e+03
i_c = i_c.isel(lon=slice(34, 40), lat=47).squeeze().mean(dim=['lon']) / 1*1.0e+03
i_d = i_d.isel(lon=56, lat=80).squeeze()/ 1*1.0e+03
i_e = i_e.isel(lon=7, lat=22).squeeze()/ 1*1.0e+03
i_f = i_f.isel(lon=43, lat=57).squeeze()/ 1*1.0e+03
i_g = i_g.isel(lon=5, lat=24).squeeze()/ 1*1.0e+03
i_h = i_h.isel(lon=66, lat=53).squeeze()/ 1*1.0e+03
i_i = i_i.isel(lon=7, lat=23).squeeze()/ 1*1.0e+03
i_j = i_j.isel(lon=30, lat=85).squeeze()/ 1*1.0e+03

# i_a = i_a.isel(lon=20, lat=34).squeeze()/ 1*1.0e+03
# i_b = i_b.isel(lon=55, lat=62).squeeze()/ 1*1.0e+03
# i_c = i_c.isel(lon=18, lat=35).squeeze()/ 1*1.0e+03
# i_d = i_d.isel(lon=56, lat=80).squeeze()/ 1*1.0e+03
# i_e = i_e.isel(lon=7, lat=22).squeeze()/ 1*1.0e+03
# i_f = i_f.isel(lon=43, lat=57).squeeze()/ 1*1.0e+03
# i_g = i_g.isel(lon=5, lat=24).squeeze()/ 1*1.0e+03
# i_h = i_h.isel(lon=66, lat=53).squeeze()/ 1*1.0e+03
# i_i = i_i.isel(lon=7, lat=23).squeeze()/ 1*1.0e+03
# i_j = i_j.isel(lon=30, lat=85).squeeze()/ 1*1.0e+03

# # Extract snow values
# # sa = ds1['qsnow'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+03# This case actual time is 17 step
# # sb = ds2['qsnow'].sel(lon=84.87, lat=22.82, method='nearest').isel(time=16).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# sc = ds3['qsnow'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# sd = ds4['qsnow'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# se = ds5['qsnow'].sel(lon=86.9, lat=21.36, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# sf = ds6['qsnow'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+03# This case actual time is 17 step
# sg = ds7['qsnow'].sel(lon=86.91, lat=21.5, method='nearest').isel(time=16).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# sh = ds8['qsnow'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
# si = ds9['qsnow'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 / 1*1.0e+03# This case actual time is 17 step
# sj = ds10['qsnow'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 / 1*1.0e+03
#snow mixing rato # Extract reflectivity values
# sa = da['qsnow']
# sb = db['qsnow']
sc = dc['qsnow']
sd = dd['qsnow']
se = de['qsnow']
sf = df['qsnow']
sg = dg['qsnow']
sh = dh['qsnow']
si = di['qsnow']
sj = dj['qsnow']
# sa = sa.isel(lon=69, lat=51).squeeze()/ 1*1.0e+03
# sb = sb.isel(lon=2, lat=89).squeeze()/ 1*1.0e+03
sc = sc.isel(lon=14, lat=30).squeeze()/ 1*1.0e+03
sd = sd.isel(lon=68, lat=65).squeeze()/ 1*1.0e+03
se = se.isel(lon=5, lat=23).squeeze()/ 1*1.0e+03
sf = sf.isel(lon=46, lat=55).squeeze()/ 1*1.0e+03
sg = sg.isel(lon=6, lat=34).squeeze()/ 1*1.0e+03
sh = sh.isel(lon=69, lat=47).squeeze()/ 1*1.0e+03
si = si.isel(lon=7, lat=23).squeeze()/ 1*1.0e+03
sj = sj.isel(lon=72, lat=71).squeeze()/ 1*1.0e+03

# da = ds1['dbz'].isel(time=15, lon=69, lat=51).squeeze()/ 1*1.0e+03# / 1*1.0e+03# This case actual time is 17 step
# db = ds2['dbz'].isel(time=16, lon=51, lat=69).squeeze()/ 1*1.0e+03# / 1*1.0e+03
# dc = ds3['dbz'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03# / 1*1.0e+03
# dd = ds4.sel(lon=slice(84, 86), lat=slice(22, 24)).isel(time=17)# / 1*1.0e+03
# de = ds5['dbz'].sel(lon=86.9, lat=21.36, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03# / 1*1.0e+03
# df = ds6['dbz'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03 #/ 1*1.0e+03# This case actual time is 17 step
# dg = ds7['dbz'].sel(lon=86.91, lat=21.5, method='nearest').isel(time=16).squeeze()/ 1*1.0e+03 #/ 1*1.0e+03
# dh = ds8['dbz'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03 #/ 1*1.0e+03
# di = ds9['dbz'].sel(lon=86.95, lat=21.5, method='nearest').isel(time=15).squeeze()/ 1*1.0e+03# / 1*1.0e+03# This case actual time is 17 step
# dj = ds10['dbz'].sel(lon=85.05, lat=22.95, method='nearest').isel(time=17).squeeze()/ 1*1.0e+03# / 1*1.0e+03
# dd = dd['dbz'].squeeze()/ 1*1.0e+03
###### Reflectivity
da1 = da['dbz']
db1 = db['dbz']
dc1 = dc['dbz']
dd1 = dd['dbz']
de1 = de['dbz']
df1 = df['dbz']
dg1 = dg['dbz']
dh1 = dh['dbz']
di1 = di['dbz']
dj1 = dj['dbz']
da1 = da1.isel(lon=15, lat=10).squeeze()
db1 = db1.isel(lon=2, lat=89).squeeze()
dc1 = dc1.isel(lon=6, lat=34).squeeze()
dd1 = dd1.isel(lon=79, lat=57).squeeze()
de1 = de1.isel(lon=6, lat=23).squeeze()
df1 = df1.isel(lon=24, lat=65).squeeze()
dg1 = dg1.isel(lon=4, lat=25).squeeze()
dh1 = dh1.isel(lon=16, lat=60).squeeze()
di1 = di1.isel(lon=5, lat=20).squeeze()
dj1 = dj1.isel(lon=70, lat=72).squeeze()

#####################2019/04/21######## 1 st case

fig = plt.figure(figsize=(21, 19))
gs = gridspec.GridSpec(3, 3, width_ratios=[1, 1, 1], wspace=0.12, hspace=0.38)  # Adjusted to 3 columns
# mpl.rcParams['figure.facecolor'] = 'white'
# fig.patch.set_facecolor('lightblue')  # Set background color for the entire figure
ax1 = fig.add_subplot(gs[0, 0])  # First column
# ax1.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax1.plot(va.values, va['lev'], color='b', linewidth=2, label='Ferrier')  # Example plot on top axis
ax1.plot(vc.values, vc['lev'], color='r', linewidth=2, label='Milbrandt')  # Example plot on top axis
ax1.plot(ve.values, ve['lev'], color='g', linewidth=2, label='Thompson')  # Example plot on top axis
ax1.plot(vg.values, vg['lev'], color='y', linewidth=2, label='Morrison')  # Example plot on top axis
ax1.plot(vi.values, vi['lev'], color='k', linewidth=2, label='Wsm6')  # Example plot on top axis
ax1.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=22)
ax1.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax1.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax1.invert_yaxis()  # Invert y-axis
# ax1.legend(fontsize=10)
ax1.set_title('(a)  ', fontweight='bold', fontsize=18)
ax1.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax1.set_xticks(np.arange(0, 20.1, 4))  # Set ticks on the top x-axis
ax1.set_xlim([0, 20])  # Adjust top axis limits to match top axis data range
# ax1.set_xlim([])
ax1.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax1.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
ax1.set_xlabel(r'Vapor Mixing ratio (g/kg)', fontweight='bold', fontsize=17)
ax1.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax2 = fig.add_subplot(gs[0, 1])  # First column
# ax2.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax2.plot(ra.values, ra['lev'], color='b', linewidth=2)  # Example plot on top axis
ax2.plot(rc.values, rc['lev'], color='r', linewidth=2)  # Example plot on top axis
ax2.plot(re.values, re['lev'], color='g', linewidth=2)  # Example plot on top axis
ax2.plot(rg.values, rg['lev'], color='y', linewidth=2)  # Example plot on top axis
ax2.plot(ri.values, ri['lev'], color='k', linewidth=2)  # Example plot on top axis
ax2.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax2.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax2.invert_yaxis()  # Invert y-axis
ax2.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax2.set_title('(b)  ', fontweight='bold', fontsize=18)

ax2.set_xticks(np.arange(0, 7.1, 1))  # Set ticks on the top x-axis
ax2.set_xlim([0, 7])  # Adjust top axis limits to match top axis data range
ax2.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax2.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
ax2.set_yticklabels([])
ax2.set_xlabel(r'Rain Mixing ratio (g/kg)', fontweight='bold', fontsize=17)
ax2.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax3 = fig.add_subplot(gs[0, 2])  # First column
# ax3.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax3.plot(ca.values, ca['lev'], color='b', linewidth=2)  # Example plot on top axis
ax3.plot(cc.values, cc['lev'], color='r', linewidth=2)  # Example plot on top axis
ax3.plot(ce.values, ce['lev'], color='g', linewidth=2)  # Example plot on top axis
ax3.plot(cg.values, cg['lev'], color='y', linewidth=2)  # Example plot on top axis
ax3.plot(ci.values, ci['lev'], color='k', linewidth=2)  # Example plot on top axis
ax3.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax3.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax3.invert_yaxis()  # Invert y-axis
ax3.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax3.set_title('(c)  ', fontweight='bold', fontsize=18)
ax3.set_xticks(np.arange(0, 5.51, 0.5))  # Set ticks on the top x-axis
ax3.set_xlim([0, 5])  # Adjust top axis limits to match top axis data range
ax3.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax3.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
ax3.set_yticklabels([])
ax3.set_xlabel(r'Cloud Mixing ratio (g/kg)', fontweight='bold', fontsize=17)
ax3.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax4 = fig.add_subplot(gs[1, 0])  # First column
# ax4.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
# ax4.plot(ga.values, ga['lev'], color='b', linewidth=2)  # Example plot on top axis
ax4.plot(gc.values, gc['lev'], color='r', linewidth=2)  # Example plot on top axis
ax4.plot(ge.values, ge['lev'], color='g', linewidth=2)  # Example plot on top axis
ax4.plot(gg.values, gg['lev'], color='y', linewidth=2)  # Example plot on top axis
ax4.plot(gi.values, gi['lev'], color='k', linewidth=2)  # Example plot on top axis
ax4.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=22)
ax4.set_title('(d)  ', fontweight='bold', fontsize=18)

ax4.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax4.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax4.invert_yaxis()  # Invert y-axis
ax4.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax4.set_xticks(np.arange(0, 10.1, 1))  # Set ticks on the top x-axis
ax4.set_xlim([0, 9])  # Adjust top axis limits to match top axis data range
ax4.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax4.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
ax4.set_xlabel(r'Graupel Mixing ratio (g/kg)', fontweight='bold', fontsize=17)
ax4.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax5 = fig.add_subplot(gs[1, 1])  # First column
# ax5.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax5.plot(i_a.values, i_a['lev'], color='b', linewidth=2)  # Example plot on top axis
ax5.plot(i_c.values, i_c['lev'], color='r', linewidth=2)  # Example plot on top axis
ax5.plot(i_e.values, i_e['lev'], color='g', linewidth=2)  # Example plot on top axis
ax5.plot(i_g.values, i_g['lev'], color='y', linewidth=2)  # Example plot on top axis
ax5.plot(i_i.values, i_i['lev'], color='k', linewidth=2)  # Example plot on top axis
ax5.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax5.tick_params(axis='y', rotation=90)  # Rotate y-axis labels if needed
ax5.invert_yaxis()  # Invert y-axis
ax5.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax5.set_title('(e)  ', fontweight='bold', fontsize=18)

ax5.set_xticks(np.arange(0, 0.51, 0.1))  # Set ticks on the top x-axis
ax5.set_xlim([0, 0.5])  # Adjust top axis limits to match top axis data range
ax5.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax5.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
ax5.set_yticklabels([])
ax5.set_xlabel(r'Ice Mixing ratio (g/kg)', fontweight='bold', fontsize=17)
ax5.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax6 = fig.add_subplot(gs[1, 2])  # First column
# ax6.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
# ax6.plot(sa.values, sa['lev'], color='b', linewidth=2)  # Example plot on top axis
ax6.plot(sc.values, sc['lev'], color='r', linewidth=2)  # Example plot on top axis
ax6.plot(se.values, se['lev'], color='g', linewidth=2)  # Example plot on top axis
ax6.plot(sg.values, sg['lev'], color='y', linewidth=2)  # Example plot on top axis
ax6.plot(si.values, si['lev'], color='k', linewidth=2)  # Example plot on top axis
ax6.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax6.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax6.invert_yaxis()  # Invert y-axis
ax6.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax6.set_title('(f)  ', fontweight='bold', fontsize=18)
ax6.set_xticks(np.arange(0, 3.1, 0.5))  # Set ticks on the top x-axis
ax6.set_xlim([0, 3])  # Adjust top axis limits to match top axis data range
ax6.set_yticks(np.arange(200, 1000.1, 100))  # Set ticks on the top x-axis
ax6.set_ylim([1000, 200])  # Adjust top axis limits to match top axis data range
ax6.set_yticklabels([])
ax6.set_xlabel(r'Snow Mixing ratio (g/kg)', fontweight='bold', fontsize=17)
ax6.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax7 = fig.add_subplot(gs[2, 0])  # First column
# ax7.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax7.plot(da1.values, da1['lev'], color='b', linewidth=2)  # Example plot on top axis
ax7.plot(dc1.values, dc1['lev'], color='r', linewidth=2)  # Example plot on top axis
ax7.plot(de1.values, de1['lev'], color='g', linewidth=2)  # Example plot on top axis
ax7.plot(dg1.values, dg1['lev'], color='y', linewidth=2)  # Example plot on top axis
ax7.plot(di1.values, di1['lev'], color='k', linewidth=2)  # Example plot on top axis
ax7.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=22)
ax7.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax7.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax7.invert_yaxis()  # Invert y-axis
ax7.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax7.set_title('(g)  ', fontweight='bold', fontsize=18)
ax7.set_xticks(np.arange(00, 60.1, 5))  # Set ticks on the top x-axis
ax7.set_xlim([0, 65])  # Adjust top axis limits to match top axis data range
ax7.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax7.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
ax7.set_xlabel(r'reflectivity (dbz)', fontweight='bold', fontsize=17)
ax7.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)

###########setting customized legend position
fig.legend(loc='upper left', bbox_to_anchor=(0.44, 0.24), fontsize=24, ncol=3)


# plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.35, color='gray')
plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 24,
    'ytick.labelsize': 24,
    "axes.linewidth": 2,
    "patch.linewidth": 2,
    'xtick.major.size': 24,
    'ytick.major.size': 24,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 22,  # For axes titles
    'figure.titlesize': 24  # For overall figure title
})
plt.show()
##############################2020/03/03########2 nd figure
fig = plt.figure(figsize=(21, 19))
gs = gridspec.GridSpec(3, 3, width_ratios=[1, 1, 1], wspace=0.12, hspace=0.38)  # Adjusted to 3 columns
# mpl.rcParams['figure.facecolor'] = 'white'
# fig.patch.set_facecolor('lightblue')  # Set background color for the entire figure
ax1 = fig.add_subplot(gs[0, 0])  # First column
# ax1.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax1.plot(vb.values, vb['lev'], color='b', linewidth=2, label='Ferrier')  # Example plot on top axis
ax1.plot(vd.values, vd['lev'], color='r', linewidth=2, label='Milbrandt')  # Example plot on top axis
ax1.plot(vf.values, vf['lev'], color='g', linewidth=2, label='Thompson')  # Example plot on top axis
ax1.plot(vh.values, vh['lev'], color='y', linewidth=2, label='Morrison')  # Example plot on top axis
ax1.plot(vj.values, vj['lev'], color='k', linewidth=2, label='Wsm6')  # Example plot on top axis
ax1.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=22)
ax1.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax1.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax1.invert_yaxis()  # Invert y-axis
# ax1.legend(fontsize=10)
ax1.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax1.set_title('(a)  ', fontweight='bold', fontsize=18)
ax1.set_xticks(np.arange(0, 10.1, 2))  # Set ticks on the top x-axis
ax1.set_xlim([0, 10])  # Adjust top axis limits to match top axis data range
# ax1.set_xlim([])
ax1.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax1.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
ax1.set_xlabel(r'Vapor Mixing ratio (g/kg)', fontweight='bold', fontsize=17)
ax1.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax2 = fig.add_subplot(gs[0, 1])  # First column
# ax2.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax2.plot(rb.values, rb['lev'], color='b', linewidth=2)  # Example plot on top axis
ax2.plot(rd.values, rd['lev'], color='r', linewidth=2)  # Example plot on top axis
ax2.plot(rf.values, rf['lev'], color='g', linewidth=2)  # Example plot on top axis
ax2.plot(rh.values, rh['lev'], color='y', linewidth=2)  # Example plot on top axis
ax2.plot(rj.values, rj['lev'], color='k', linewidth=2)  # Example plot on top axis
ax2.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax2.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax2.invert_yaxis()  # Invert y-axis
ax2.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax2.set_title('(b)  ', fontweight='bold', fontsize=18)
ax2.set_xticks(np.arange(0, 3.8, 0.5))  # Set ticks on the top x-axis
ax2.set_xlim([0, 3.75])  # Adjust top axis limits to match top axis data range
ax2.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax2.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
ax2.set_yticklabels([])
ax2.set_xlabel(r'Rain Mixing ratio (g/kg)', fontweight='bold', fontsize=17)
ax2.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax3 = fig.add_subplot(gs[0, 2])  # First column
# ax3.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax3.plot(cb.values, cb['lev'], color='b', linewidth=2)  # Example plot on top axis
ax3.plot(cd.values, cd['lev'], color='r', linewidth=2)  # Example plot on top axis
ax3.plot(cf.values, cf['lev'], color='g', linewidth=2)  # Example plot on top axis
ax3.plot(ch.values, ch['lev'], color='y', linewidth=2)  # Example plot on top axis
ax3.plot(cj.values, cj['lev'], color='k', linewidth=2)  # Example plot on top axis
ax3.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax3.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax3.invert_yaxis()  # Invert y-axis
ax3.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax3.set_title('(c)  ', fontweight='bold', fontsize=18)
ax3.set_xticks(np.arange(0, 4.15, 0.5))  # Set ticks on the top x-axis
ax3.set_xlim([0, 4.5])  # Adjust top axis limits to match top axis data range
ax3.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax3.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
ax3.set_yticklabels([])
ax3.set_xlabel(r'Cloud Mixing ratio (g/kg)', fontweight='bold', fontsize=17)
ax3.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax4 = fig.add_subplot(gs[1, 0])  # First column
# ax4.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
# ax4.plot(ga.values, ga['lev'], color='b', linewidth=2)  # Example plot on top axis
ax4.plot(gd.values, gd['lev'], color='r', linewidth=2)  # Example plot on top axis
ax4.plot(gf.values, gf['lev'], color='g', linewidth=2)  # Example plot on top axis
ax4.plot(gh.values, gh['lev'], color='y', linewidth=2)  # Example plot on top axis
ax4.plot(gj.values, gj['lev'], color='k', linewidth=2)  # Example plot on top axis
ax4.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=22)
ax4.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax4.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax4.invert_yaxis()  # Invert y-axis
ax4.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax4.set_title('(d)  ', fontweight='bold', fontsize=18)
ax4.set_xticks(np.arange(0, 4.51, 0.5))  # Set ticks on the top x-axis
ax4.set_xlim([0, 4.5])  # Adjust top axis limits to match top axis data range
ax4.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax4.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
ax4.set_xlabel(r'Graupel Mixing ratio (g/kg)', fontweight='bold', fontsize=17)
ax4.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax5 = fig.add_subplot(gs[1, 1])  # First column
# ax5.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax5.plot(i_b.values, i_b['lev'], color='b', linewidth=2)  # Example plot on top axis
ax5.plot(i_d.values, i_d['lev'], color='r', linewidth=2)  # Example plot on top axis
ax5.plot(i_f.values, i_f['lev'], color='g', linewidth=2)  # Example plot on top axis
ax5.plot(i_h.values, i_h['lev'], color='y', linewidth=2)  # Example plot on top axis
ax5.plot(i_j.values, i_j['lev'], color='k', linewidth=2)  # Example plot on top axis
ax5.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax5.tick_params(axis='y', rotation=90)  # Rotate y-axis labels if needed
ax5.invert_yaxis()  # Invert y-axis
ax5.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax5.set_title('(e)  ', fontweight='bold', fontsize=18)
ax5.set_xticks(np.arange(0, 0.151, 0.025))  # Set ticks on the top x-axis
ax5.set_xlim([0, 0.15])  # Adjust top axis limits to match top axis data range
ax5.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax5.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
ax5.set_yticklabels([])
ax5.set_xlabel(r'Ice Mixing ratio (g/kg)', fontweight='bold', fontsize=17)
ax5.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax6 = fig.add_subplot(gs[1, 2])  # First column
# ax6.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
# ax6.plot(sa.values, sa['lev'], color='b', linewidth=2)  # Example plot on top axis
ax6.plot(sd.values, sd['lev'], color='r', linewidth=2)  # Example plot on top axis
ax6.plot(sf.values, sf['lev'], color='g', linewidth=2)  # Example plot on top axis
ax6.plot(sh.values, sh['lev'], color='y', linewidth=2)  # Example plot on top axis
ax6.plot(sj.values, sj['lev'], color='k', linewidth=2)  # Example plot on top axis
ax6.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax6.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax6.invert_yaxis()  # Invert y-axis
ax6.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax6.set_title('(f)  ', fontweight='bold', fontsize=18)
ax6.set_xticks(np.arange(0, 3.51, 0.5))  # Set ticks on the top x-axis
ax6.set_xlim([0, 3.5])  # Adjust top axis limits to match top axis data range
ax6.set_yticks(np.arange(200, 1000.1, 100))  # Set ticks on the top x-axis
ax6.set_ylim([1000, 200])  # Adjust top axis limits to match top axis data range
ax6.set_yticklabels([])
ax6.set_xlabel(r'Snow Mixing ratio (g/kg)', fontweight='bold', fontsize=17)
ax6.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax7 = fig.add_subplot(gs[2, 0])  # First column
# ax7.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax7.plot(db1.values, db1['lev'], color='b', linewidth=2)  # Example plot on top axis
ax7.plot(dd1.values, dd1['lev'], color='r', linewidth=2)  # Example plot on top axis
ax7.plot(df1.values, df1['lev'], color='g', linewidth=2)  # Example plot on top axis
ax7.plot(dh1.values, dh1['lev'], color='y', linewidth=2)  # Example plot on top axis
ax7.plot(dj1.values, dj1['lev'], color='k', linewidth=2)  # Example plot on top axis
ax7.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=22)
ax7.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax7.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax7.invert_yaxis()  # Invert y-axis
ax7.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax7.set_title('(g)  ', fontweight='bold', fontsize=18)
ax7.set_xticks(np.arange(0, 65.1, 5))  # Set ticks on the top x-axis
ax7.set_xlim([0, 60])  # Adjust top axis limits to match top axis data range
ax7.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax7.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
ax7.set_xlabel(r'reflectivity (dbz)', fontweight='bold', fontsize=17)
ax7.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)

###########setting customized legend position
fig.legend(loc='upper left', bbox_to_anchor=(0.44, 0.24), fontsize=24, ncol=3)



# plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.35, color='gray')
plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 24,
    'ytick.labelsize': 24,
    "axes.linewidth": 2,
    "patch.linewidth": 2,
    'xtick.major.size': 24,
    'ytick.major.size': 24,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 22,  # For axes titles
    'figure.titlesize': 24  # For overall figure title
})
plt.show()

# # da = da['qsnow']
# # db = db['qsnow']
# # dc = dc['qsnow']
# # dd = dd['qsnow']
# # de = de['qsnow']
# # df = df['qsnow']
# # dg = dg['qsnow']
# # dh = dh['qsnow']
# # di = di['qsnow']
# # dj = dj['qsnow']


# ####################################
# ######## this is for to find a max value position 
# data = ra
# from numpy import unravel_index
# unravel_index(data.argmax(), data.shape)