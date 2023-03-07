import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
   "국비지원반.csv",
    columns=['이름', '성별', '직업'])

st.line_chart(chart_data)