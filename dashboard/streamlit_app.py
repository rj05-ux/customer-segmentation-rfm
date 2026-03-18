import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Segmentation", layout="wide")

# Title
st.title(" Customer Segmentation Dashboard")

# Sidebar
st.sidebar.header("Navigation")
option = st.sidebar.radio("Go to", ["Overview", "Insights", "Segments"])

# -------------------------
# OVERVIEW
# -------------------------
if option == "Overview":
    st.header(" Project Overview")

    st.write("""
    This project uses RFM (Recency, Frequency, Monetary) analysis 
    and K-Means clustering to segment customers based on behavior.
    
    Goal:
    - Identify high-value customers
    - Improve retention strategies
    - Optimize marketing decisions
    """)

# -------------------------
# INSIGHTS
# -------------------------
elif option == "Insights":
    st.header(" Key Insights")

    st.write("""
    - Revenue is highly concentrated among a small group of customers
    - Strong seasonal trend observed in monthly revenue
    - Customer spending is highly uneven (skewed distribution)
    """)

    st.subheader("Monthly Revenue Trend")
    st.image("images/monthly_revenue.png")

    st.subheader("Elbow Method")
    st.image("images/elbow_plot.png")

# -------------------------
# SEGMENTS
# -------------------------
elif option == "Segments":
    st.header(" Customer Segments")

    st.write("""
    ### Cluster 0 — Low Value Customers
    - High Recency
    - Low Frequency
    - Low Monetary

    ### Cluster 1 — Medium Value Customers
    - Moderate behavior
    - Growth potential

    ### Cluster 2 — High Value Customers
    - Recent purchases
    - High spending
    """)

    st.subheader("Cluster Visualization")
    st.image("images/cluster_k3.png")

    st.success("Business Impact: Target customers based on segment for better revenue optimization")
