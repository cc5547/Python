import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
   "submission/mastgm0817/00_practice_webapp/국비지원반.CSV",
    columns=['이름', '성별', '직업'])

st.line_chart(chart_data)