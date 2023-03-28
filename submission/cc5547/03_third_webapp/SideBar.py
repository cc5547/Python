import streamlit as st
import numpy as np
import pandas as pd

class Sidebar:
    def __init__(self) -> None:
        self.s = st.sidebar
        self.age = ""
        self.gender_c = ['남자', '여자']
    
    # 나이 받기
    def account_age(self):
        self.s.title('문진표를 작성해 주세요👇')
        age = self.s.text_input('나이를 입력해 주세요.', self.age)
        return age

    # 성별 받기
    def gender_choice(self):
        gender = self.s.selectbox('성별을 선택해주세요.', self.gender_c)
        return gender

    # 후에 유지보수시 한번에 return 하는 용으로 만듬 main에서 이 함수를 호출함.
    def result_sidebar(self):
        age = self.account_age()
        gender = self.gender_choice()
        return age, gender