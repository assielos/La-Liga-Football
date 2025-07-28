# La Liga Football Data Analysis & Machine Learning Project

## Overview
This project analyzes La Liga football data to understand player statistics, market values, and club performance across Spain. The project includes comprehensive data analysis, visualization, and machine learning models for market value prediction.

## Project Structure

```
footaball/
├── data/                          # Data files
│   ├── top5-players24-25.xlsx    # Original raw data (2854 players, 37 columns)
│   ├── la_liga.xlsx              # Processed data with coordinate
├── src/                          # Source code
│   ├── gathering.py              # Data collection and enrichment
│   ├── cleaning.py               # Data preprocessing
│   ├── analyzing.py              # Statistical analysis
│   ├── visual.py                 # Data visualization
│   ├── model.py                  # Machine learning model
├── myenv/                        # Python virtual environment
├── requirements.txt               # Python dependencies
└── README.md                     # Project documentation
```

## Original Data Source

### `top5-players24-25.xlsx`
- **Size**: 456KB, 2052 lines
- **Players**: 2854 players from top 5 European leagues
- **Columns**: 37 columns including comprehensive player statistics
- **Leagues**: Premier League, La Liga, Serie A, Bundesliga, Ligue 1
- **Time Period**: 2024-25 season

### Key Original Data Fields:
- **Player Info**: Rk, Player, Nation, Pos, Squad, Comp, Age, Born
- **Performance**: MP, Starts, Min, 90s, Gls, Ast, G+A, G-PK, PK, PKatt
- **Cards**: CrdY, CrdR
- **Advanced Stats**: xG, npxG, xAG, npxG+xAG, PrgC, PrgP, PrgR
- **Per 90 Stats**: Gls_90, Ast_90, G+A_90, G-PK_90, G+A-PK_90, xG_90, xAG_90, xG+xAG_90, npxG_90, npxG+xAG_90

## Data Processing Pipeline

### 1. Data Gathering (`src/gathering.py`)
**Purpose**: Collects and enriches football data with geographical and market information.

**Key Features**:
- **Web Scraping**: Fetches player market values from Transfermarkt website
- **Geographical Mapping**: Maps clubs to Spanish cities, states, and stadiums
- **Coordinate Data**: Adds latitude/longitude coordinates for cities and stadiums
- **API Integration**: Uses OpenCage Geocoding API for location data

**Main Functions**:
- `get_tm_profile_url()`: Searches for player profiles on Transfermarkt
- `get_market_value()`: Extracts market values from player profiles
- Club-to-location mapping for all La Liga teams
- Stadium coordinate assignment

### 2. Data Cleaning (`src/cleaning.py`)
**Purpose**: Preprocesses and standardizes the raw football data.

**Key Operations**:
- **Column Management**: Removes unnecessary columns and renames for clarity
- **Data Standardization**: Converts market values from strings to numeric format
- **Nationality Processing**: Extracts 3-letter country codes
- **Position Simplification**: Keeps only primary position for each player
- **Missing Data Handling**: Fills missing age values and converts to integers

**Data Transformations**:
- Market value conversion (€50m → 50,000,000)
- Player ranking system
- Age data correction for specific players
- Position data cleaning

### 3. Data Analysis (`src/analyzing.py`)
**Purpose**: Performs comprehensive statistical analysis on the cleaned dataset.

**Analyses Performed**:

1. **Club Performance Analysis**:
   - Top 5 clubs by total matches played
   - Top 10 players by matches played
   - Top 5 clubs by goals and assists

2. **Geographical Analysis**:
   - Top 5 cities by total player market value
   - Top states/regions by player market value

3. **Player Distribution Analysis**:
   - Number of players per club
   - Relationship between squad size and total market value

4. **Nationality Analysis**:
   - Spanish vs non-Spanish players comparison
   - Market value analysis by nationality
   - Top 5 nations by total player value

5. **Club-Specific Analysis**:
   - Barcelona players detailed analysis
   - Key metrics for Barcelona squad

