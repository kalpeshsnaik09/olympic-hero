# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)


# --------------
#Code starts here





data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')

data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both',data['Better_Event'])

better_event=data['Better_Event'].value_counts().index[0]
print(better_event,type(better_event))


# --------------
#Code starts here




top_countries=data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']].copy()
top_countries.drop(top_countries.tail(1).index,axis=0,inplace=True)

def top_ten(df,df_column_1,df_column_2):
    top=df.nlargest(10,df_column_1)
    country_list=list(top[df_column_2])
    return country_list

top_10_summer=top_ten(top_countries,'Total_Summer','Country_Name')
top_10_winter=top_ten(top_countries,'Total_Winter','Country_Name')
top_10=top_ten(top_countries,'Total_Medals','Country_Name')

common=list(set(top_10)&set(top_10_summer)&set(top_10_winter))
print(common)



# --------------
#Code starts here
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]

plt.bar(summer_df['Total_Summer'],summer_df['Country_Name'])

plt.bar(summer_df['Total_Winter'],summer_df['Country_Name'])

plt.bar(summer_df['Total_Medals'],summer_df['Country_Name'])
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=round(summer_df['Golden_Ratio'].max(),2)
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio']==summer_df['Golden_Ratio'].max(),'Country_Name'].iloc[0]

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=round(winter_df['Golden_Ratio'].max(),2)
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio']==winter_df['Golden_Ratio'].max(),'Country_Name'].iloc[0]

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=round(top_df['Golden_Ratio'].max(),2)
top_country_gold=top_df.loc[top_df['Golden_Ratio']==top_df['Golden_Ratio'].max(),'Country_Name'].iloc[0]


# --------------
#Code starts here
data_1=data.drop(data.tail(1).index,axis=0)
data_1['Total_Points']=(data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+data_1['Bronze_Total']
most_points=data_1['Total_Points'].max()
best_country=data_1.loc[data_1['Total_Points']==data_1['Total_Points'].max(),'Country_Name'].iloc[0]


# --------------
#Code starts here
best=data.loc[data['Country_Name']==best_country,['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United State')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


