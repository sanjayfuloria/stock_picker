import streamlit as st
from stock_picker.main import run

st.title("Stock Picker App")

sector = st.selectbox(
    "Select a sector for research:",
    ["Technology", "Consumer Goods", "Retail", "Energy"]
)

if st.button("Analyze Top 5 Companies"):
    with st.spinner("Analyzing companies in {}...".format(sector)):
        result = run(sector)
        st.subheader("Research Output:")
        st.write(result)
