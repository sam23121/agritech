import pandas as pd


# df = pd.read_csv('data/metadata.csv', index_col='filename')
# print(df.iloc[0])
headers = [*pd.read_csv('data/metadata.csv', nrows=1)]
df = pd.read_csv('data/metadata.csv', usecols=[c for c in headers if c != 'Unnamed: 0'], index_col='filename')
print(df.iloc[0])
# filename, xmin, ymin,xmax, ymax, points = df.loc[df['filename'] == 'AK_DeltaJunction_1_2021/']

# file= df.iloc['AK_DeltaJunction_1_2021/']['filename']
file = df.loc['AK_DeltaJunction_1_2021/', 'xmax'] 
print(file)