import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_pillar3_page():
    # Streamlit app title
    st.title('Resource Mobilization, Optimisation & Sustainability')
    
    # Dropdown menu for selecting the item to display
    option = st.selectbox(
        'Select the data/metrics item to display',
        (
            'Financial optimisation and sustainability',
            'Implementation of infrastructure master plan',
            'Enhance institutional resources mobilisation',
            'Human capital management',
            'Environmental sustainability and reporting',
            'Governance risk and compliance'
        )
    )
    
    # Example KPI data for several years starting from 2024
    data = {
        'Financial optimisation and sustainability': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Cost Reduction (%)': [5, 6, 7, 8, 9],
            'Revenue Growth (%)': [10, 12, 14, 15, 16],
            'Operational Efficiency (%)': [80, 82, 85, 87, 90],
            'Surplus/Deficit ($)': [50000, 60000, 70000, 80000, 90000]
        }),
        'Implementation of infrastructure master plan': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Projects Completed': [2, 3, 4, 5, 6],
            'Investment in Infrastructure ($)': [1000000, 1200000, 1400000, 1600000, 1800000],
            'Facility Upgrades': [5, 6, 7, 8, 9],
            'New Buildings Constructed': [1, 2, 3, 4, 5]
        }),
        'Enhance institutional resources mobilisation': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'External Funding Secured ($)': [200000, 250000, 300000, 350000, 400000],
            'Alumni Contributions ($)': [50000, 60000, 70000, 80000, 90000],
            'Partnerships Formed': [4, 5, 6, 7, 8],
            'Grant Proposals Submitted': [10, 12, 15, 18, 20]
        }),
        'Human capital management': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Employee Satisfaction (%)': [85, 86, 87, 88, 89],
            'Training Programs Conducted': [10, 12, 15, 18, 20],
            'Retention Rate (%)': [90, 91, 92, 93, 94],
            'New Hires': [30, 35, 40, 45, 50]
        }),
        'Environmental sustainability and reporting': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Carbon Footprint Reduction (%)': [5, 6, 7, 8, 9],
            'Energy Efficiency Improvements (%)': [10, 12, 14, 16, 18],
            'Waste Reduction (%)': [20, 22, 25, 27, 30],
            'Sustainability Reports Published': [1, 1, 1, 1, 1]
        }),
        'Governance risk and compliance': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Compliance Audits Passed': [95, 96, 97, 98, 99],
            'Risk Mitigation Strategies Implemented': [5, 6, 7, 8, 9],
            'Training on Compliance and Risk': [10, 12, 15, 18, 20],
            'Incidents Reported': [3, 2, 1, 1, 1]
        })
    }
    
    # Display the selected data/metrics item
    if option in data:
        st.write(f"Selected option: {option}")
        df = data[option]
        if 'Year' in df.columns:
            df['Year'] = df['Year'].astype(str)  # Convert Year to string to avoid commas
        st.dataframe(df)
    else:
        st.write("No data available for the selected option.")
    
    if st.button("Back"):
        st.session_state.page = "department_details"
    
    
# Run the Streamlit app
if __name__ == "__main__":
    show_pillar3_page()
