# research_support.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

def show_research_support_page():
    # Provided data for Research Opportunities Posted (January - June 2024)
    months = ["January", "February", "March", "April", "May", "June"]
    grants = [26, 27, 59, 64, 50, 16]
    innovation_grants = [1, 2, 16, 7, 5, 6]
    conferences = [14, 21, 30, 30, 24, 12]
    workshops_fellowships = [2, 6, 18, 19, 19, 6]
    scholarships = [12, 18, 38, 30, 24, 12]

    # Create dataframes
    research_data = {
        'Month': months,
        'Grants': grants,
        'Innovation Grants': innovation_grants,
        'Conferences': conferences,
        'Workshops & Fellowships': workshops_fellowships,
        'Scholarships': scholarships
    }
    df_research = pd.DataFrame(research_data)

    # Set page title
    st.title('Research Support & Dissemination')

    # Display the data
    st.write('## Research Opportunities Posted (January - June 2024)')
    st.dataframe(df_research)

    # Visualizations
    st.write('## Visualizations')

    # Bar chart for Research Opportunities Posted over the first half of 2024
    st.write("### Research Opportunities Posted (January - June 2024)")
    fig, ax = plt.subplots(figsize=(12, 6))
    bar_width = 0.15
    bar_positions = np.arange(len(months))

    ax.bar(bar_positions - 2*bar_width, grants, width=bar_width, label='Grants')
    ax.bar(bar_positions - bar_width, innovation_grants, width=bar_width, label='Innovation Grants')
    ax.bar(bar_positions, conferences, width=bar_width, label='Conferences')
    ax.bar(bar_positions + bar_width, workshops_fellowships, width=bar_width, label='Workshops & Fellowships')
    ax.bar(bar_positions + 2*bar_width, scholarships, width=bar_width, label='Scholarships')

    ax.set_xticks(bar_positions)
    ax.set_xticklabels(months)
    ax.set_title('Research Opportunities Posted (January - June 2024)')
    ax.set_xlabel('Month')
    ax.set_ylabel('Count')
    ax.legend()

    st.pyplot(fig)

    # Pie chart for Research Opportunities distribution in June 2024
    st.write("### Research Opportunities Distribution in June 2024")
    june_data = {
        'Type': ['Grants', 'Innovation Grants', 'Conferences', 'Workshops & Fellowships', 'Scholarships'],
        'Count': [grants[-1], innovation_grants[-1], conferences[-1], workshops_fellowships[-1], scholarships[-1]]
    }
    df_june = pd.DataFrame(june_data)
    fig = px.pie(df_june, values='Count', names='Type', title='Research Opportunities Distribution in June 2024')
    fig.update_traces(pull=[0.1]*len(df_june), hole=0.3)
    st.plotly_chart(fig, use_container_width=True)

    #st.write("### Tagline")
    #st.markdown("**Developed by the Division of Research Innovation and Outreach**")

    if st.button("Back to Research Innovation and Outreach"):
        st.session_state.page = "department_details"

# Run the app
if __name__ == "__main__":
    show_research_support_page()
