import streamlit as st
import numpy as np
import pandas as pd

class Sidebar:
    def __init__(self, df) -> None:
        self.df = df

    def sidebar(self):
        s = st.sidebar
        s.title('여기가 타이틀')
        
        area = self.df['지사명'].unique().tolist()
        choice = s.selectbox('선택', area, index=10)

        result = self.df[self.df['지사명'] == choice]
        result.index = np.arange(1, len(result) + 1)

        return result
