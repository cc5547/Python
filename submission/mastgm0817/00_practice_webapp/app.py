import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("국비지원반.CSV")

fig, ax = plt.subplots()
ax.pie(df, autopct='%1.1f%%')
ax.axis('equal')

st.pyplot(fig)
