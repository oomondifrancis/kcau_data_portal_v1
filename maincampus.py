import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def show_maincampus_page():
    # Streamlit app
    logo = Image.open("kcau_logo.png")
    st.title("Main Campus(Ruaraka)")
    
    # Dropdown menu for selecting the item to display
    option = st.selectbox(
        'Select the data item to display',
        ('Student Numbers by Cohorts', 'Cohorts Count by Gender')   
    )
    
    #Data Upload
    df = pd.read_csv('/home/fochieng/projects/kcau_data_portal_v1/data/interim/new_2017_2024_data.csv')
        
    #Data preprocessing
    #1. Filter out Main Campus Data
    main_campus_df = df[df['Campus'] == "MAIN"]
    
    # Count unique Registration No. based on Cohorts
    main_cohort_counts = main_campus_df.groupby('Cohorts')['Registration No'].nunique().reset_index()
    # Rename columns for clarity
    main_cohort_counts.columns = ['Cohorts', 'Student Numbers']
    
    # Function to plot the bar graph for Student Number Counts by Cohorts
    def plot_unique_registration_no_count(main_cohort_counts):
        fig, ax = plt.subplots(figsize=(12, 8))
        bars = ax.bar(main_cohort_counts['Cohorts'], main_cohort_counts['Student Numbers'], color='skyblue')
        ax.set_title('Student Numbers by Cohorts')
        ax.set_xlabel('Cohorts')
        ax.set_ylabel('Student Numbers Count')
        ax.set_xticklabels(main_cohort_counts['Cohorts'], rotation=45)
        ax.grid(axis='y')

        # Add value labels on top of the bars
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), va='bottom', ha='center', fontsize=9, color='black', rotation='vertical')

        st.pyplot(fig)
        
    # Function to plot the bar graph for Cohorts Gender Count
    def plot_cohorts_gender_count():
        
        # Group by Cohorts and Gender, then count occurrences
        df_gender_count = main_campus_df.groupby(['Cohorts', 'Gender']).size().reset_index(name='Count')
       
        # Pivot the data for plotting
        df_pivot = df_gender_count.pivot(index='Cohorts', columns='Gender', values='Count').fillna(0)

        # Add a totals column
        df_pivot['Total'] = df_pivot.sum(axis=1)

        # Remove columns with all zeros except the Total column
        df_pivot = df_pivot.loc[:, (df_pivot != 0).any(axis=0) | (df_pivot.columns == 'Total')]

        # Plot the data without the totals
        fig, ax = plt.subplots(figsize=(20, 14))
        df_pivot_no_total = df_pivot.drop(columns=['Total'])
        df_pivot_no_total.plot(kind='bar', ax=ax)
        ax.set_title('Cohorts Gender Count')
        ax.set_xlabel('Cohorts')
        ax.set_ylabel('Count')
        ax.set_xticklabels(df_pivot.index, rotation=45)
        ax.legend(title='Gender')
        ax.grid(axis='y')

        # Add value labels on top of the bars
        for container in ax.containers:
            for bar in container:
                height = bar.get_height()
                if height > 0:  # Only add labels for non-zero values
                    ax.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=9, color='black', rotation='vertical')

        st.pyplot(fig)    
        # Display the selected item
    if option == 'Student Numbers by Cohorts':
        st.dataframe(main_cohort_counts)
        plot_unique_registration_no_count(main_cohort_counts)
        
    elif option == 'Cohorts Count by Gender':
        #st.dataframe(df_gender_count)
        plot_cohorts_gender_count()
  


    if st.button("Back"):
        st.session_state.page = "department_details"

# Run the app
if __name__ == "__main__":
    show_maincampus_page()
