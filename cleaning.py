import pandas as pd

# Load the dataset from Excel file
df = pd.read_excel("la_liga.xlsx" )

# Remove unnecessary columns that are not needed for analysis
df = df.drop(columns=['90s','npxG','npxG+xAG','Gls_90','Ast_90','G-PK_90','G+A-PK_90','xG_90','xG+xAG_90','npxG_90','npxG+xAG_90','G+A_90','xAG_90'])

# Rename columns for better clarity and consistency
df = df.rename(columns={'Shots':'Shots_on_Goals','Matches Played':'Matches_Played'})
df = df.rename(columns={'PKatt':'Penalty_Kicks_Attempted','xAG':'xA'})

# Create Club column from Squad column and remove Squad
df['Club'] = df['Squad']
df.drop(columns=['Squad','index'],inplace=True)

# Remove competition and birth date columns as they're not needed
df.drop(columns=['Comp'],inplace=True)
df.drop(columns=['Born'],inplace=True)

# Rename MP column to be more descriptive
df = df.rename(columns={'MP':'Matches Played'})

# Rename additional columns for clarity
df = df.rename(columns={'MP':'Matches Played',
                         'Gls':'Goals','Ast':'Assist','CrdR':'YCrad','CrdR':'RCard'})

# Clean nationality data by removing country codes and keeping only the main nationality
df['Nation'] = df['Nation'].str.replace(r'\b[a-z]{2}\s+', '', regex=True)

# Extract only the primary position for each player
df['Pos'] = df['Pos'].str.split(',').str[0] 

# Fill missing age values with 0 and convert to integer
df['Age'] = df['Age'].fillna(0).astype(int)

# Sort the dataset by player name and reset index
df = df.sort_values(by='Player').reset_index()

# Add a ranking column
df['Rk'] = range(1,len(df)+1)

# Extract 3-letter country codes from nationality
df['Nation'] = df['Nation'].str.extract(r'(\b[A-Z]{3}\b)', expand=False)

# Fix specific player data (Fer López age correction)
df.loc[df['Player'].str.contains('Fer López',na=False),'Age']= 21

def convert(val):
    """
    Convert market value strings to numeric values
    Args:
        val: Market value string (e.g., '€50m', '€500k')
    Returns:
        int: Market value in euros
    """
    if isinstance(val,str):
        val = val.replace('€','').lower().strip()
        if 'm' in val:
            return float(val.replace('m',''))*1_000_000
        elif 'k' in val:
           return float(val.replace('k',''))*1_000
        else:
            return val

# Apply the conversion function to Value column
df['Value'] = df['Value'].apply(convert).astype(int)


