import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

@st.cache_resource
def load_data(file_path):
    # Load the data
    df = pd.read_csv(file_path)
    
    # Replace non-numeric values with NaN and then fill NaN with 0
    df.replace(" - ", np.nan, inplace=True)
    df.fillna(0, inplace=True)

    # Convert all columns except 'Programmes' and 'CAMPUS' to numeric
    for col in df.columns:
        if col not in ['Programmes', 'CAMPUS']:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
            
    return df

def show_ppti_page():
    # Load data
    file_path = 'PPTT_numbers.csv'
    ppti = load_data(file_path)

    # Streamlit App
    st.title('PPTI Numbers Analysis')

    # Sidebar for campus selection
    selected_campus = st.sidebar.selectbox('Select Campus', ppti['CAMPUS'].unique())

    # Filter data based on selected campus
    filtered_data = ppti[ppti['CAMPUS'] == selected_campus]

    # Display filtered data in a table
    st.write(f"### Admission Numbers for {selected_campus}")
    st.dataframe(filtered_data)

    # Sidebar for program selection within the selected campus
    selected_program = st.sidebar.selectbox('Select Program', filtered_data['Programmes'].unique())

    # Filter data based on selected program
    program_data = filtered_data[filtered_data['Programmes'] == selected_program]

    # Visualize enrollment data for the selected program using a bar chart
    if not program_data.empty:
        st.write(f"### Admission Trends for {selected_program} at {selected_campus}")
        melted_df = pd.melt(program_data, id_vars=['Programmes', 'CAMPUS'], var_name='Trimester', value_name='Enrollment')
        melted_df['Trimester'] = melted_df['Trimester'].apply(lambda x: x.replace('TRIM', 'Trimester '))
        
        plt.figure(figsize=(12, 8))
        sns.barplot(data=melted_df, x='Trimester', y='Enrollment', hue='Programmes')
        plt.title(f'Admission Trends for {selected_program} at {selected_campus}')
        plt.xlabel('Trimester')
        plt.ylabel('Admission Numbers')
        plt.xticks(rotation=45)
        plt.grid(True)
        st.pyplot(plt)
    else:
        st.write(f"No data available for {selected_program} at {selected_campus}")
        
    if st.sidebar.button("Back"):
        st.session_state.page = "department_details"

# Run the app
if __name__ == "__main__":
    show_ppti_page()
