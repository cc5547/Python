import streamlit as st
import numpy as np
import pandas as pd

class Sidebar:
    def __init__(self, df) -> None:
        self.df = df
        self.s = st.sidebar

    # 셀렉트 박스 생성
    def create_sidebar(self):
        self.s.title('여기가 타이틀')

        area = self.df['지사명'].drop_duplicates().tolist()
        choice = self.s.selectbox('선택', area)
        return choice

    # 셀렉트 박스 선택 결과 처리 
    def select_choice(self, choice):
        result = self.df[self.df['지사명'] == choice]
        result.index = np.arange(1, len(result) + 1)
        return result

    # 후에 유지보수시 한번에 return 하는 용으로 만듬
    def result_sidebar(self):
        choice = self.create_sidebar()
        result = self.select_choice(choice)
        return result