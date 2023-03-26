import streamlit as st
import numpy as np
import pandas as pd

class SideBar:
    def __init__(self, df) -> None:
        self.df = df
        self.ment = "마싯는 머신러닝"
    
    def sb_function(self):
        s = st.sidebar
        s.title('여기가 타이틀')
        area = df['지사명'].unique().tolist()
        choice = s.selectbox('선택', area, index = 10)
        result = df[df['지사명'] == choice]
        result.index = np.arange(1, len(result) + 1)
        return result

    def ment(self):
        return self.ment
        

