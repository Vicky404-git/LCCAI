def calculate_lifecycle_cost(initial_cost, annual_maintenance, annual_energy, discount_rate, lifespan_years):
    """
    Calculates the Net Present Value (NPV) of a project's lifecycle costs.
    This acts as the baseline for our ML comparison.
    """
    total_npv = initial_cost
    
    for year in range(1, lifespan_years + 1):
        # Total cost for the current year
        yearly_operating_cost = annual_maintenance + annual_energy
        
        # Discount it back to present value
        discounted_cost = yearly_operating_cost / ((1 + discount_rate) ** year)
        
        total_npv += discounted_cost
        
    return round(total_npv, 2)

# Quick Test Run
if __name__ == "__main__":
    baseline_cost = calculate_lifecycle_cost(
        initial_cost=5000000, 
        annual_maintenance=120000, 
        annual_energy=80000, 
        discount_rate=0.05, 
        lifespan_years=30
    )
    print(f"[SYSTEM] Traditional LCCA NPV: ₹{baseline_cost:,.2f}")
