import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io


def upload_csv():        
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        data = uploaded_file.read().decode("utf-8")
        df = pd.read_csv(io.StringIO(data))
        st.dataframe(df)

pushed = st.button("번호 추첨", on_click=upload_csv)

