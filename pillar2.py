import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_pillar2_page():
    # Streamlit app title
    st.title('Research, Entrepreneurship & Commercialization')
    
    # Dropdown menu for selecting the item to display
    option = st.selectbox(
        'Select the data/metrics item to display',
        (
            'Research, ethics and impact', 
            'Institutional capacity and partnerships',
            'Startup ecosystem',
            'Innovation and Commercialisation'
        )
    )
    
    # Example KPI data for several years starting from 2024
    data = {
        'Research, ethics and impact': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Research Publications': [50, 60, 70, 80, 90],
            'Citations': [300, 400, 500, 600, 700],
            'Ethics Approvals': [15, 18, 22, 25, 28],
            'Research Grants ($)': [200000, 250000, 300000, 350000, 400000]
        }),
        'Institutional capacity and partnerships': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Strategic Partnerships': [5, 6, 8, 10, 12],
            'Faculty Development Programs': [20, 25, 30, 35, 40],
            'Infrastructure Investments ($)': [500000, 600000, 700000, 800000, 900000],
            'Collaborative Projects': [10, 12, 14, 16, 18]
        }),
        'Startup ecosystem': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Startups Incubated': [10, 12, 14, 16, 18],
            'Funding Raised by Startups ($)': [100000, 150000, 200000, 250000, 300000],
            'Mentorship Programs': [5, 6, 7, 8, 9],
            'Startup Success Rate (%)': [70, 72, 75, 78, 80]
        }),
        'Innovation and Commercialisation': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Patents Filed': [8, 10, 12, 14, 16],
            'Commercialized Innovations': [3, 4, 5, 6, 7],
            'Revenue from Innovations ($)': [50000, 75000, 100000, 125000, 150000],
            'Industry Collaborations': [6, 8, 10, 12, 14]
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
    show_pillar2_page()
