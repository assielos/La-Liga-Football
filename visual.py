import pandas as pd 
import plotly.express as px
import plotly.io as pio

# Load the dataset for visualization
df = pd.read_excel(r"la_liga.xlsx" )

# Visualization 1: Interactive map showing club market values across Spain
# Aggregate data by club to get total market value and stadium coordinates
df_club_value = df.groupby('Club').agg({
    'Value': 'sum',
    'Stadium_Latitude': 'first',
    'Stadium_Longitude': 'first',
    'City': 'first',
    'Stadium':'first'
}).reset_index()

# Convert market value to millions of euros for better readability
df_club_value['Value (M €)'] = (df_club_value['Value'] / 1_000_000).round(2)

# Create interactive scatter map showing clubs by location and market value
fig = px.scatter_mapbox(
    df_club_value,
    lat='Stadium_Latitude',
    lon='Stadium_Longitude',
    size='Value',
    color='Club',
    hover_name='Club',
    hover_data={
        'City': True,
        'Stadium': True,
        'Stadium_Latitude': False,
        'Stadium_Longitude': False,
        'Value (M €)':True,
        'Value':False
    },
    mapbox_style='open-street-map',
    zoom=5,
    title='La liga value for each club'
)
fig.update_layout(title_x=0.5)
pio.renderers.default = 'browser'
fig.show()

# Visualization 2: Pie chart comparing Spanish vs Other players market value
# Create nationality grouping for comparison
df['NationGroup'] = df['Nation'].apply(lambda x : 'ESP' if x == 'ESP'else 'Other')
compare_nation_players = df.groupby('NationGroup')['Value'].sum().reset_index()

# Create pie chart showing market value distribution by nationality
compare_nation_players_fig = px.pie(compare_nation_players,names='NationGroup',values='Value')
compare_nation_players_fig.show()

# Visualization 3: Bar chart of top 5 nations by total player market value
# Get top 5 nations by total market value
top5_nation_players_value = df.groupby('Nation')['Value'].sum().reset_index().sort_values(by='Value',ascending=False).head(5)
top5_nation_value_fig = px.bar(top5_nation_players_value,x='Nation',y='Value',color='Value')
top5_nation_value_fig.show()

# Visualization 4: Scatter plot of Barcelona players by age and market value
# Filter Barcelona players
barca_players = df.loc[df['Club'].str.contains('Barcelona')]
compare_barca_players = barca_players[['Player','Age','Goals','Assist','Min','Value']]

# Create scatter plot showing relationship between age and market value for Barcelona players
compare_barca_players_fig = px.scatter(compare_barca_players,x='Age',y='Value',color='Player')
compare_barca_players_fig.show()
