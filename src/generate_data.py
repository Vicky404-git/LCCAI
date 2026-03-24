import pandas as pd
import numpy as np
import os

def generate_dummy_dataset(num_records=1000, output_path="data/dummy_building_data.csv"):
    """
    Generates synthetic building data to train the baseline ML models.
    """
    np.random.seed(42) # For reproducibility
    
    data = {
        "building_area_sqm": np.random.randint(500, 20000, num_records),
        "building_age_years": np.random.randint(1, 60, num_records),
        "material_quality_index": np.random.uniform(0.5, 1.0, num_records), # 1.0 is highest quality
        "initial_construction_cost": np.random.randint(1000000, 50000000, num_records),
        "climate_zone_severity": np.random.randint(1, 5, num_records), # 1=Mild, 4=Harsh
    }
    
    df = pd.DataFrame(data)
    
    # Simulate Target Variables (What the ML will predict)
    # Maintenance increases with age and harsh climates, decreases with high material quality
    df["actual_annual_maintenance"] = (
        (df["initial_construction_cost"] * 0.02) * (1 + (df["building_age_years"] * 0.01)) * (df["climate_zone_severity"] * 0.5) / 
        df["material_quality_index"]
    ).astype(int)
    
    # Energy cost correlates with area and climate
    df["actual_annual_energy"] = (
        df["building_area_sqm"] * 150 * df["climate_zone_severity"]
    ).astype(int)

    # Ensure data directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    df.to_csv(output_path, index=False)
    print(f"[SYSTEM] Generated {num_records} records at {output_path}")

if __name__ == "__main__":
    generate_dummy_dataset()
