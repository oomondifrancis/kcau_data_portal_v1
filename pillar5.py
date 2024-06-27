import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_pillar5_page():
    # Streamlit app title
    st.title('Stakeholder Engagement')
    
    # Dropdown menu for selecting the item to display
    option = st.selectbox(
        'Select the data/metrics item to display',
        (
            'Internal stakeholder engagement',
            'External stakeholder engagement',
            'Foster Equity and inclusiveness'
        )
    )
    
    # Example KPI data for several years starting from 2024
    data = {
        'Internal stakeholder engagement': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Employee Satisfaction (%)': [75, 78, 80, 82, 85],
            'Internal Communications Initiatives': [10, 12, 15, 17, 20],
            'Engagement Activities': [8, 10, 12, 14, 16]
        }),
        'External stakeholder engagement': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Partnerships Formed': [5, 6, 8, 10, 12],
            'Community Engagement Events': [6, 8, 10, 12, 14],
            'Stakeholder Satisfaction (%)': [70, 73, 75, 78, 80]
        }),
        'Foster Equity and inclusiveness': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Diversity Initiatives Implemented': [3, 5, 7, 8, 10],
            'Inclusivity Training Sessions': [4, 6, 8, 10, 12],
            'Employee Diversity (%)': [30, 35, 40, 45, 50]
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
    show_pillar5_page()
