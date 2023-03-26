import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
# from PIL import Image
# import requests

st.set_page_config(layout="wide")

# df생성
def create_df() :
    df_URL = "https://raw.githubusercontent.com/cc5547/Python/main/submission/cc5547/02_second_webapp/%EC%8B%9C%ED%97%98%EC%9E%A5%EC%86%8C_%EA%B0%80%EA%B3%B5%EC%B2%98%EB%A6%AC.csv"
    df = pd.read_csv(df_URL).iloc[:, 1:]
    df.index += 1
    return df
# @st.cache
@st.cache(suppress_st_warning=True)

def side_bar(df) :
    s = st.sidebar
    s.title('여기가 타이틀')
    s.write("여기다가 만들자!")
    df = df.head()
    return df

def main() :
    df = create_df()

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["1번탭", "2번탭", "3번탭", "4번탭", "5번탭"])
    col1, col2 = st.columns([8, 2])

    with tab1 :
        st.write("여기가 머신러닝 시각화_1")
    with tab2 :
        st.write("여기가 머신러닝 시각화_2")
    with tab3 :
        st.write("여기가 머신러닝 시각화")
    with tab4 :
        st.write("여기가 머신러닝 시각화")
    with tab5 :
        st.write("여기가 머신러닝 시각화")

    with col1 :
        # Title
        st.title("Hi")
        # Header/Subheader
        st.header("나야")
        st.subheader("하이")
        # Text
        st.text("여기가 output되는 값 예정")
        st.dataframe(side_bar(df), width = 1000, height = 500)

    with col2 :
        # Select Box
        job = st.selectbox("직군을 선택하세요.",
                                    ["Backend Developer",
                                    "Frontend Developer",
                                    "ML Engineer",
                                    "Data Engineer",
                                    "Database Administrator",
                                    "Data Scientist",
                                    "Data Analyst",
                                    "Security Engineer"])
        st.write(f"당신의 직군은 {job}입니다.")

        
if __name__ == '__main__' :
    main()