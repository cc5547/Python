import streamlit as st
import numpy as np
import pandas as pd

class Sidebar:
    def __init__(self) -> None:
        self.s = st.sidebar
        self.age = ""
        self.gender_c = ['남자', '여자']
        self.y_n = ['예', '아니오']
    # 나이 받기
    def account_age(self):
        self.s.title('문진표를 작성해 주세요👇')
        age = self.s.text_input('나이를 입력해 주세요.', self.age)
        return age

    # 성별 받기
    def gender_choice(self):
        gender = self.s.radio('성별을 선택 해주세요.', self.gender_c)
        if gender == "남자" : return 1
        else : return 0

    # 심장병 유무
    def heart_sick(self):
        sick = self.s.radio('심장병이 있습니까?', self.y_n)
        if sick == "예" : return True
        else : return False

    # 후에 유지보수시 한번에 return 하는 용으로 만듬 main에서 이 함수를 호출함.
    def result_sidebar(self):
        age = self.account_age()
        gender = self.gender_choice()
        heart = self.heart_sick()

        return age, gender, heart