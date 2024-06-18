import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data for Student Number Counts by Cohorts

def show_admissions_page():
    data = {
        'Cohorts': ['JAN 17', 'MAY 17', 'SEP 17', 'JAN 18', 'MAY 18', 'SEP 18', 'JAN 19', 'MAY 19', 'SEP 19',
                    'JAN 20', 'MAY 20', 'SEP 20', 'JAN 21', 'MAY 21', 'SEP 21', 'JAN 22', 'MAY 22', 'SEP 22',
                    'JAN 23', 'MAY 23', 'SEP 23', 'JAN 24'],
        'Unique Registration No Count': [2287, 528, 794, 2163, 670, 909, 2009, 1810, 1515,
                                        2342, 344, 2354, 2631, 1882, 5518, 2499, 2488, 5727,
                                        2879, 3240, 4299, 3394]
    }

    # Create DataFrame for Student Number Counts by Cohorts
    df = pd.DataFrame(data)

    # Streamlit app
    st.title('KCAU Admissions Data')

    # Dropdown menu for selecting the item to display
    option = st.selectbox(
        'Select the data item to display',
        ('Student Number Counts by Cohorts', 'Cohorts Gender Count')
    )

    # Function to plot the bar graph for Student Number Counts by Cohorts
    def plot_unique_registration_no_count(df):
        plt.figure(figsize=(12, 8))
        bars = plt.bar(df['Cohorts'], df['Unique Registration No Count'], color='blue')
        plt.title('Student Numbers by Cohorts')
        plt.xlabel('Cohorts')
        plt.ylabel('Student Numbers Count')
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        
        # Add value labels on top of the bars
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 100, int(yval), va='bottom', ha='center', fontsize=9)

        st.pyplot(plt)

    # Function to plot the bar graph for Cohorts Gender Count
    def plot_cohorts_gender_count():
        # Load the gender cohorts data
        df_gender = pd.read_csv('gender_cohorts.csv')
        
        # Pivot the data for plotting
        df_pivot = df_gender.pivot(index='Cohorts', columns='Gender', values='Count').fillna(0)
        
        # Plot the data
        ax = df_pivot.plot(kind='bar', figsize=(12, 8))
        plt.title('Cohorts Gender Count')
        plt.xlabel('Cohorts')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.legend(title='Gender')
        plt.grid(axis='y')
        
        # Add value labels on top of the bars
        for container in ax.containers:
            ax.bar_label(container, label_type='edge')
        
        st.pyplot(plt)
        
    
    # Display the selected item
    if option == 'Student Number Counts by Cohorts':
        plot_unique_registration_no_count(df)
    elif option == 'Cohorts Gender Count':
        plot_cohorts_gender_count()
        
    if st.button("Back"):
        st.session_state.page = "department_details"
        
        
