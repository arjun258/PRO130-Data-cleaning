import pandas as pd
df = pd.read_csv('./finalMergedData.csv')

print(df.shape)
del df['Unitsname']
del df['UnitsDistance']
del df['UnitsMass']
del df['UnitsRadius']

df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.drop(['Unnamed: 5'],axis=1,inplace=True)

df.to_csv('newUpdated.csv')