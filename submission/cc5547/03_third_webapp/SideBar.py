import streamlit as st
import numpy as np
# import pandas as pd

class Sidebar:
    def __init__(self, df) -> None:
        self.df = df
        self.s = st.sidebar

    def create_sidebar(self):
        self.s.title('여기가 타이틀')
        area = self.df['지사명'].unique().tolist()
        choice = self.s.selectbox('선택', area, index=10)
        return choice

    def select_choice(self):
        choice = self.create_sidebar()
        result = self.df[self.df['지사명'] == choice]
        result.index = np.arange(1, len(result) + 1)
        return result

    def result_sidebar(self):
        result = self.select_choice()
        return result