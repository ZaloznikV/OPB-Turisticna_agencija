import pandas as pd
import random
df = pd.read_csv('\podatki/MOCK_DATA.csv')

sez = list(range(1,1001))
random.shuffle(sez) #nakljucno premesa seznam

n = df.columns[0]

# Drop that column
df.drop(n, axis = 1, inplace = False)

# Put whatever series you want in its place
df[n] = sez

df.to_csv (r'\podatki\izlet.csv', index = False, header=True)