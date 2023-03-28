import streamlit as st
import numpy as np
import pandas as pd

class Sidebar:
    def __init__(self, df) -> None:
        self.df = df
        self.s = st.sidebar
        # self.on = True
        # self.off = False
        self.age = None
        self.sex_c = ['남자', '여자']
    # 나이 받기
    def account_age(self):
        self.s.title('문진표를 작성해 주세요👇')
        age = self.s.text_input('나이를 입력해 주세요.', self.age)
        return age if age else None

    # 성별 받기
    def sex_choice(self, age):
        if age is None : return None
        
        sex = self.s.selectbox('성별을 선택해주세요.', self.sex_c)
        return 1 if sex == '남자' else 0

    # 후에 유지보수시 한번에 return 하는 용으로 만듬 main에서 이 함수를 호출함.
    def result_sidebar(self):
        age = self.account_age()
        sex = self.sex_choice(age)
        if age is None or sex is None:
            return None, None
        return age, sex