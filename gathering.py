import pandas as pd
from opencage.geocoder import OpenCageGeocode
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import requests 

# Load the dataset from Excel file
df = pd.read_excel("la_liga.xlsx")
players = df['Player']
headers = {'User-Agent': 'Mozilla/5.0'}

def get_tm_profile_url(player_name):
    """
    Search for a player's profile URL on Transfermarkt website
    Args:
        player_name (str): Name of the player to search for
    Returns:
        str: Player's profile URL or None if not found
    """
    search_url = "https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche"
    response = requests.get(search_url, params={'query': player_name}, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    link = soup.select_one("a.spielprofil_tooltip")
    if link:
        return "https://www.transfermarkt.com" + link['href']
    return None

def get_market_value(url):
    """
    Extract market value from a player's Transfermarkt profile
    Args:
        url (str): Player's profile URL
    Returns:
        float: Market value in millions of euros or None if error
    """
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        value_div = soup.select_one('.dataMarktwert')
        if value_div:
            raw = value_div.get_text(strip=True).replace('€', '').replace('m', '').replace('Th.', 'k').replace(',', '.')
            if 'k' in raw:
                return float(raw.replace('k', '')) / 1000  # convert k to millions
            return float(raw)
    except Exception as e:
        print(f"Error at {url}: {e}")
        return None

# Fetch market values for all players
values = []
for player in players:
    print(f"Fetching: {player}")
    url = get_tm_profile_url(player)
    if url:
        value = get_market_value(url)
        values.append(value)
    else:
        values.append(None)
    time.sleep(1.5)  # polite delay to avoid overwhelming the server

# Define Spanish regions/states for mapping
state = [
    'Catalunya',
    'Comunidad de Madrid',
    'Andalucía',
    'País Vasco',
    'Comunidad Valenciana',
    'Galicia',
    'Navarra',
    'Islas Baleares',
    'Canarias'
]

# Define Spanish cities for mapping
city=[
    'Barcelona',
    'Madrid',
    'Sevilla',
    'San Sebastián',
    'Bilbao',
    'Valencia',
    'Villarreal',
    'Getafe',
    'Girona',
    'Vigo',
    'Vitoria-Gasteiz',
    'Pamplona',
    'Granada',
    'Cádiz',
    'Almería',
    'Palma de Mallorca',
    'Las Palmas'
]

# Create mapping dictionary for cities to states
my_dict = {}
for city_names in city:
    if city_names in ['Barcelona','Girona']:
        my_dict[city_names] = 'Catalunya'
    elif city_names in ['Madrid','Getafe']:
        my_dict[city_names] = 'Comunidad de Madrid'
    elif city_names in ['San Sebastiá','Bilbao','Vitoria-Gasteiz']:
        my_dict[city_names] = 'País Vasco' 
    elif city_names in ['Valencia','Villarreal']:
        my_dict[city_names] = 'Comunidad Valenciana'
    elif city_names == 'Vigo':
        my_dict[city_names] = 'Galicia'
    elif city_names == 'Pamplona':
        my_dict[city_names] = 'Navarra'
    elif city_names == 'Palma de Mallorca':
        my_dict[city_names] = 'Islas Baleares'
    elif city_names == 'Las Palmas':
        my_dict[city_names] = 'Canarias'
    else:
        my_dict[city_names] = 'Andalucía'

# Add City and State columns to the dataframe
df['City'] = ''
df['State'] = ''

# Map clubs to their respective cities and states
for s, c in df['Club'].items():
    if c in ['Barcelona', 'Espanyol']:
        df.at[s, 'State'] = 'Catalunya'
        df.at[s, 'City'] = 'Barcelona'
    elif c == 'Girona':
        df.at[s, 'State'] = 'Catalunya'
        df.at[s, 'City'] = 'Girona'
    elif c in ['Real Madrid', 'Atlético Madrid', 'Madrid']:
        df.at[s, 'State'] = 'Comunidad de Madrid'
        df.at[s, 'City'] = 'Madrid'
    elif c == 'Getafe':
        df.at[s, 'State'] = 'Comunidad de Madrid'
        df.at[s, 'City'] = 'Getafe'
    elif c == 'Athletic Club':
        df.at[s, 'State'] = 'País Vasco'
        df.at[s, 'City'] = 'Bilbao'
    elif c == 'Real Sociedad':
        df.at[s, 'State'] = 'País Vasco'
        df.at[s, 'City'] = 'San Sebastián'
    elif c == 'Alavés':
        df.at[s, 'State'] = 'País Vasco'
        df.at[s, 'City'] = 'Vitoria-Gasteiz'
    elif c == 'Valencia':
        df.at[s, 'State'] = 'Comunidad Valenciana'
        df.at[s, 'City'] = 'Valencia'
    elif c == 'Villarreal':
        df.at[s, 'State'] = 'Comunidad Valenciana'
        df.at[s, 'City'] = 'Villarreal'
    elif c == 'Celta Vigo':
        df.at[s, 'State'] = 'Galicia'
        df.at[s, 'City'] = 'Vigo'
    elif c == 'Osasuna':
        df.at[s, 'State'] = 'Navarra'
        df.at[s, 'City'] = 'Pamplona'
    elif c == 'Mallorca':
        df.at[s, 'State'] = 'Islas Baleares'
        df.at[s, 'City'] = 'Palma de Mallorca'
    elif c == 'Las Palmas':
        df.at[s, 'State'] = 'Canarias'
        df.at[s, 'City'] = 'Las Palmas'
    elif c == 'Valladolid':
        df.at[s, 'State'] = 'Castile and León'
        df.at[s, 'City'] = 'Valladolid'
    elif c.strip() == 'Sevilla':
        df.at[s, 'State'] = 'Andalucía'
        df.at[s, 'City'] = 'Sevilla'
    elif c == 'Leganés':
        df.at[s, 'State'] = 'Comunidad de Madrid'
        df.at[s, 'City'] = 'Leganés'
    elif c == 'Rayo Vallecano':
        df.at[s, 'State'] = 'Comunidad de Madrid'
        df.at[s, 'City'] = 'Madrid'
    elif c == 'Betis':
        df.at[s, 'State'] = 'Andalucía'
        df.at[s, 'City'] = 'Sevilla'

# Map clubs to their stadiums
for s, c in df['Club'].items():
    if c == 'Barcelona':
        df.at[s, 'Stadium'] = 'Estadi Olímpic Lluís Companys'
    elif c == 'Espanyol':
        df.at[s, 'Stadium'] = 'RCDE Stadium'
    elif c == 'Girona':
        df.at[s, 'Stadium'] = 'Estadi Municipal de Montilivi'
    elif c == 'Real Madrid':
        df.at[s, 'Stadium'] = 'Santiago Bernabéu'
    elif c == 'Atlético Madrid':
        df.at[s, 'Stadium'] = 'Estadio Metropolitano'
    elif c == 'Getafe':
        df.at[s, 'Stadium'] = 'Coliseum Alfonso Pérez'
    elif c == 'Athletic Club':
        df.at[s, 'Stadium'] = 'San Mamés'
    elif c == 'Real Sociedad':
        df.at[s, 'Stadium'] = 'Reale Arena'
    elif c == 'Alavés':
        df.at[s, 'Stadium'] = 'Estadio de Mendizorroza'
    elif c == 'Valencia':
        df.at[s, 'Stadium'] = 'Mestalla Stadium'
    elif c == 'Villarreal':
        df.at[s, 'Stadium'] = 'Estadio de la Cerámica'
    elif c == 'Celta Vigo':
        df.at[s, 'Stadium'] = 'Abanca Balaídos'
    elif c == 'Osasuna':
        df.at[s, 'Stadium'] = 'Estadio El Sadar'
    elif c == 'Mallorca':
        df.at[s, 'Stadium'] = 'Estadi Mallorca Son Moix'
    elif c == 'Las Palmas':
        df.at[s, 'Stadium'] = 'Estadio de Gran Canaria'
    elif c == 'Valladolid':
        df.at[s, 'Stadium'] = 'Estadio José Zorrilla'
    elif c.strip() == 'Sevilla':
        df.at[s, 'Stadium'] = 'Estadio Ramón Sánchez Pizjuán'
    elif c == 'Leganés':
        df.at[s, 'Stadium'] = 'Estadio Municipal de Butarque'
    elif c == 'Rayo Vallecano':
        df.at[s, 'Stadium'] = 'Estadio de Vallecas'
    elif c == 'Betis':
        df.at[s, 'Stadium'] = 'Estadio Benito Villamarín'

# Initialize geocoding service
key = '////'
geocoder = OpenCageGeocode(key)

# Add latitude and longitude columns for cities
df["Latitude"] = None
df["Longitude"] = None

# Geocode cities to get coordinates
for i, row in df.iterrows():
    city = row["City"]  
    if pd.notnull(city):
        try:
            results = geocoder.geocode(f"{city}, Spain")
            if results:
                df.at[i, "Latitude"] = results[0]['geometry']['lat']
                df.at[i, "Longitude"] = results[0]['geometry']['lng']
            else:
                print(f"Not found: {city}")
        except Exception as e:
            print(f"Error geocoding {city}: {e}")
        time.sleep(1)  # Rate limiting for API calls

# Add stadium coordinates manually for each stadium
for s, c in df['Stadium'].items():
    if c == 'Estadi Olímpic Lluís Companys':
        df.at[s, 'Stadium_Latitude'] = 41.3675
        df.at[s, 'Stadium_Longitude'] = 2.1500
    elif c == 'RCDE Stadium':
        df.at[s, 'Stadium_Latitude'] = 41.3472
        df.at[s, 'Stadium_Longitude'] = 2.0800
    elif c == 'Estadi Municipal de Montilivi':
        df.at[s, 'Stadium_Latitude'] = 41.9613
        df.at[s, 'Stadium_Longitude'] = 2.8291
    elif c == 'Santiago Bernabéu':
        df.at[s, 'Stadium_Latitude'] = 40.4531
        df.at[s, 'Stadium_Longitude'] = -3.6883
    elif c == 'Estadio Metropolitano':
        df.at[s, 'Stadium_Latitude'] = 40.4378
        df.at[s, 'Stadium_Longitude'] = -3.6097
    elif c == 'Coliseum Alfonso Pérez':
        df.at[s, 'Stadium_Latitude'] = 40.3256
        df.at[s, 'Stadium_Longitude'] = -3.7147
    elif c == 'San Mamés':
        df.at[s, 'Stadium_Latitude'] = 43.2581
        df.at[s, 'Stadium_Longitude'] = -2.9424
    elif c == 'Reale Arena':
        df.at[s, 'Stadium_Latitude'] = 43.3200
        df.at[s, 'Stadium_Longitude'] = -1.9800
    elif c == 'Estadio de Mendizorroza':
        df.at[s, 'Stadium_Latitude'] = 42.8372
        df.at[s, 'Stadium_Longitude'] = -2.6881
    elif c == 'Mestalla Stadium':
        df.at[s, 'Stadium_Latitude'] = 39.4747
        df.at[s, 'Stadium_Longitude'] = -0.3764
    elif c == 'Estadio de la Cerámica':
        df.at[s, 'Stadium_Latitude'] = 39.9373
        df.at[s, 'Stadium_Longitude'] = -0.1004
    elif c == 'Abanca Balaídos':
        df.at[s, 'Stadium_Latitude'] = 42.2377
        df.at[s, 'Stadium_Longitude'] = -8.7247
    elif c == 'Estadio El Sadar':
        df.at[s, 'Stadium_Latitude'] = 42.7967
        df.at[s, 'Stadium_Longitude'] = -1.6369
    elif c == 'Estadi Mallorca Son Moix':
        df.at[s, 'Stadium_Latitude'] = 39.5900
        df.at[s, 'Stadium_Longitude'] = 2.6300
    elif c == 'Estadio de Gran Canaria':
        df.at[s, 'Stadium_Latitude'] = 28.1000
        df.at[s, 'Stadium_Longitude'] = -15.4539
    elif c == 'Estadio José Zorrilla':
        df.at[s, 'Stadium_Latitude'] = 41.6517
        df.at[s, 'Stadium_Longitude'] = -4.7417
    elif c == 'Estadio Ramón Sánchez Pizjuán':
        df.at[s, 'Stadium_Latitude'] = 37.3828
        df.at[s, 'Stadium_Longitude'] = -5.9731
    elif c == 'Estadio Municipal de Butarque':
        df.at[s, 'Stadium_Latitude'] = 40.3444
        df.at[s, 'Stadium_Longitude'] = -3.7386
    elif c == 'Estadio de Vallecas':
        df.at[s, 'Stadium_Latitude'] = 40.3919
        df.at[s, 'Stadium_Longitude'] = -3.6589
    elif c == 'Estadio Benito Villamarín':
        df.at[s, 'Stadium_Latitude'] = 37.3538
        df.at[s, 'Stadium_Longitude'] = -5.9755

