
import pandas as pd

# Load the dataset
df = pd.read_csv('traffic dataset.csv')

# Check for missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# For this dataset, we can either drop rows with missing values or fill them.
# Let's check the number of missing values first. If it's small, we can drop them.
# If you want to fill them, you can use:
# df.fillna(method='ffill', inplace=True) # Forward fill
# df.fillna(method='bfill', inplace=True) # Backward fill
# Or fill with a specific value like the mean or median
# df['Vehicles'].fillna(df['Vehicles'].mean(), inplace=True)

# For now, let's drop rows with any missing values
df.dropna(inplace=True)

print(
"Missing values after cleaning:")
print(df.isnull().sum())

# Standardize DateTime format
df['DateTime'] = pd.to_datetime(df['DateTime'])

# Create a 'Date' column
df['Date'] = df['DateTime'].dt.date

print("DataFrame Info after initial cleaning:")
df.info()

print("First 5 rows of the cleaned dataframe:")
print(df.head())
