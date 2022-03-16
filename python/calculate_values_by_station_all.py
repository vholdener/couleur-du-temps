# read csv from
# clean/format data for visualization input

cosmo_data = 'https://data.geo.admin.ch/ch.meteoschweiz.prognosen/punktprognosen/COSMO-E-all-stations.csv'
# stationen_data = '/home/vholdener/site01/data/meteoschweiz_stationen_20220228_utf8.csv'
stationen_data = 'C:/Users/Viktor/OneDrive/Dokumente/V/CAS_DataViz/couleur_du_temps_01/data/meteoschweiz_stationen_20220228_utf8.csv'

import pandas as pd
import numpy as np
import locale

# in franzoesisch (fuer Monatsnamen)
locale.setlocale(locale.LC_ALL, 'fr_FR')

columnnames = ['stn','time','leadtime','T_2M_0','T_2M_1','T_2M_2','T_2M_3','T_2M_4','T_2M_5','T_2M_6',	'T_2M_7',	'T_2M_8',	'T_2M_9',	'T_2M_10',	'T_2M_11',	'T_2M_12',	'T_2M_13',	'T_2M_14',	'T_2M_15',	'T_2M_16',	'T_2M_17',	'T_2M_18',	'T_2M_19',	'T_2M_20',	'FF_10M_0',	'FF_10M_1',	'FF_10M_2',	'FF_10M_3',	'FF_10M_4',	'FF_10M_5',	'FF_10M_6',	'FF_10M_7',	'FF_10M_8',	'FF_10M_9',	'FF_10M_10',	'FF_10M_11',	'FF_10M_12',	'FF_10M_13',	'FF_10M_14',	'FF_10M_15',	'FF_10M_16',	'FF_10M_17',	'FF_10M_18',	'FF_10M_19',	'FF_10M_20',	'DD_10M_0',	'DD_10M_1',	'DD_10M_2',	'DD_10M_3',	'DD_10M_4',	'DD_10M_5',	'DD_10M_6',	'DD_10M_7',	'DD_10M_8',	'DD_10M_9',	'DD_10M_10',	'DD_10M_11',	'DD_10M_12',	'DD_10M_13',	'DD_10M_14',	'DD_10M_15',	'DD_10M_16',	'DD_10M_17',	'DD_10M_18',	'DD_10M_19',	'DD_10M_20',	'TOT_PREC_0',	'TOT_PREC_1',	'TOT_PREC_2',	'TOT_PREC_3',	'TOT_PREC_4',	'TOT_PREC_5',	'TOT_PREC_6',	'TOT_PREC_7',	'TOT_PREC_8',	'TOT_PREC_9',	'TOT_PREC_10',	'TOT_PREC_11',	'TOT_PREC_12',	'TOT_PREC_13',	'TOT_PREC_14',	'TOT_PREC_15',	'TOT_PREC_16',	'TOT_PREC_17',	'TOT_PREC_18',	'TOT_PREC_19',	'TOT_PREC_20',	'RELHUM_2M_0',	'RELHUM_2M_1',	'RELHUM_2M_2',	'RELHUM_2M_3',	'RELHUM_2M_4',	'RELHUM_2M_5',	'RELHUM_2M_6',	'RELHUM_2M_7',	'RELHUM_2M_8',	'RELHUM_2M_9',	'RELHUM_2M_10',	'RELHUM_2M_11',	'RELHUM_2M_12',	'RELHUM_2M_13',	'RELHUM_2M_14',	'RELHUM_2M_15',	'RELHUM_2M_16',	'RELHUM_2M_17',	'RELHUM_2M_18','RELHUM_2M_19','RELHUM_2M_20','DURSUN_0','DURSUN_1','DURSUN_2','DURSUN_3','DURSUN_4','DURSUN_5','DURSUN_6','DURSUN_7','DURSUN_8','DURSUN_9','DURSUN_10','DURSUN_11','DURSUN_12','DURSUN_13','DURSUN_14','DURSUN_15','DURSUN_16','DURSUN_17','DURSUN_18','DURSUN_19','DURSUN_20','a']
columnrelevant = ['stn','time','leadtime','T_2M_0',	'T_2M_1',	'T_2M_2',	'T_2M_3',	'T_2M_4',	'T_2M_5',	'T_2M_6',	'T_2M_7',	'T_2M_8',	'T_2M_9',	'T_2M_10',	'T_2M_11',	'T_2M_12',	'T_2M_13',	'T_2M_14',	'T_2M_15',	'T_2M_16',	'T_2M_17',	'T_2M_18',	'T_2M_19',	'T_2M_20', 'TOT_PREC_0',	'TOT_PREC_1',	'TOT_PREC_2',	'TOT_PREC_3',	'TOT_PREC_4',	'TOT_PREC_5',	'TOT_PREC_6',	'TOT_PREC_7',	'TOT_PREC_8',	'TOT_PREC_9',	'TOT_PREC_10',	'TOT_PREC_11',	'TOT_PREC_12',	'TOT_PREC_13',	'TOT_PREC_14',	'TOT_PREC_15',	'TOT_PREC_16',	'TOT_PREC_17',	'TOT_PREC_18',	'TOT_PREC_19',	'TOT_PREC_20','DURSUN_0',	'DURSUN_1',	'DURSUN_2',	'DURSUN_3',	'DURSUN_4',	'DURSUN_5',	'DURSUN_6',	'DURSUN_7',	'DURSUN_8',	'DURSUN_9',	'DURSUN_10',	'DURSUN_11',	'DURSUN_12',	'DURSUN_13',	'DURSUN_14',	'DURSUN_15',	'DURSUN_16',	'DURSUN_17',	'DURSUN_18',	'DURSUN_19',	'DURSUN_20']

