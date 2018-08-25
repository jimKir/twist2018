import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ssl
import fiona
import geopandas

single_familiy_home_transactions = pd.read_csv("total_dataset_efh_en.csv") #
apartment_transactions = pd.read_csv("total_dataset_STW_en.csv")
total_house_stock= pd.read_csv("total_dataset_GWR.csv")

# print(single_familiy_home_transactions.head())
# print(apartment_transactions.head())
# print(total_house_stock.head())

# merged = single_familiy_home_transactions.merge(apartment_transactions, how='inner', left_on='GRID_ID', right_on='GRID_ID')

# print(merged.head())

shape = fiona.open('Hexbins.shp')
#
# # pd.merge(left, right, left_on=key_or_keys, right_index=True,
# #       how='left', sort=False)
#

print(shape.schema)
print(shape.next)

gp =  geopandas.read_file('Hexbins.shp')


merged = single_familiy_home_transactions.merge(gp, how='inner', left_on='GRID_ID', right_on='GRID_ID')
print(merged.head())
# #first feature of the shapefile
# first = shape.next()

