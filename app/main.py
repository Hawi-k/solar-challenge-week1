import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_all_data

st.set_page_config(page_title="MoonLight Energy Solutions Dashbord", layout="centered")

df = load_all_data()

st.sidebar.header("🔍 Filters")
selected_countries = st.sidebar.multiselect(
    "Select Country/Countries",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)
selected_metric = st.sidebar.selectbox("Select Metric", ["GHI", "DNI", "DHI"])

df_filtered = df[df["Country"].isin(selected_countries)]

# Dashboard Title
st.title("MoonLight Energy Solutions Dashbord")

# Boxplot
st.subheader(f"Distribution of {selected_metric}")
fig, ax = plt.subplots()
sns.boxplot(x="Country", y=selected_metric, data=df_filtered, palette="Set2", ax=ax)
st.pyplot(fig)

# Summary Stats Table
st.subheader("Summary Table")
summary_stats = df_filtered.groupby("Country")[selected_metric].agg(["mean", "median", "std"]).round(2)
st.dataframe(summary_stats)

# Ranking Chart
st.subheader("🏆 Ranking by Average GHI")
ranking = df_filtered.groupby("Country")["GHI"].mean().sort_values(ascending=False)
st.bar_chart(ranking)

# Footer
st.markdown("---")
st.caption("Created by [Hawi Kebebew] | 10 Academy AIM Week 0")
