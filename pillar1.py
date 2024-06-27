import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_pillar1_page():
    # Streamlit app title
    st.title('Excellence in Teaching and Learning')
    
    # Dropdown menu for selecting the item to display
    option = st.selectbox(
        'Select the data/metrics item to display',
        (
            'Quality of Teaching and Learning', 
            'Entrepreneurial-focused curriculum',
            'Transformative student experience',
            'Academic-industry linkage',
            'Student success',
            'Internationalization'
        )
    )
    
    # Example KPI data for several years starting from 2024
    data = {
        'Quality of Teaching and Learning': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Student Satisfaction (%)': [88, 89, 90, 91, 92],
            'Faculty Evaluation Score': [4.4, 4.5, 4.6, 4.7, 4.8],
            'Graduation Rate (%)': [82, 83, 84, 85, 86]
        }),
        'Entrepreneurial-focused curriculum': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Students in Entrepreneurial Programs': [350, 360, 370, 380, 390],
            'Startups Launched by Students': [18, 20, 22, 24, 26],
            'Entrepreneurial Courses Offered': [8, 9, 10, 11, 12]
        }),
        'Transformative student experience': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Student Engagement Index': [78, 79, 80, 81, 82],
            'Participation in Extracurricular Activities (%)': [75, 76, 77, 78, 79],
            'Retention Rate (%)': [89, 90, 91, 92, 93]
        }),
        'Academic-industry linkage': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Industry Partnerships': [22, 24, 26, 28, 30],
            'Internships Offered': [160, 170, 180, 190, 200],
            'Industry-led Workshops/Seminars': [8, 9, 10, 11, 12]
        }),
        'Student success': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'Employment Rate (%)': [80, 81, 82, 83, 84],
            'Average Starting Salary ($)': [38000, 39000, 40000, 41000, 42000],
            'Alumni Satisfaction (%)': [86, 87, 88, 89, 90]
        }),
        'Internationalization': pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'International Students': [150, 160, 170, 180, 190],
            'Study Abroad Programs': [5, 6, 7, 8, 9],
            'International Collaborations': [10, 12, 14, 16, 18]
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
    show_pillar1_page()
