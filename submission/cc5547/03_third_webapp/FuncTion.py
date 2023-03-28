import streamlit as st
import numpy as np
import pandas as pd

class Function:
    def __init__(self, data, blood, clst, hbit, gender, heart, age) -> None:
        self.data = data
        self.blood = int(blood)
        self.clst = int(clst)
        self.hbit = int(hbit)
        self.gender = float(gender)
        self.heart = int(heart)
        self.age = float(age)
        # self.data = data
        # self.blood = blood.astype(np.int64)
        # self.clst = clst.astype(np.int64)
        # self.hbit = hbit.astype(np.int64)
        # self.gender = gender.astype(np.float32)
        # self.heart = heart.astype(np.int64)
        # self.age = age.astype(np.float32)

        
        
    def into_xgb_model(self):
        # 나이, 성별, 심장병, 혈압, 콜레스테롤, 최대심박수
        tf = self.data.predict([[self.age, self.gender, self.heart, self.blood, self.clst, self.hbit]])
        tf_p = self.data.predict_proba([[self.age, self.gender, self.heart, self.blood, self.clst, self.hbit]])
        tf_p = (np.array(tf_p)[:,1])
        return tf, tf_p

    def create_model(self):
        tf, tf_p = self.into_xgb_model()
        return tf, tf_p

    # from joblib import dump, load
    # model1 = load('xgb_model.joblib')
    # k = model1.predict([[40,0,0,190,190,150]])
    # print(k)
    # proba = model.predict_proba([[40,0,0,190,190,150]])
    # print(np.array(proba)[:,1])