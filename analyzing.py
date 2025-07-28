import pandas as pd

# Load the cleaned dataset with coordinates
df = pd.read_excel(r"la_liga.xlsx" )
pd.set_option('display.max_rows',None)

# Analysis 1: Top 5 clubs by total matches played
group_club_and_match = df.groupby('Club')['Matches_Played'].sum().reset_index().sort_values(by='Matches_Played',ascending=False).head(5)

# Analysis 2: Top 10 players by matches played (with their clubs)
most_player_played_match = df.groupby(['Player','Club'])['Matches_Played'].sum().reset_index().sort_values(by='Matches_Played',ascending=False).head(10)

# Analysis 3: Top 5 cities by total player market value
most_city_value = df.groupby('City')['Value'].sum().reset_index().sort_values(by='Value',ascending=False).head(5).reset_index(drop=True)
most_city_value.index = range(1,len(most_city_value)+1)

# Analysis 4: Top 5 clubs by total goals and assists
most_clubs_have_G_A = df.groupby('Club')['G+A'].sum().reset_index().sort_values(by='G+A',ascending=False).reset_index(drop=True).head(5)
most_clubs_have_G_A.index = range(1,len(most_clubs_have_G_A)+1)

# Analysis 5: Top states/regions by total player market value
most_players_value_by_state  = df.groupby('State')['Value'].sum().reset_index().sort_values(by='Value',ascending=False).reset_index(drop=True)
most_players_value_by_state.index = range(1,len(most_players_value_by_state)+1)

# Analysis 6: Number of players for each club
number_of_palyers_by_club = df.groupby(['Club'])['Player'].count().reset_index(name='PlayerCount').sort_values(by='PlayerCount',ascending=False)
number_of_palyers_by_club.index = range(1,len(number_of_palyers_by_club)+1)

# Analysis 7: Total market value for each club
value_club = df.groupby('Club')['Value'].sum().reset_index(name='TotalMarket')

# Analysis 8: Relationship between number of players and total market value per club
relation_value_number_of_players =pd.merge(
    number_of_palyers_by_club.reset_index(drop=True),
    value_club,
    on='Club'
).sort_values(by='PlayerCount',ascending=False)
relation_value_number_of_players.index = range(1,len(relation_value_number_of_players)+1)

# Display dataset information
print(df.info())

# Clean nationality data by extracting 3-letter country codes
df['Nation'] = df['Nation'].str.extract(r'(\b[A-Z]{3}\b)', expand=False)

# Analysis 9: Separate Spanish and non-Spanish players
ESP_players = df.loc[df['Nation'].str.contains('ESP',case=False,na=False)]
other_players =df.loc[~df['Nation'].str.contains('ESP',case=False,na=False)]

# Analysis 10: Market value analysis by nationality
value_of_esp_players = df.groupby(ESP_players['Nation'])['Value'].sum().reset_index()
value_of_other_players = df.groupby(other_players['Nation'])['Value'].sum().reset_index().sort_values(by='Value',ascending=False)
value_of_other_players.index = range(1,len(value_of_other_players)+1)

# Analysis 11: Compare Spanish vs Other players market value
df['NationGroup'] = df['Nation'].apply(lambda x : 'ESP' if x == 'ESP'else 'Other')
compare_nation_players = df.groupby('NationGroup')['Value'].sum().reset_index()
print(compare_nation_players)

# Analysis 12: Barcelona players analysis
barca_players = df.loc[df['Club'].str.contains('Barcelona')]
print(barca_players)

# Analysis 13: Key metrics for Barcelona players
compare_barca_players = barca_players[['Player','Age','Goals','Assist','Min','Value']]
print(compare_barca_players)




