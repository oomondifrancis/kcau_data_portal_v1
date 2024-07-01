import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_staffcount_page():
    # Define the non-academic staff data
    non_academic_staff = {
        "Qualifications": ['Diplomas', 'Undergraduate Degree', 'Masters Degree', 'Doctor of Philosophy(PhD)', 'Diplomas', 'Undergraduate Degree', 'Masters Degree', 'Doctor of Philosophy(PhD)'],
        "Gender": ["Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male"],
        "Staff Count": [30, 35, 50, 24, 25, 20, 15, 10]
    }
    
    # Define the academic staff data
    academic_staff = {
        "Qualifications": ['Diplomas', 'Undergraduate Degree', 'Masters Degree', 'Doctor of Philosophy(PhD)', 'Diplomas', 'Undergraduate Degree', 'Masters Degree', 'Doctor of Philosophy(PhD)'],
        "Gender": ["Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male"],
        "Staff Count": [12, 14, 25, 34, 10, 12, 15, 20]
    }
    
    # Create DataFrames for the staff numbers by qualifications
    non_academic_df = pd.DataFrame(non_academic_staff)
    academic_df = pd.DataFrame(academic_staff)
    
    # Streamlit app
    st.title("KCAU Staff Data")
    
    # Dropdown menu for selecting the item to display
    option = st.selectbox(
        'Select the data item to display',
        ('Non-Academic Staff', 'Academic Staff')
    )
    
    # Display the selected item
    if option == 'Non-Academic Staff':
        st.subheader("Non-Academic Staff Data")
        st.dataframe(non_academic_df)  # Display the DataFrame
        # Plotting the data
        fig, ax = plt.subplots()
        sns.barplot(x='Qualifications', y='Staff Count', hue='Gender', data=non_academic_df, ax=ax)
        ax.set_title('Non-Academic Staff by Qualifications and Gender')
        plt.xticks(rotation=45)
        st.pyplot(fig)
    elif option == 'Academic Staff':
        st.subheader("Academic Staff Data")
        st.dataframe(academic_df)  # Display the DataFrame
        # Plotting the data
        fig, ax = plt.subplots()
        sns.barplot(x='Qualifications', y='Staff Count', hue='Gender', data=academic_df, ax=ax)
        ax.set_title('Academic Staff by Qualifications and Gender')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    if st.button("Back"):
        st.session_state.page = "department_details"

# Run the app
if __name__ == "__main__":
    show_staffcount_page()
