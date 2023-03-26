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
        choice = self.s.selectbox('선택', area, index = area['서울특별시'])
        return choice

    # 셀렉트 박스 선택 결과 처리 
    def select_choice(self):
        choice = self.create_sidebar()
        result = self.df[self.df['지사명'] == choice]
        result.reset_index(drop=True, inplace=True)
        return result

    # 추 후 다른 함수 선언시 한번에 return 하는 용으로 만듬
    def result_sidebar(self):
        result = self.select_choice()
        return result