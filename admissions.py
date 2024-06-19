import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data for Student Number Counts by Cohorts
def show_admissions_page():
    data = {
        'Cohorts': ['JAN 17', 'MAY 17', 'SEP 17', 'JAN 18', 'MAY 18', 'SEP 18', 'JAN 19', 'MAY 19', 'SEP 19',
                    'JAN 20', 'MAY 20', 'SEP 20', 'JAN 21', 'MAY 21', 'SEP 21', 'JAN 22', 'MAY 22', 'SEP 22',
                    'JAN 23', 'MAY 23', 'SEP 23', 'JAN 24'],
        'Student Numbers': [2287, 528, 794, 2163, 670, 909, 2009, 1810, 1515,
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
        fig, ax = plt.subplots(figsize=(12, 8))
        bars = ax.bar(df['Cohorts'], df['Student Numbers'], color='skyblue')
        ax.set_title('Student Numbers by Cohorts')
        ax.set_xlabel('Cohorts')
        ax.set_ylabel('Student Numbers Count')
        ax.set_xticklabels(df['Cohorts'], rotation=45)
        ax.grid(axis='y')

        # Add value labels on top of the bars
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), va='bottom', ha='center', fontsize=9, color='black', rotation='vertical')

        st.pyplot(fig)

    # Function to plot the bar graph for Cohorts Gender Count
    def plot_cohorts_gender_count():
        # Load the gender cohorts data
        df_gender = pd.read_csv('gender_cohorts.csv')

        # Pivot the data for plotting
        df_pivot = df_gender.pivot(index='Cohorts', columns='Gender', values='Count').fillna(0)

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
        st.dataframe(df_pivot)  # Display the DataFrame with totals

    # Display the selected item
    if option == 'Student Number Counts by Cohorts':
        plot_unique_registration_no_count(df)
        st.dataframe(df)  # Display the DataFrame
    elif option == 'Cohorts Gender Count':
        plot_cohorts_gender_count()

    if st.button("Back"):
        st.session_state.page = "department_details"
