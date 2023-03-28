import streamlit as st
import numpy as np
import pandas as pd

class Sidebar:
    def __init__(self, df) -> None:
        self.df = df
        self.s = st.sidebar
    # 셀렉트 박스 생성
    def account_name(self):
        self.s.title('문진표를 작성해 주세요👇')
        
        name = s_bar.text_input('이름을 입력해 주세요.', value = '')
        return name

    # 셀렉트 박스 선택 결과 처리 
    def first_choice(self, name):
        name = name

        return name

    # 후에 유지보수시 한번에 return 하는 용으로 만듬 main에서 이 함수를 호출함.
    def result_sidebar(self):
        result = self.first_choice(self.account_name())

        return result