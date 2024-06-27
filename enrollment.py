import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_enrollment_page():
    # Streamlit app title
    st.title('KCAU Enrollment/Demographics')
    
    # Dropdown menu for selecting the item to display
    option = st.selectbox(
        'Select the data/metrics item to display',
        (
            'Total Enrollment (Head Count)', 
            'Total Students Full Time Equivalent',
            'Total Student Credit Hours',
            'Enrollment By Program',
            'Enrollment By School/Faculty',
            'Enrollment BY GSS/SSS'
        )
    )
    
    # Example data
    data = {
        'Total Enrollment (Head Count)': pd.DataFrame({
            'Year': [2020, 2021, 2022, 2023, 2024],
            'Enrollment': [1500, 1600, 1700, 1300, 1400]
        }),
        'Total Students Full Time Equivalent': pd.DataFrame({
            'Year': [2020, 2021, 2022, 2023, 2024],
            'FTE': [1400, 1500, 1600, 1250, 1100]
        }),
        'Total Student Credit Hours': pd.DataFrame({
            'Year': [2020, 2021, 2022, 2023, 2024],
            'Credit Hours': [45000, 47000, 49000, 50000, 47000]
        }),
        'Enrollment By Program': pd.DataFrame({
            'Program': ['Bachelor of Commerce', 'BSc IT', 'BBIT'],
            'Enrollment': [500, 600, 400]
        }),
        'Enrollment By School/Faculty': pd.DataFrame({
            'School/Faculty': ['School of Business', 'School of Technology', 'School of Education', 'PPTI'],
            'Enrollment': [800, 700, 500, 300]
        }),
        'Enrollment BY GSS/SSS': pd.DataFrame({
            'Group': ['GSS', 'SSS'],
            'Enrollment': [1000, 700]
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
    show_enrollment_page()
