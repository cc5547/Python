import streamlit as st
import numpy as np
import pandas as pd

class Function:
    def __init__(self, data, blood, clst, hbit, gender, heart, age) -> None:
        self.data = data
        self.ment_str = "마싯는 머신러닝"
    
    def into_xgb_model(self):
        # 나이, 성별, 심장병, 혈압, 콜레스테롤, 최대심박수
        tf = self.data.predict([[age, gender, heart, blood, clst, hbit]])
        tf_p = self.data.predict_proba([[age, gender, heart, blood, clst, hbit]])

    def create_model(self):
        tf, tf_p = self.into_xgb_model()
        return tf, tf_p

    # from joblib import dump, load
    # model1 = load('xgb_model.joblib')
    # k = model1.predict([[40,0,0,190,190,150]])
    # print(k)
    # proba = model.predict_proba([[40,0,0,190,190,150]])
    # print(np.array(proba)[:,1])