### 4. Data Visualization (`src/visual.py`)
**Purpose**: Creates interactive visualizations to present the analysis results.

**Visualizations Created**:

1. **Interactive Map**: 
   - Shows all La Liga clubs on a map of Spain
   - Bubble size represents total club market value
   - Hover information includes city, stadium, and value

2. **Pie Chart**: 
   - Compares market value distribution between Spanish and non-Spanish players

3. **Bar Chart**: 
   - Top 5 nations by total player market value
   - Color-coded by value

4. **Scatter Plot**: 
   - Barcelona players plotted by age vs market value
   - Individual player identification

## Machine Learning Model

### Market Value Prediction Model (`src/model.py`)
**Purpose**: Predicts player market values based on performance and demographic features.

**Features Used**:
- **Demographic**: Age, Nation, Club, City
- **Performance**: Goals, Assists, Minutes played
- **Position**: Player position (FW, MF, DF, GK)

**Model Architecture**:
```python
Pipeline([
    ('preprocess', ColumnTransformer([
        ('num', StandardScaler(), ['Age', 'Goals', 'Min']),
        ('cat', OneHotEncoder(), ['Nation', 'Club', 'Pos', 'City'])
    ])),
    ('regressor', RandomForestRegressor())
])
```

**Model Performance Metrics**:
- **R² Score**: Coefficient of determination
- **MAE**: Mean Absolute Error

## Data Sources
- **Primary Data**: `top5-players24-25.xlsx` - Comprehensive player statistics from top 5 European leagues
- **Filtered Data**: La Liga subset extracted from original dataset
- **Market Values**: Transfermarkt website (web scraping)
- **Geographical Data**: OpenCage Geocoding API
- **Stadium Information**: Manual coordinate assignment

## Key Technologies Used
- **Python Libraries**: pandas, numpy, scikit-learn, matplotlib, seaborn, plotly
- **Machine Learning**: RandomForest, GradientBoosting, Linear Regression, SVR
- **APIs**: OpenCage Geocoding API
- **Web Scraping**: Transfermarkt website
- **Visualization**: Plotly for interactive charts and maps
- **Data Processing**: Excel file handling with openpyxl

## Installation & Setup

### 1. Clone the repository
```bash
git clone <repository-url>
cd footaball
```

### 2. Create virtual environment
```bash
python -m venv myenv
myenv\Scripts\activate  # Windows
# source myenv/bin/activate  # Linux/Mac
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the analysis pipeline
```bash
# Data gathering and preprocessing
python src/gathering.py
python src/cleaning.py

# Data analysis and visualization
python src/analyzing.py
python src/visual.py

# Machine learning model
python src/model.py
```

## Usage Instructions

### Data Processing
1. **Data Gathering**: Run `src/gathering.py` to collect market values and geographical data
2. **Data Cleaning**: Run `src/cleaning.py` to preprocess the data
3. **Analysis**: Run `src/analyzing.py` to perform statistical analysis
4. **Visualization**: Run `src/visual.py` to generate interactive visualizations

### Machine Learning
1. **Model Training**: Run `src/model.py` to train the market value prediction modele

## Key Insights
- Market value distribution across Spanish regions
- Performance correlation with player age and value
- Club investment patterns and squad composition
- Nationality diversity in La Liga
- Geographical concentration of football talent in Spain
- Machine learning model for market value prediction
- Feature importance in determining player values

## Model Performance
- **R² Score**: Model accuracy in predicting market values
- **MAE**: Average prediction error in euross

## File Dependencies
- `data/top5-players24-25.xlsx`: Original comprehensive dataset
- `data/la_liga.xlsx`: Processed La Liga data with geographical information
- `src/`: All Python source code files
- `requirements.txt`: Python package dependencies
- Environment: Python virtual environment with required packages

## Notes
- Web scraping includes polite delays to avoid overwhelming servers
- API keys need to be configured for geocoding functionality
- Data filtering focuses on La Liga from the broader European dataset
- Visualizations are interactive and open in browser windows
- Original dataset provides context for broader European football analysis
- Machine learning model provides insights into market value determinants 