
import streamlit as st
import pandas as pd

st.title("Grocery Shopping Optimization")

st.write("This app uses Dynamic Programming to select grocery items within a budget.")

budget = st.number_input("Enter your grocery budget", min_value=1, value=30)

st.write("Budget selected:", budget)

st.write("Run the Python script locally to generate selected_items.csv, then upload results here.")

uploaded_file = st.file_uploader("Upload selected_items.csv", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    st.write("Total Cost:", df["price"].sum())
    st.write("Total Nutrition Score:", df["nutrition_score"].sum())
