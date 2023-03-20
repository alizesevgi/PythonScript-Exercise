import sys
import pandas as pd
#Take min-date max-date top if exist if not set default
if("--min-date" in sys.argv):
    mindate = sys.argv[sys.argv.index('--min-date')+1]
else:
    mindate = "2020-01-01"
if("--max-date" in sys.argv):
    maxdate = sys.argv[sys.argv.index('--max-date')+1]
else:
    maxdate = "2020-06-30"
if("--top" in sys.argv):
    toprows = sys.argv[sys.argv.index('--top')+1]
else:
    toprows = "3"
#read all 3
df_pd = pd.read_csv('product.csv')

df_sl = pd.read_csv('sales.csv')

df_st = pd.read_csv('store.csv')
#merge product.csv with sales.csv using product id
pd_sl = df_pd.merge(df_sl, left_on="id", right_on = "product")
#merge new df with store.csv on store id
pd_sl_st= pd_sl.merge(df_st, left_on = "store", right_on = "id")
#make sure date column is type datetime
pd_sl_st['date'] = pd.to_datetime(pd_sl_st['date']) 
#create bool mask greater than mindate smaller than maxdate
mask = (pd_sl_st['date'] >= mindate) & (pd_sl_st['date'] <= maxdate)
#select sub-df and reassign
final = pd_sl_st.loc[mask]

#drop redundant columns 
final = final.drop(['id_x','id_y','product'], axis=1)
#top seller product
#create new df of name_x by summing all quantity of that name_x
pd_final = (final.groupby('name_x')['quantity'].sum().reset_index())
pd_final = pd_final.rename(columns = {'name_x':'name'}) #rename
pd_final = pd_final.nlargest(int(toprows), 'quantity',keep = 'all')#get toprows number of rows and keep all duplicates
print("-- top seller product --")
print(pd_final.to_string(index=False))
print("-- top seller store --") #repeat for name_y which is store name
st_final = (final.groupby('name_y')['quantity'].sum().reset_index())
st_final = st_final.rename(columns = {'name_y':'name'})
st_final = st_final.nlargest(int(toprows), 'quantity',keep = 'all')
print(st_final.to_string(index=False))
br_final = (final.groupby('brand')['quantity'].sum().reset_index())#repeat for brand
br_final = br_final.nlargest(int(toprows), 'quantity',keep = 'all')
print("-- top seller brand --")
print(br_final.to_string(index=False))
ct_final = (final.groupby('city')['quantity'].sum().reset_index())#repeat for city
ct_final = ct_final.nlargest(int(toprows), 'quantity',keep = 'all')
print("-- top seller city --")
print(ct_final.to_string(index=False))
