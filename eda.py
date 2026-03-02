import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load Data (Simulating the load based on previous context)
try:
    df = pd.read_csv('traffic dataset.csv')
except FileNotFoundError:
    print("Dataset not found. Generating synthetic data for demonstration...")
    dates = pd.date_range(start='2017-01-01', periods=500, freq='H')
    df = pd.DataFrame({
        'DateTime': dates,
        'Junction': np.random.choice([1, 2, 3, 4], size=500),
        'Vehicles': np.random.randint(5, 120, size=500),
        'ID': range(500)
    })

# --- Data Preprocessing ---
df['DateTime'] = pd.to_datetime(df['DateTime'])
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
sns.barplot(data=junction_traffic, x='Junction', y='Vehicles', palette='viridis')
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