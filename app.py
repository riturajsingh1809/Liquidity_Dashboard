
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Liquidity Dashboard", layout="wide")

st.title("Liquidity Dashboard")

df = pd.read_excel("Task05_Sample_Dataset.xlsx")

st.subheader("Dataset Preview")
st.dataframe(df)

col1, col2, col3 = st.columns(3)

col1.metric("Companies", df["Company_ID"].nunique())
col2.metric("Jobs", df["Job_ID"].nunique())
col3.metric("Applications", len(df))

company_jobs = df.groupby("Company_Name")["Job_ID"].count()
st.subheader("Company-wise Jobs")
st.bar_chart(company_jobs)

location_apps = df.groupby("Location")["Student_ID"].count()
st.subheader("Location-wise Applications")
st.bar_chart(location_apps)
