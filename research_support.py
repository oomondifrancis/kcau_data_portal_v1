# research_support.py

import streamlit as st
import pandas as pd
import plotly.express as px

def show_research_support_page():
    st.set_page_config(layout="wide")  # full-width app
    # Define months and years
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    
    years = [2023, 2024, 2025]
    
    # === SAMPLE DATA ===
    posted_data = {
        2023: {
            'Grants': [15, 18, 22, 25, 20, 10, 8, 9, 12, 14, 13, 11],
            'Innovation Grants': [2, 3, 5, 4, 6, 3, 2, 3, 4, 5, 3, 2],
            'Conferences': [10, 12, 14, 16, 15, 7, 6, 8, 10, 11, 12, 9],
            'Workshops & Fellowships': [3, 4, 6, 5, 7, 3, 2, 3, 4, 6, 5, 4],
            'Scholarships': [8, 9, 12, 11, 10, 6, 5, 6, 8, 9, 7, 6]
        },
        2024: {
            'Grants': [20, 22, 25, 30, 27, 15, 12, 13, 16, 18, 20, 22],
            'Innovation Grants': [3, 4, 6, 7, 5, 4, 3, 4, 5, 6, 4, 3],
            'Conferences': [12, 14, 18, 20, 19, 10, 8, 9, 11, 12, 14, 13],
            'Workshops & Fellowships': [4, 6, 8, 9, 8, 5, 4, 5, 6, 7, 6, 5],
            'Scholarships': [10, 12, 15, 14, 13, 7, 6, 7, 9, 10, 8, 7]
        },
        2025: {
            'Grants': [26, 27, 59, 64, 50, 16, 13, 18, 16, 22, 24, 28],
            'Innovation Grants': [1, 2, 16, 7, 5, 6, 5, 7, 4, 6, 7, 8],
            'Conferences': [14, 21, 30, 30, 24, 12, 9, 11, 13, 15, 16, 18],
            'Workshops & Fellowships': [2, 6, 18, 19, 19, 6, 5, 8, 9, 10, 11, 12],
            'Scholarships': [12, 18, 38, 30, 24, 12, 11, 10, 9, 11, 12, 14]
        }
    }

    # Won data ~40% success
    won_data = {
        year: {cat: [int(val * 0.4) for val in posted_data[year][cat]] for cat in posted_data[year]}
        for year in years
    }

    # Sidebar filters
    st.sidebar.header("Filters")
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_category = st.sidebar.multiselect(
        "Select Category (optional)", 
        options=list(posted_data[selected_year].keys()),
        default=list(posted_data[selected_year].keys())
    )
    
    # === Annual Summary ===
    summary_records = []
    for cat in posted_data[selected_year].keys():
        posted_sum = sum(posted_data[selected_year][cat])
        won_sum = sum(won_data[selected_year][cat])
        success_rate = (won_sum / posted_sum * 100) if posted_sum > 0 else 0
        summary_records.append({
            "Category": cat,
            "Posted": posted_sum,
            "Won": won_sum,
            "Success %": round(success_rate, 1)
        })
    df_summary = pd.DataFrame(summary_records)
    df_summary.loc[len(df_summary.index)] = [
        "Overall", df_summary["Posted"].sum(), df_summary["Won"].sum(),
        round((df_summary["Won"].sum() / df_summary["Posted"].sum() * 100), 1)
    ]

    # Top metrics (reduce empty space)
    st.title("📊 Research Support & Dissemination Dashboard")
    st.markdown(f"### Overview for **{selected_year}**")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Posted", int(df_summary["Posted"].sum()))
    col2.metric("Total Won", int(df_summary["Won"].sum()))
    col3.metric("Overall Success %", f"{df_summary.iloc[-1]['Success %']}%")

    # Tabs for Monthly / Annual / Quarterly
    tab1, tab2, tab3 = st.tabs(["📅 Monthly Details", "📈 Annual Summary", "🗓 Quarterly Trends"])

    with tab1:
        # Build detailed monthly data
        records = []
        for i, month in enumerate(months):
            row = {"Month": month}
            for cat in posted_data[selected_year].keys():
                if cat not in selected_category: 
                    continue
                posted_val = posted_data[selected_year][cat][i]
                won_val = won_data[selected_year][cat][i]
                success_rate = (won_val / posted_val * 100) if posted_val > 0 else 0
                row[f"{cat} (Posted)"] = posted_val
                row[f"{cat} (Won)"] = won_val
                row[f"{cat} (Success %)"] = round(success_rate, 1)
            records.append(row)

        df_combined = pd.DataFrame(records)
        st.dataframe(df_combined, use_container_width=True)

        if not df_combined.empty:
            fig = px.line(df_combined, x="Month", 
                          y=[c for c in df_combined.columns if "(Posted)" in c or "(Won)" in c],
                          markers=True, title="Monthly Posted vs Won")
            st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("Annual Summary by Category")
        st.dataframe(df_summary, use_container_width=True)
        
        fig = px.bar(df_summary[df_summary["Category"]!="Overall"], 
                     x="Category", y=["Posted","Won"], barmode="group",
                     title=f"Annual Posted vs Won Opportunities ({selected_year})")
        st.plotly_chart(fig, use_container_width=True)

        fig2 = px.bar(df_summary[df_summary["Category"]!="Overall"], 
                      x="Category", y="Success %", text="Success %",
                      title=f"Success Rate by Category ({selected_year})")
        st.plotly_chart(fig2, use_container_width=True)

    with tab3:
        quarters = {"Q1": [0,1,2], "Q2": [3,4,5], "Q3": [6,7,8], "Q4": [9,10,11]}
        selected_quarter = st.selectbox("Select Quarter", list(quarters.keys()))
        q_idx = quarters[selected_quarter]

        quarter_data = {}
        for cat in posted_data[2023].keys():
            row = {"Category": cat}
            for year in years:
                posted_sum = sum([posted_data[year][cat][m] for m in q_idx])
                won_sum = sum([won_data[year][cat][m] for m in q_idx])
                success_rate = (won_sum / posted_sum * 100) if posted_sum > 0 else 0
                row[f"{year} Posted"] = posted_sum
                row[f"{year} Won"] = won_sum
                row[f"{year} Success %"] = round(success_rate, 1)
            quarter_data[cat] = row

        df_quarter = pd.DataFrame(list(quarter_data.values()))
        st.dataframe(df_quarter, use_container_width=True)

        fig3 = px.line(df_quarter, x="Category", 
                       y=[f"{y} Success %" for y in years], 
                       markers=True, title=f"Quarterly Success Rate Across Years ({selected_quarter})")
        st.plotly_chart(fig3, use_container_width=True)

    # Back button
    if st.button("⬅️ Back"):
        st.session_state.page = "department_details"


# ✅ Entry point
if __name__ == "__main__":
    show_research_support_page()
