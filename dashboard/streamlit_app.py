import streamlit as st
import pandas as pd

st.title("Customer Segmentation Dashboard")

# Load data
df = pd.read_csv("Online Retail Data Set.csv", encoding='ISO-8859-1')

st.write("### Raw Data")
st.dataframe(df.head())

st.write("### Project Summary")
st.write("""
- RFM Analysis used
- K-Means clustering applied
- Customers segmented into 3 groups
""")
