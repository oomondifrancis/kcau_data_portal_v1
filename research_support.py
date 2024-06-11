# research_support.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

def show_research_support_page():
    # Generate dummy data
    total_publications = 150
    grants_applied_for = np.random.randint(50, 100)
    grants_won = np.random.randint(20, 50)
    increase_in_opportunities = np.random.uniform(5, 15)

    # Generate dummy data for grant amounts in USD and Kenyan Shillings
    grants_applied_for_usd = np.random.uniform(5000, 10000, grants_applied_for)
    grants_won_usd = np.random.uniform(2000, 5000, grants_won)
    usd_to_kes_conversion_rate = 110.50  # Dummy conversion rate

    grants_applied_for_kes = grants_applied_for_usd * usd_to_kes_conversion_rate
    grants_won_kes = grants_won_usd * usd_to_kes_conversion_rate

    # Create a dataframe for the data
    data = {
        'Metric': ['Total Publications', 'Grants Applied For (USD)', 'Grants Won (USD)', 'Increase in Opportunities (%)'],
        'Value': [total_publications, f"${grants_applied_for_usd.sum():,.2f}", f"${grants_won_usd.sum():,.2f}", increase_in_opportunities]
    }
    df = pd.DataFrame(data)

    # Set page title
    st.title('Research Support & Dissemination')

    # Display the data
    st.write('## Metrics Overview')
    st.dataframe(df)

    # Additional insights for grant amounts
    st.write('### Additional Grant Amounts (in Kenyan Shillings)')
    if grants_applied_for > 0:
        st.write(f"Total amount applied for (KES): Ksh {grants_applied_for_kes.sum():,.2f}")
    if grants_won > 0:
        st.write(f"Total amount won (KES): Ksh {grants_won_kes.sum():,.2f}")

    # Visualizations
    st.write('## Visualizations')

    # Pie chart for research areas
    st.write("### Research Areas")
    research_areas = ["Machine Learning", "Green Finance", "Education & Arts", "Creative Economy", "Data Science"]
    research_area_counts = np.random.randint(10, 50, len(research_areas))
    research_area_data = pd.DataFrame({
        "Research Area": research_areas,
        "Count": research_area_counts
    })
    fig = px.pie(research_area_data, values='Count', names='Research Area', title='Research Areas Distribution')
    st.plotly_chart(fig, use_container_width=True)

    # Line chart for grants over time
    years = range(2010, 2022)
    grants_applied_for_yearly = np.random.randint(50, 100, len(years))
    grants_won_yearly = np.random.randint(20, 50, len(years))

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(years, grants_applied_for_yearly, label='Grants Applied For', marker='o')
    ax.plot(years, grants_won_yearly, label='Grants Won', marker='s')
    ax.set_title('Grants Over Time')
    ax.set_xlabel('Year')
    ax.set_ylabel('Count')
    ax.legend()
    st.pyplot(fig)

    if st.button("Back to Research Innovation and Outreach"):
        st.session_state.page = "department_details"
