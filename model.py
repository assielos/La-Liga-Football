import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


# Load the dataset for modeling
df = pd.read_excel(r"la_liga.xlsx" )
pd.set_option('display.max_rows',None)

features = ['Age', 'Goals', 'Assist', 'Min', 'Nation', 'Club', 'Pos', 'City']
target = 'Value'

# Fix: Use 'passthrough' correctly or use StandardScaler for numerical features
preprocess = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['Age','Goals','Min']),  # Fixed: Use StandardScaler instead of 'passthrough'
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['Nation','Club','Pos','City'])
    ]
)

x = df[features]
y = df[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model_pipeline = Pipeline(steps=[
    ('preprocess', preprocess),
    ('regressor', RandomForestRegressor(random_state=42))
])

model_pipeline.fit(X_train, y_train)

y_pred = model_pipeline.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae:.2f}")
print(f"R2 Score: {r2:.2f}")

