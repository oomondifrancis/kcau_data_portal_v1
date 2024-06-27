import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_pillar4_page():
    # Streamlit app title
    st.title('Digital Transformation')
    
    # Dropdown menu for selecting the item to display
    option = st.selectbox(
        'Select the data/metrics item to display',
        (
            'Sound ICT governance',
            'ICT infrastructure and connectivity',
            'Enhanced integrated information systems',
            'Cutting edge technologies for open and distance education',
            'Enhanced ICT security, data protection and ICT risk management',
            'Collaborations and partnerships with technology companies and other stakeholders'
        )
    )
    
    # Example KPI data for several years starting from 2024
    data = {
        'Sound ICT governance': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Governance Policies Implemented': [5, 6, 7, 8, 9],
            'Compliance Audits': [3, 4, 5, 6, 7],
            'Stakeholder Satisfaction (%)': [80, 82, 84, 86, 88]
        }),
        'ICT infrastructure and connectivity': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Network Uptime (%)': [95, 96, 97, 98, 99],
            'Bandwidth Capacity (Gbps)': [10, 15, 20, 25, 30],
            'New Hardware Installed': [50, 60, 70, 80, 90],
            'WiFi Coverage (%)': [85, 87, 90, 93, 95]
        }),
        'Enhanced integrated information systems': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Systems Integrated': [4, 5, 6, 7, 8],
            'User Satisfaction (%)': [75, 77, 80, 82, 85],
            'Data Accuracy (%)': [90, 92, 94, 96, 98]
        }),
        'Cutting edge technologies for open and distance education': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Online Courses Offered': [10, 15, 20, 25, 30],
            'Student Enrollment in Online Courses': [200, 300, 400, 500, 600],
            'Technology Adoption Rate (%)': [60, 65, 70, 75, 80],
            'Virtual Classroom Sessions': [50, 70, 90, 110, 130]
        }),
        'Enhanced ICT security, data protection and ICT risk management': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Security Incidents': [10, 8, 6, 4, 2],
            'Data Breaches': [2, 1, 1, 0, 0],
            'Security Audits': [4, 5, 6, 7, 8],
            'Employee Training Sessions': [5, 6, 7, 8, 9]
        }),
        'Collaborations and partnerships with technology companies and other stakeholders': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Partnerships Formed': [5, 7, 10, 12, 15],
            'Joint Projects': [3, 4, 5, 6, 7],
            'Funding Received ($)': [50000, 70000, 90000, 110000, 130000],
            'Workshops Conducted': [4, 5, 6, 7, 8]
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
    show_pillar4_page()
