import streamlit as st
import numpy as np
import pandas as pd

class Function:
    def __init__(self, data, blood, clst, hbit, gender, heart, age) -> None:
        self.data = data
        self.blood = blood
        self.clst = clst
        self.hbit = hbit
        self.gender = gender
        self.heart = heart
        self.age = age
        
    def into_xgb_model(self):
            # 나이, 성별, 심장병, 혈압, 콜레스테롤, 최대심박수
            tf = self.data.predict([[float(self.age), float(self.gender), int(self.heart), int(self.blood), int(self.clst), int(self.hbit)]])
            tf_p = self.data.predict_proba([[float(self.age), float(self.gender), int(self.heart), int(self.blood), int(self.clst), int(self.hbit)]])
            # tf_p = (np.array(tf_p)[:,1])
            return tf, tf_p

    def create_model(self):
        tf, tf_p = self.into_xgb_model()
        return tf, tf_p