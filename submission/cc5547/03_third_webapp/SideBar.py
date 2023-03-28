import streamlit as st
import numpy as np
import pandas as pd

class Sidebar:
    def __init__(self, df) -> None:
        self.df = df
        self.s = st.sidebar
        self.on = True
        self.off = False
        self.age = ""

    # 셀렉트 박스 생성
    def account_age(self):
        self.s.title('문진표를 작성해 주세요👇')

        self.age = self.s.text_input('나이를 입력해 주세요.', self.age)

        return self.age

    # 셀렉트 박스 선택 결과 처리 
    def first_choice(self, age):
        if age is "":
            return None, None, self.off
        else : 
            sex = ['남자', '여자']
            sex_choice = self.s.selectbox('성별을 선택해주세요.', sex, default = "")
            if sex_choice == '남자' : 
                sex_choice = 1
            else : 
                sex_choice = 0

            return age, sex_choice, self.on

    # 후에 유지보수시 한번에 return 하는 용으로 만듬 main에서 이 함수를 호출함.
    def result_sidebar(self):
        age = self.account_age()
        age, sex, on_off = self.first_choice(age)
        return age, sex, on_off