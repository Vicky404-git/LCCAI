import sys
import pickle
import pandas as pd

# Import your mathematical core
from src.lcca_engine import calculate_lifecycle_cost

def load_ai_engines():
    """Loads the predictive models from the local data directory."""
    print("[SYSTEM] Booting AI Core from ./data/ directory...")
    try:
        with open("data/model_maintenance.pkl", "rb") as f:
            maint_model = pickle.load(f)
        with open("data/model_energy.pkl", "rb") as f:
            energy_model = pickle.load(f)
        return maint_model, energy_model
    except FileNotFoundError as e:
        print(f"\n[FATAL ERROR] Core ML models not found: {e}")
        print("[ACTION] Ensure Sagar's .pkl files are placed inside the ./data/ directory.")
        sys.exit(1)

def main():
    print("\n==================================================")
    print("             LCCAI CORE ENGINE v1.0               ")
    print("==================================================")

    # 1. Load the pickled models
    maint_model, energy_model = load_ai_engines()
    print("[SYSTEM] Engines loaded successfully. Ready for inference.\n")

    # 2. Define a Test Project (This is what you will eventually hook up to a UI/CLI prompt)
    project_input = {
        'building_area_sqm': [12000],
        'building_age_years': [1], 
        'material_quality_index': [0.85], # High quality
        'initial_construction_cost': [20000000], # ₹2 Crore
        'climate_zone_severity': [4] # Harsh climate
    }
    
    input_df = pd.DataFrame(project_input)

    # 3. Execute AI Predictions
    print("[SYSTEM] Running ML predictions for operational degradation...")
    predicted_annual_maint = maint_model.predict(input_df)[0]
    predicted_annual_energy = energy_model.predict(input_df)[0]

    print(f"  -> Predicted Maintenance: ₹{predicted_annual_maint:,.2f} / year")
    print(f"  -> Predicted Energy:      ₹{predicted_annual_energy:,.2f} / year\n")

    # 4. Execute LCCA Math (Traditional vs AI-Enhanced)
    print("[SYSTEM] Calculating 30-Year Net Present Value (NPV)...")
    
    # Traditional baseline (Static 1% maintenance assumption)
    static_maint = project_input['initial_construction_cost'][0] * 0.01
    static_energy = 600000 
    
    traditional_npv = calculate_lifecycle_cost(
        initial_cost=project_input['initial_construction_cost'][0],
        annual_maintenance=static_maint,
        annual_energy=static_energy,
        discount_rate=0.05,
        lifespan_years=30
    )

    # ML-Enhanced NPV
    ml_npv = calculate_lifecycle_cost(
        initial_cost=project_input['initial_construction_cost'][0],
        annual_maintenance=predicted_annual_maint,
        annual_energy=predicted_annual_energy,
        discount_rate=0.05,
        lifespan_years=30
    )

    # 5. Output Final Intelligence
    print("\n==================================================")
    print("              LCCAI FINANCIAL REPORT              ")
    print("==================================================")
    print(f"Traditional Estimate:   ₹{traditional_npv:,.2f}")
    print(f"ML-Enhanced Forecast:   ₹{ml_npv:,.2f}")
    
    difference = traditional_npv - ml_npv
    if difference > 0:
        print(f"\n[INSIGHT] Traditional methods OVERESTIMATED the budget by ₹{abs(difference):,.2f}.")
    else:
        print(f"\n[INSIGHT] Traditional methods UNDERESTIMATED the budget by ₹{abs(difference):,.2f}.")
        print("          WARNING: High probability of budget overrun due to climate severity.")
    print("==================================================\n")

if __name__ == "__main__":
    main()
