import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Segmentation", layout="wide")

# -------------------------
# TITLE
# -------------------------
st.title(" Customer Segmentation Dashboard")

# -------------------------
# SIDEBAR
# -------------------------
page = st.sidebar.radio("Navigation", ["Overview", "Insights", "Segments"])

# -------------------------
# OVERVIEW
# -------------------------
if page == "Overview":
    st.header("📌 Project Overview")

    st.write("""
    This project uses RFM (Recency, Frequency, Monetary) analysis 
    and K-Means clustering to segment customers.

    🎯 Goal:
    - Identify high-value customers
    - Improve retention strategies
    - Optimize marketing decisions
    """)

    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", "4338")
    col2.metric("Segments Created", "3")
    col3.metric("Top Segment", "High Value")

# -------------------------
# INSIGHTS
# -------------------------
elif page == "Insights":
    st.header("📊 Key Insights")

    st.write("""
    - Revenue is highly concentrated among a small group of customers  
    - Strong seasonal trend observed in monthly revenue  
    - Customer spending is highly skewed  
    """)

    st.subheader("📈 Monthly Revenue Trend")
    st.image("images/monthly_revenue.png")

    st.subheader("📉 Elbow Method")
    st.image("images/elbow_plot.png")

# -------------------------
# SEGMENTS
# -------------------------
elif page == "Segments":
    st.header(" Customer Segments")

    # Cluster Table
    st.subheader("📊 Cluster Summary")

    cluster_data = {
        "Cluster": ["Low Value", "Medium Value", "High Value"],
        "Recency": [174, 64, 14],
        "Frequency": [15, 64, 267],
        "Monetary": [303, 1161, 6605]
    }

    cluster_df = pd.DataFrame(cluster_data)
    st.dataframe(cluster_df)

    # Dropdown interaction
    st.subheader(" Explore Customer Segments")

    segment_option = st.selectbox(
        "Select Segment",
        ["Low Value", "Medium Value", "High Value"]
    )

    if segment_option == "Low Value":
        st.warning("Inactive customers → re-engage with discounts and campaigns")
    elif segment_option == "Medium Value":
        st.info("Potential customers → upsell and cross-sell strategies")
    else:
        st.success("High-value customers → focus on retention and loyalty programs")

    # Cluster Visualization
    st.subheader("📍 Cluster Visualization")
    st.image("images/cluster_k3.png")

    st.success("Business Impact: Better targeting → Higher retention → Increased revenue")
