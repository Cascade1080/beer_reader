import pandas as pd

df = pd.read_csv('january taproom sales 2022.csv', usecols=['Item Name','Num Sold'], nrows = 104)

#Selects the range by row
df_pints = df.iloc[0:22,0:2]
df_mug = df.iloc[23:41,0:2]
df_PTR = df.iloc[42:50, 0:2]
df_thirtytwo = df.iloc[52:67, 0:2]
df_sixtyfour = df.iloc[68:81, 0:2]
df_halfs = df.iloc[82:105]

#applies a particular function to the selected row
df_pints["bbls"] = df_pints["Num Sold"]*0.00403226.round(df_pints["bbls"],2)
df_mug["bbls"] = df_mug["Num Sold"]*0.00554435
df_PTR["bbls"] = df_PTR["Num Sold"]*0.01612903
df_thirtytwo["bbls"] = df_thirtytwo["Num Sold"]*0.00806452
df_sixtyfour["bbls"] = df_sixtyfour["Num Sold"]*0.01612903
df_halfs["bbls"] = df_halfs["Num Sold"]*0.00201613

#prints the data
print(df_pints)
print(df_mug)
print(df_PTR)
print(df_thirtytwo)
print(df_sixtyfour)
print(df_halfs)
#df["BBLs"] = df["Num Sold"]*0.00403226 #selects and creates a new column with the wanted math expression

#splits = [df.loc[[i]] for i in df.index] #splits dataframe by row



###### selects specfic set of rows
#print(df.iloc[0:21])
#print(df.iloc[23:40])
#print(df.iloc[42:49])

#to_bbls = df[['Num Sold']] - selects the specific column

#print(df)
#print(to_bbls)
print(df["Num Sold"].shape)
