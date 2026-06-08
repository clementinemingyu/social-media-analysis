import streamlit as st
import pandas as pd

st.title("Social Media Analysis Dashboard")

df = pd.read_csv("cleaned_social_media_data.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Post Topics")

topic_counts = df["PostTopic"].value_counts()

st.bar_chart(topic_counts)

st.subheader("Basic Statistics")

st.write(df.describe())