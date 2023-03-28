import streamlit as st
import numpy as np
import pandas as pd

class Sidebar:
    def __init__(self, df) -> None:
        self.df = df
        self.s = st.sidebar
        self.on = True
        self.off = False
        self.name = ""
        self.age = 0


    # 셀렉트 박스 생성
    def account_name(self):
        self.s.title('문진표를 작성해 주세요👇')

        self.name = self.s.text_input('이름을 입력해 주세요.', self.name)
        return self.name

    # 셀렉트 박스 선택 결과 처리 
    def first_choice(self, name):
        if name is "":
            return None, None, self.off
        else : 
            age = list(range(1, 100))
            age_choice = self.s.selectbox('나이를 입력해주세요.', age, , default = "")

            return name, age_choice, self.on

    # 후에 유지보수시 한번에 return 하는 용으로 만듬 main에서 이 함수를 호출함.
    def result_sidebar(self):
        name = self.account_name()
        name, age, on_off = self.first_choice(name)
        return name, age, on_off