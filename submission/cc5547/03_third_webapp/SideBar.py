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

        area1 = self.df['지사명'].drop_duplicates().tolist()
        choice1 = self.s.selectbox('선택', area)

        area2 = df[(df['지사명'] == choice1) & df['시험장소']].drop_duplicates.tolist
        choice2 = self.s.selectbox('선택', area2)

        area3 = df[(df['지사명'] == choice1) & df['시험장소']].drop_duplicates.tolist
        choice3 = self.s.selectbox('선택', area)

        return choice1, choice2, choice3

    # 셀렉트 박스 선택 결과 처리 
    def select_choice(self, choice):
        result = self.df[self.df['지사명'] == choice1]
        result = self.df[self.df['시험장소'] == choice2]
        result = self.df[self.df['시험장소'] == choice3]

        result.index = np.arange(1, len(result) + 1)

        return result

    # 후에 유지보수시 한번에 return 하는 용으로 만듬 main에서 이 함수를 호출함.
    def result_sidebar(self):
        result = self.select_choice(self.create_sidebar())

        return result