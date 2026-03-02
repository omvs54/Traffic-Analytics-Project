# 🚦 Traffic Analytics Project

End-to-end **Data Engineering, Analysis, and Business Intelligence** pipeline for optimizing urban traffic flow.  
This project transforms raw sensor data into actionable insights, enabling congestion hotspot detection, peak usage analysis, and strategic traffic management solutions.

---

## 📌 Project Overview
- **Objective:** Convert raw traffic sensor data into actionable strategies for congestion reduction.  
- **Role:** Data Analyst / Engineer  
- **Tools:** Python (Pandas, Seaborn), SQL, Power BI  
- **Outcome:** Projected **15–20% reduction in wait times** via dynamic signaling and infrastructure recommendations.

---

## 🛠️ Phase 1: Data Engineering
- **Data Cleaning Pipeline (Python):**
  - Median imputation for missing values  
  - Standardized timestamp formats  
  - Feature engineering (Hour, Region)  

```python
df['DateTime'] = pd.to_datetime(df['DateTime'], errors='coerce')
df['Vehicles'] = pd.to_numeric(df['Vehicles'], errors='coerce')
df['Vehicles'].fillna(df['Vehicles'].median(), inplace=True)
df['Hour'] = df['DateTime'].dt.hour
df['Region'] = df['Junction'].map(junction_mapping)
```
📊 Phase 2: Exploratory Data Analysis
- Peak Hours:
- Evening rush (17:00–19:00) → Critical congestion
- Secondary peak at 08:00
- Hotspot Analysis:
| Junction | Avg Vehicles/Hour | Congestion Level |
|1 (Downtown) | 85.4 | Critical |
| 2 (North Exit) | 45.2 | Moderate |
| 3 (South Ave) | 32.1 | Low |

📈 Phase 3: Power BI Dashboard
- Interactive Features:
- Slicers for Date Range, Weather Condition
- Geospatial mapping with latitude/longitude integration
- Hierarchical drill‑downs (Region → Intersection)
- Performance Optimization:
- Refined DAX measures (variables, DIVIDE)
- Reduced query load times by 40%
<img width="1920" height="1080" alt="Screenshot (86)" src="https://github.com/user-attachments/assets/9f254d55-e982-4308-964f-f9a208e90cf7" />

🧩 Phase 4: Strategic Solutions
- Short-Term: Dynamic signal timing (+20s green light for Northbound lanes at Junction 1 during rush hours).
- Medium-Term: Deploy traffic marshals during rainy weather (10% drop in flow speed).
- Long-Term: Infrastructure review to widen turn lane at Junction 1.

✨ Author
Created by Om Satarkar

Passionate about building robust analytics pipelines and showcasing them with cinematic, tech-forward branding.

[Traffic Optimization Project Portfolio.pdf](https://github.com/user-attachments/files/25691674/Traffic.Optimization.Project.Portfolio.pdf)

  
