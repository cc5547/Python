import streamlit as st
import numpy as np
import pandas as pd

# 나이 -> 성별 -> 심장병 -> 혈압 -> 콜레스테롤 -> 최대심박수 
class Sidebar:
    def __init__(self) -> None:
        self.s = st.sidebar
        self.age = ""
        self.gender_c = ['남자', '여자']
        self.y_n = ['예', '아니오']

    # 혈압 int로 후에 형변환
    def blood_pressure(self) :
        self.s.title('문진표를 작성해 주세요👇')
        return self.s.slider('혈압을 입력해주세요.', 0, 500, 1) or None

    # 콜레스트롤 int로 후에 형변환 
    def cholesterol(self, blood) : 
        return self.s.slider('콜레스트롤을 입력하세요.', 0, 500, 1) if blood is not None and blood > 1 else None
        # if blood is not None and blood > 1 : return self.s.slider('콜레스트롤을 입력하세요.', 0, 500, 1)
        # else : return None
    
    # 심박수 int로 후에 형변환
    def heart_beat(self, clst) : 
        if clst is not None and clst > 1 : return self.s.slider('심박수를 입력하세요', 0, 500, 1)
        else : return None

    # 성별 받기 float로 후에 형변환
    def gender_choice(self, hbit):
        if hbit is not None and hbit > 1 :
            if self.s.radio('성별을 선택 해주세요.', self.gender_c) == "남자" : return 1
            else : return 0
        else : return None
        
    # 심장병 유무 int로 후에 형변환
    def heart_sick(self, hbit) : 
        if hbit is not None and hbit > 1 :
            if self.s.radio('심장병이 있습니까?', self.y_n) == "예" : return 0 
            else : return 1
        else : return None

    # 나이 받기 float로 후에 형변환
    def account_age(self, hbit):
        if hbit is not None and hbit > 1 : return self.s.text_input('나이를 입력해 주세요.', self.age)
        else : return self.age

    # 후에 유지보수시 한번에 return 하는 용으로 만듬 handle에서 이 함수를 호출함.
    def result_sidebar(self) :
        blood = self.blood_pressure()
        clst = self.cholesterol(blood)
        hbit = self.heart_beat(clst)
        gender = self.gender_choice(hbit)
        heart = self.heart_sick(hbit)
        self.age = self.account_age(hbit)

        return blood, clst, hbit, gender, heart, self.age