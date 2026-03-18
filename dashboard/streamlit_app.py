import streamlit as st
import pandas as pd

st.title("Customer Segmentation Dashboard")

st.write("## Project Overview")
st.write("""
This project uses RFM analysis and K-Means clustering to segment customers into:
- High-value customers
- Medium-value customers
- Low-value customers
""")

st.write("## Sample Data")

# Load sample data (optional)
st.write("Dataset preview not included in deployment version")

st.write("## Insights")

st.write("""
- High-value customers contribute most revenue
- Few customers generate majority of sales
- Business should focus on retention and targeted marketing
""")
