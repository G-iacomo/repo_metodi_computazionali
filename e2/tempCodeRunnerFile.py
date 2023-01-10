df = pd.DataFrame(columns=['Date Local','NO2 Mean','NO2 AQI','NO2 1st Max Value','O3 Mean','O3 AQI','O3 1st Max Value','SO2 Mean','SO2 AQI','SO2 1st Max Value','CO Mean','CO AQI','CO 1st Max Value'])
# for i in range(j):
#     a = stazione4.loc[i,'Date Local']
#     b = stazione4.loc[i+1,'Date Local']
#     delta = (dt.datetime.strptime(b, '%Y-%m-%d').date()) - (dt.datetime.strptime(a, '%Y-%m-%d').date())
#     if delta.days!=1:
#         df.iloc[i+1,0] = a+dt.timedelta(days=1)