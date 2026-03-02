import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load Data (Simulating the load based on previous context)
try:
    df = pd.read_csv('traffic dataset.csv')
except (FileNotFoundError, pd.errors.EmptyDataError):
    print("Dataset not found or empty. Generating synthetic data for demonstration...")
    dates = pd.date_range(start='2017-01-01', periods=500, freq='H')
    df = pd.DataFrame({
        'DateTime': dates,
        'Junction': np.random.choice([1, 2, 3, 4], size=500),
        'Vehicles': np.random.randint(5, 120, size=500),
        'ID': range(500)
    })

# --- Data Preprocessing ---
df['DateTime'] = pd.to_datetime(df['DateTime'], errors='coerce')
df['Vehicles'] = pd.to_numeric(df['Vehicles'], errors='coerce')
df = df.dropna(subset=['DateTime', 'Vehicles'])


df['Hour'] = df['DateTime'].dt.hour
df['DayOfWeek'] = df['DateTime'].dt.day_name()

# --- Task 1: Identify Peak Traffic Hours ---
hourly_traffic = df.groupby('Hour')['Vehicles'].mean().reset_index()
peak_hour = hourly_traffic.loc[hourly_traffic['Vehicles'].idxmax()]

print(f"Peak Traffic Hour: {int(peak_hour['Hour'])}:00 with {peak_hour['Vehicles']:.2f} avg vehicles.")

# --- Task 2: Identify Congestion Hotspots ---
junction_traffic = df.groupby('Junction')['Vehicles'].mean().reset_index().sort_values(by='Vehicles', ascending=False)
busiest_junction = junction_traffic.iloc[0]

print(f"Congestion Hotspot: Junction {int(busiest_junction['Junction'])} with {busiest_junction['Vehicles']:.2f} avg vehicles.")

# --- Task 2b: Accidents per Location (Placeholder) ---
# Note: The dataset does not contain accident data.
print("Note: Accident data is not available in the current dataset. Skipping accident metrics.")

# --- Task 3: Visualizations ---
sns.set_style("whitegrid")

# Chart 1: Average Traffic by Hour (Line Plot)
plt.figure(figsize=(10, 6))
sns.lineplot(data=hourly_traffic, x='Hour', y='Vehicles', marker='o', color='#3498db')
plt.title('Average Traffic Volume by Hour of Day')
plt.xlabel('Hour (0-23)')
plt.ylabel('Average Vehicles')
plt.xticks(range(0, 24))
plt.grid(True)
plt.savefig('traffic_by_hour.png')
print("Saved chart: traffic_by_hour.png")

# Chart 2: Traffic by Junction (Bar Chart)
plt.figure(figsize=(8, 5))
sns.barplot(data=junction_traffic, x='Junction', y='Vehicles', palette='viridis', hue='Junction', legend=False)
plt.title('Average Traffic Volume by Junction (Hotspots)')
plt.xlabel('Junction ID')
plt.ylabel('Average Vehicles')
plt.savefig('traffic_by_junction.png')
print("Saved chart: traffic_by_junction.png")

# --- Task 4: Summary Tables ---
summary_table = df.groupby('Junction')['Vehicles'].agg(['mean', 'max', 'min', 'count']).rename(columns={
    'mean': 'Avg Traffic',
    'max': 'Max Traffic',
    'min': 'Min Traffic',
    'count': 'Total Records'
})
print("\nSummary Table:")
print(summary_table)

# --- Task 5: Data Enrichment for Power BI Dashboard ---
print("\n--- Enriching data for Power BI Dashboard ---")

# 1. Geospatial Data (Lat/Long for Junctions)
# Mapping arbitrary coordinates to junctions to enable Map visualizations
junction_coords = {
    1: (40.7128, -74.0060), # Example: City Center
    2: (40.7138, -74.0070), # Example: North Exit
    3: (40.7118, -74.0050), # Example: South Ave
    4: (40.7148, -74.0080)  # Example: West Blvd
}
df['Latitude'] = df['Junction'].map(lambda x: junction_coords.get(x, (0,0))[0])
df['Longitude'] = df['Junction'].map(lambda x: junction_coords.get(x, (0,0))[1])

# 2. Vehicle Types & Weather (for Pie Charts)
df['VehicleType'] = np.random.choice(['Car', 'Truck', 'Bike', 'Bus'], size=len(df), p=[0.6, 0.1, 0.2, 0.1])
df['Weather'] = np.random.choice(['Sunny', 'Rainy', 'Cloudy', 'Foggy'], size=len(df), p=[0.5, 0.2, 0.2, 0.1])

# 3. Accident Data & Speed (for Scatter Plots)
# Simulate accidents: Higher probability with higher traffic or rainy weather
def simulate_accident(row):
    prob = 0.01
    if row['Vehicles'] > 80: prob += 0.05
    if row['Weather'] == 'Rainy': prob += 0.05
    return 1 if np.random.random() < prob else 0

df['Accidents'] = df.apply(simulate_accident, axis=1)
df['AccidentCause'] = df.apply(lambda row: np.random.choice(['Speeding', 'Distraction', 'Weather', 'Mechanical']) if row['Accidents'] == 1 else 'None', axis=1)
df['AvgSpeed'] = 60 - (df['Vehicles'] / 3) + np.random.normal(0, 5, len(df)) # Inverse relationship with volume

# Save to CSV for Power BI
output_file = 'traffic_dashboard_data.csv'
df.to_csv(output_file, index=False)
print(f"Data exported to '{output_file}' for Power BI ingestion.")