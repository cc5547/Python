import streamlit as st
import numpy as np
import pandas as pd

class Sidebar:
    def __init__(self) -> None:
        self.s = st.sidebar
        self.space = ""
        self.gender_c = ['남자', '여자']
        self.y_n = ['예', '아니오']

    # 혈압 int
    def blood_pressure(self) :
        self.s.title('문진표를 작성해 주세요👇')
        blood = self.s.slider('혈압을 입력해주세요.', 0, 200, 1)
        return blood

    # 콜레스트롤 int 
    def cholesterol(self, blood) :
        if blood != 1 : 
            clst = self.s.slider('콜레스트롤을 입력하세요.', 0, 200, 1)
            return clst
        else : return None

    # 심박수 int 
    def heart_beat(self, clst) :
        if clst > 1:
            hbit = self.s.slider('심박수를 입력하세요', 0, 200, 1)
            return hbit
        else : return None

    # 성별 받기 float
    def gender_choice(self, hbit):
        if hbit > 1 and not None:
            gender = self.s.radio('성별을 선택 해주세요.', self.gender_c)
            if gender == "남자" : return 1
            else : return 0
        else : return None

    # 심장병 유무
    def heart_sick(self, gender):
        if gender != None:
            heart = self.s.radio('심장병이 있습니까?', self.y_n)
            if heart == "예" : return True 
            else : return False
        else : return None

    # 나이 받기 float
    def account_age(self, heart):
        if heart != None :
            age = self.s.text_input('나이를 입력해 주세요.', self.space)
            return age
        else : return None

    # 후에 유지보수시 한번에 return 하는 용으로 만듬 main에서 이 함수를 호출함.
    def result_sidebar(self):
        blood = self.blood_pressure()
        clst = self.cholesterol(blood)
        hbit = self.heart_beat(clst)
        gender = self.gender_choice(hbit)
        heart = self.heart_sick(gender)
        age = self.account_age(heart)

        return blood, clst, hbit, gender, heart, age