# csv einlesen
df = pd.read_csv(cosmo_data, sep=';', skiprows=27, names=columnnames, header=0, usecols=columnrelevant, parse_dates=['time'])

# # df fuer stationen
df_stationen = pd.read_csv(stationen_data, sep=';', encoding = 'utf-8')

# relevante Prognosen (zeitlich)
now = pd.Timestamp.now()
td = pd.Timedelta(21600,'seconds') # 6h
nachher = now + td
vorher = now - td

# maske fuer aktuellste und vorherige Prognose
mask = (df['time'] > vorher) & (df['time'] <= nachher)
df = df.loc[mask]

# Durchschnitte berechnen
ColumnListTemp = ['T_2M_0','T_2M_1','T_2M_2','T_2M_3','T_2M_4','T_2M_5','T_2M_6',	'T_2M_7',	'T_2M_8',	'T_2M_9',	'T_2M_10',	'T_2M_11',	'T_2M_12',	'T_2M_13',	'T_2M_14',	'T_2M_15',	'T_2M_16',	'T_2M_17',	'T_2M_18',	'T_2M_19',	'T_2M_20']
ColumnListSun = ['DURSUN_1',	'DURSUN_2',	'DURSUN_3',	'DURSUN_4',	'DURSUN_5',	'DURSUN_6',	'DURSUN_7',	'DURSUN_8',	'DURSUN_9',	'DURSUN_10',	'DURSUN_11',	'DURSUN_12',	'DURSUN_13',	'DURSUN_14',	'DURSUN_15',	'DURSUN_16',	'DURSUN_17',	'DURSUN_18',	'DURSUN_19',	'DURSUN_20']
ColumnListNs = ['TOT_PREC_0',	'TOT_PREC_1',	'TOT_PREC_2',	'TOT_PREC_3',	'TOT_PREC_4',	'TOT_PREC_5',	'TOT_PREC_6',	'TOT_PREC_7',	'TOT_PREC_8',	'TOT_PREC_9',	'TOT_PREC_10',	'TOT_PREC_11',	'TOT_PREC_12',	'TOT_PREC_13',	'TOT_PREC_14',	'TOT_PREC_15',	'TOT_PREC_16',	'TOT_PREC_17',	'TOT_PREC_18',	'TOT_PREC_19',	'TOT_PREC_20']

df['temperatur']=df.loc[:,ColumnListTemp].mean(axis=1)
df['sonne']=df.loc[:,ColumnListSun].mean(axis=1)
df['niederschlag']=df.loc[:,ColumnListNs].mean(axis=1)

# df verkleinern auf relevante Spalten
df = df[['stn','time','temperatur','sonne','niederschlag']]

# Temperaturdifferenz
df['tempdiff'] = df.groupby('stn')['temperatur'].diff()

# maske fuer aktuellste Prognose
masknow = (df['time'] > now) & (df['time'] <= nachher)
df = df.loc[masknow]

df['datum'] = df['time'].dt.strftime('%#d %B %Y')

# Titel der Zeitperiode anhaengen
df['stunde'] = df['time'].dt.strftime('%H')
#stunde = ''
stunde = df['stunde'].values[0]
#stunde = df.at[0,'stunde']
zeitperiode = ''
if stunde == '12':
    zeitperiode = "l'après-midi"
elif stunde == '18':
    zeitperiode = 'la soirée'
elif stunde == '00':
    zeitperiode = 'la nuit'
elif stunde == '06':
    zeitperiode = 'la mattinée'
df['zeitperiode'] = zeitperiode

# Namen der Stationen anhaengen
result = pd.merge(df, df_stationen, on='stn', how='left')
result = result.sort_values(by=['namestn'])

# Write DataFrame to CSV
# result.to_csv('/home/vholdener/site01/data/Prognose_all.csv', index=False)
result.to_csv('C:/Users/Viktor/OneDrive/Dokumente/V/CAS_DataViz/couleur_du_temps_02/data/Prognose_all.csv', index=False)

