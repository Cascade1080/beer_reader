import pandas as pd
pd.options.mode.chained_assignment = None #removes 'SettingWithCopyWarning' message


df = pd.read_csv('january taproom sales 2022.csv', usecols=['Item Name','Num Sold'], nrows = 104)

#Selects the range by row
df_pints = df.iloc[0:21,0:2]
df_mug = df.iloc[22:40,0:2]
df_PTR = df.iloc[41:49, 0:2]
df_thirtytwo = df.iloc[52:66, 0:2]
df_sixtyfour = df.iloc[68:80, 0:2]
df_halfs = df.iloc[81:105]

#applies a particular function to the selected row
df_pints["BBLS"] = df_pints["Num Sold"]*0.00403226
df_mug["BBLS"] = df_mug["Num Sold"]*0.00554435
df_PTR["BBLS"] = df_PTR["Num Sold"]*0.01612903
df_thirtytwo["BBLS"] = df_thirtytwo["Num Sold"]*0.00806452
df_sixtyfour["BBLS"] = df_sixtyfour["Num Sold"]*0.01612903
df_halfs["BBLS"] = df_halfs["Num Sold"]*0.00201613

#sums the bbls column
total = df_pints.sum(axis = 0, skipna = True) + df_mug.sum(axis = 0, skipna = True) + df_PTR.sum(axis = 0, skipna = True)
totaltwo = df_thirtytwo.sum(axis = 0, skipna = True) + df_sixtyfour.sum(axis = 0, skipna = True) + df_halfs.sum(axis = 0, skipna = True)

pints = df_pints.sum(axis = 0, skipna = True)

totals = {'Item': ['Pints'], 'Total BBLS':[pints]}
totals_df = pd.DataFrame(totals)

#--------------------PRINTS THE LIST OF THE ITEM
#print(df_pints)
#print(df_mug)
#print(df_PTR)
#print(df_thirtytwo)
#print(df_sixtyfour)
#print(df_halfs)

#--------------------PRINTS THE SUM OF THE ITEM
#print(df_pints.sum(axis = 0, skipna = True))
#print(df_mug.sum(axis = 0, skipna = True))
#print(df_PTR.sum(axis = 0, skipna = True))
#print(df_thirtytwo.sum(axis = 0, skipna = True))
#print(df_sixtyfour.sum(axis = 0, skipna = True))
#print(df_halfs.sum(axis = 0, skipna = True))
print(total + totaltwo)
#print(pints)
#print(totals_df)




print(df["Num Sold"].shape)
