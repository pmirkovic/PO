import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#3
# učitavanje u dataframe format
df = pd.read_csv('ShenyangPM20100101_20151231.csv')
# Prikaz prvih 5 uzoraka
print(df.head())



#4
#Koliko ima uzoraka
print(df.shape)
#Koliko ima obelezja
print(df.dtypes)
#Nedostajuci podaci
print(df.isnull().sum() / df.shape[0] * 100)



#5
df.drop(['PM_Taiyuanjie', 'PM_Xiaoheyan'], axis=1, inplace=True)
print(df.isnull().sum() / df.shape[0] * 100)



#6
df['DEWP'].fillna(df['DEWP'].median(), inplace=True)
df['HUMI'].fillna(df['HUMI'].median(), inplace=True)
df['PRES'].fillna(df['PRES'].median(), inplace=True)
df['TEMP'].fillna(df['TEMP'].median(), inplace=True)
df['cbwd'].fillna(method='ffill', inplace=True)
df['Iws'].fillna(df['Iws'].median(), inplace=True)

df.dropna(axis=0, inplace=True)

print(df.isnull().sum() / df.shape[0] * 100)
print(df)



#7
print(df.describe())
print(df['cbwd'].describe())



#8
# Prikaz prvih nekoliko redova dataframea
print(df['PM_US Post'].head())
# Prikaz osnovnih statistika za numeričke kolone
print(df['PM_US Post'].describe())
# Prikaz broja pojavljivanja svake vrednosti u koloni "PM_US Post"
print(df["PM_US Post"].value_counts())

#Zavisnost PM prema godini
plt.scatter(df['year'], df['PM_US Post'])
plt.xlabel("Year")
plt.ylabel("Koncentracija PM2.5 čestica na nekoliko lokacija \n (µg/m3)")
plt.show()

#Zavisnost PM prema danima
plt.scatter(df['day'], df['PM_US Post'])
plt.xlabel("Dan")
plt.ylabel("Koncentracija PM2.5 čestica na nekoliko lokacija \n (µg/m3)")
plt.show()

#Zavisnost PM prema sat
plt.scatter(df['hour'], df['PM_US Post'])
plt.xlabel("Hour")
plt.ylabel("Koncentracija PM2.5 čestica na nekoliko lokacija \n (µg/m3)")
plt.show()

#Zavisnost PM prema danima
plt.scatter(df['season'], df['PM_US Post'])
plt.xlabel("Season")
plt.ylabel("Koncentracija PM2.5 čestica na nekoliko lokacija \n (µg/m3)")
plt.show()



#9
#Zavisnost PM prema DEWP
plt.scatter(df['DEWP'], df['PM_US Post'])
plt.xlabel("DEWP")
plt.ylabel("Koncentracija PM2.5 čestica na nekoliko lokacija \n (µg/m3)")
plt.show()

#Zavisnost PM prema TEMP
plt.scatter(df['TEMP'], df['PM_US Post'])
plt.xlabel("TEMP")
plt.ylabel("Koncentracija PM2.5 čestica na nekoliko lokacija \n (µg/m3)")
plt.show()

#Zavisnost PM prema HUMI
plt.scatter(df['HUMI'], df['PM_US Post'])
plt.xlabel("HUMI")
plt.ylabel("Koncentracija PM2.5 čestica na nekoliko lokacija \n (µg/m3)")
plt.show()

#Zavisnost PM prema PRES
plt.scatter(df['PRES'], df['PM_US Post'])
plt.xlabel("PRES")
plt.ylabel("Koncentracija PM2.5 čestica na nekoliko lokacija \n (µg/m3)")
plt.show()

#Zavisnost PM prema cbwd
plt.scatter(df['cbwd'], df['PM_US Post'])
plt.xlabel("cbwd")
plt.ylabel("Koncentracija PM2.5 čestica na nekoliko lokacija \n (µg/m3)")
plt.show()

#Zavisnost PM prema Iws
plt.scatter(df['Iws'], df['PM_US Post'])
plt.xlabel("Iws")
plt.ylabel("Koncentracija PM2.5 čestica na nekoliko lokacija \n (µg/m3)")
plt.show()

#Zavisnost PM prema precipitation
plt.scatter(df['precipitation'], df['PM_US Post'])
plt.xlabel("precipitation")
plt.ylabel("Koncentracija PM2.5 čestica na nekoliko lokacija \n (µg/m3)")
plt.show()

#Zavisnost PM prema Iprec
plt.scatter(df['Iprec'], df['PM_US Post'])
plt.xlabel("Iprec")
plt.ylabel("Koncentracija PM2.5 čestica na nekoliko lokacija \n (µg/m3)")
plt.show()



#10
corr_mat = df.corr()
sb.heatmap(corr_mat, annot=True)
plt.show()



#11
#Zavisnost prosecne PM po godini
prosek_po_godini = df.groupby("year")["PM_US Post"].mean()
print(prosek_po_godini)
df_god = df['year'].unique()
print(df_god)
plt.plot(df_god,prosek_po_godini)
plt.scatter(df_god,prosek_po_godini)
plt.xlabel("Godina")
plt.ylabel("Prosecna koncentracija PM2.5 čestica na nekoliko lokacija \n (µg/m3)")
plt.show()

#


######################



#1
