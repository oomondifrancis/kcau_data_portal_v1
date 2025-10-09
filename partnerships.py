# enhanced_partnerships_dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px

def show_partnerships_page():
    st.set_page_config(layout="wide")  # full-width app
    
    st.title("🤝 Directorate of Partnerships & Collaborations Dashboard")

    # ----------------------------
    # Sample Data (replace with real inputs)
    # ----------------------------
    data = {
        "Year": [2023]*12 + [2024]*12 + [2025]*12,
        "Month": (["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])*3,
        "New MOUs Signed": [5,6,4,3,7,8,5,6,7,4,5,6,
                            7,8,6,5,9,10,8,7,6,5,7,8,
                            10,12,8,9,11,13,9,10,8,7,9,11],
        "Active MOUs": [40,41,42,42,43,45,46,47,48,49,49,50,
                        52,54,56,57,58,60,61,62,63,64,65,66,
                        68,70,72,74,75,77,78,80,82,83,84,85],
        "Inactive MOUs": [3,3,4,4,5,5,5,6,6,6,7,7,
                          7,8,8,8,9,9,9,10,10,10,11,11,
                          11,12,12,13,13,13,14,14,14,15,15,16]
    }

    df = pd.DataFrame(data)

    # ----------------------------
    # Sidebar Filters
    # ----------------------------
    st.sidebar.header("🔍 Filters")

    years = df["Year"].unique()
    selected_year = st.sidebar.selectbox("Select Year", years, index=len(years)-1)

    view_option = st.sidebar.radio("View By:", ["All MOUs", "Active Only", "Inactive Only"])

    df_year = df[df["Year"] == selected_year]

    # ----------------------------
    # KPI Cards
    # ----------------------------
    st.subheader(f"📊 Annual Overview - {selected_year}")

    col1, col2, col3 = st.columns(3)
    col1.metric("🆕 New MOUs Signed", df_year["New MOUs Signed"].sum())
    col2.metric("✅ Active MOUs", df_year["Active MOUs"].iloc[-1])
    col3.metric("🚫 Inactive MOUs", df_year["Inactive MOUs"].iloc[-1])

    st.markdown("---")

    # ----------------------------
    # Tabs for Interactive Navigation
    # ----------------------------
    tab1, tab2, tab3 = st.tabs(["📈 Monthly Trends", "📊 Quarterly Comparison", "🥧 Status Distribution"])

    # --- Tab 1: Monthly Trends ---
    with tab1:
        st.write("### Monthly Trends")
        
        if view_option == "All MOUs":
            fig = px.line(df_year, x="Month", y="New MOUs Signed", title=f"New MOUs Signed in {selected_year}",
                          markers=True, text="New MOUs Signed")
        elif view_option == "Active Only":
            fig = px.line(df_year, x="Month", y="Active MOUs", title=f"Active MOUs Trend in {selected_year}",
                          markers=True, text="Active MOUs")
        else:
            fig = px.line(df_year, x="Month", y="Inactive MOUs", title=f"Inactive MOUs Trend in {selected_year}",
                          markers=True, text="Inactive MOUs")

        fig.update_traces(textposition="top center")
        fig.update_layout(height=500, template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)

    # --- Tab 2: Quarterly Comparison ---
    with tab2:
        st.write("### Quarterly Comparison Across Years")

        df["Quarter"] = pd.PeriodIndex(
            pd.to_datetime(df["Month"] + " " + df["Year"].astype(str)), freq="Q"
        ).astype(str)

        quarterly = df.groupby(["Year","Quarter"]).agg({
            "New MOUs Signed":"sum",
            "Active MOUs":"max",
            "Inactive MOUs":"max"
        }).reset_index()

        quarterly["Quarter"] = quarterly["Quarter"].astype(str)  # FIX applied

        # Pivot table for easy glance
        st.dataframe(quarterly.pivot(index="Quarter", columns="Year", values="New MOUs Signed"))

        fig2 = px.bar(quarterly, x="Quarter", y="New MOUs Signed", color="Year", 
                      barmode="group", title="Quarterly New MOUs Comparison")
        st.plotly_chart(fig2, use_container_width=True)

    # --- Tab 3: Status Distribution ---
    with tab3:
        st.write("### Status Distribution at Year-End")
        status_data = {
            "Status": ["Active", "Inactive"],
            "Count": [df_year["Active MOUs"].iloc[-1], df_year["Inactive MOUs"].iloc[-1]]
        }
        df_status = pd.DataFrame(status_data)

        fig3 = px.pie(df_status, values="Count", names="Status", 
                      title=f"MOU Status Distribution ({selected_year})", hole=0.3)
        st.plotly_chart(fig3, use_container_width=True)
        
        # Back button
    if st.button("⬅️ Back"):
        st.session_state.page = "department_details"

    # Footer / branding
    #st.markdown("---")
    #st.markdown("**Developed by: Directorate of Partnerships & Collaborations** | 📍 KCA University")

# Run standalone
if __name__ == "__main__":
    show_partnerships_page()
