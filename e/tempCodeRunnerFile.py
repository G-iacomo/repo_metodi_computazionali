for i in tqdm(range(0,len(dati)-4+1,4)):
# #for i in tqdm(range(262,265,4)):
#     if (((dati.at[i+1,'SO2 Mean']>=0) and (dati.at[i+1,'CO Mean']>=0) )and (dati.at[i+1,'CO Mean']>=0)):
#         dati.at[i+1,'SO2 Mean'] = st.fmean([dati.at[i+1,'SO2 1st Max Value'],dati.at[i+2,'SO2 1st Max Value']])
#         dati.at[i+1,'SO2 1st Max Value'] = max(dati.at[i+1,'SO2 1st Max Value'],dati.at[i+2,'SO2 1st Max Value'])
#         dati.at[i+1,'CO Mean'] = st.fmean([dati.at[i+1,'SO2 1st Max Value'],dati.at[i+2,'SO2 1st Max Value']])
#         dati.at[i+1,'CO 1st Max Value'] = max(dati.at[i+1,'CO 1st Max Value'],dati.at[i+2,'CO 1st Max Value'])
#     else:
#         dati.drop([i+1],axis=0,inplace=True)
#     dati.drop([i],axis=0,inplace=True)
#     dati.drop([i+2],axis=0,inplace=True)
#     dati.drop([i+3],axis=0,inplace=True)