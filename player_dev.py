import pandas as pd

#read skater data into pandas dataframe
df = pd.read_csv('skater_stats.csv', encoding = 'unicode_escape')

#convert Goals to numeric
df['G'] = pd.to_numercic(df['G'], errors='coerce')

#we want to see when players switched teams
#lets sort by player and season so we can determine 
#  when they'd switched
df.sort_values(['Player', 'Season'], inplace=True)
df["ChangedTeams"] = (df['Tm'] != df.shift(1)['Tm']) & (df['Player'] == df.shift(1)['Player'])