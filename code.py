# --------------
import pandas as pd 
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
# Load the dataset and create column `year` which stores the year in which match was played
data=pd.read_csv(path)
data['year']=data['date'].str[0:4]

# Plot the wins gained by teams across all seasons
df1=data.groupby(['winner'])['match_code'].nunique().sort_values(ascending=False)
plt.figure(figsize=(15,7))
df1.plot(kind='bar', title='Number of Wins')
plt.xlabel('Teams')
plt.ylabel('Number of matches won')

# Plot Number of matches played by each team through all seasons
df2=data.groupby(['team1'])['match_code'].nunique()
df3=data.groupby(['team2'])['match_code'].nunique()
df4=(df3+df2).sort_values(ascending=True)
plt.figure(figsize=(20,10))
df4.plot(kind='bar', title='Total Number of Matches Played')
plt.xlabel('Teams')
plt.ylabel('Number of Matches')

# Top bowlers through all seasons
data['wicket_kind'].unique()
data1=data.loc[(data.wicket_kind.isin(['bowled','caught','lbw','stumped','caught and bowled','hit wicket'])),:]
data1['wicket_kind'].unique()
df5 = data1.groupby(['bowler'])['player_out'].count().sort_values(ascending=False).head(10)
plt.figure(figsize=(20,10))
df5.plot(kind='bar', title='Top Bowlers')


# How did the different pitches behave? What was the average score for each stadium?
df6=data.groupby(['venue']).agg({'runs':'sum'}).sort_values(by='runs',ascending=False)
plt.figure(figsize=(20,10))
df6.plot(kind='bar', title='Average Score for Pitches')

# Types of Dismissal and how often they occur
df7=data['wicket_kind'].value_counts()
plt.figure(figsize=(20,10))
df7.plot(kind='bar', title='Type pf Dismissal')

# Plot no. of boundaries across IPL seasons
boundaries = ['4','6']
b1 = data.loc[data.runs.isin(boundaries)]
tb = b1['runs'].value_counts()
plt.figure(figsize=(20,10))
tb.plot(kind='bar')

# Average statistics across all seasons
NMP = data.groupby('year')['match_code'].nunique()
print('The number of matches played per season are',NMP)
RSPM =data.groupby('match_code').agg({'total':'sum'})
print('The average runs scored per match are', RSPM)
ABPM=data.groupby(['match_code','year']).agg({'delivery':'count'})
print('The average balls bowled per match per season are', ABPM)




