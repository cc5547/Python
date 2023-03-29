import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
        tf = self.data.predict([[self.age, self.gender, self.heart, self.blood, self.clst, self.hbit]])
        # tf_p = self.data.predict_proba([[self.age, self.gender, self.heart, self.blood, self.clst, self.hbit]])[:, 1]
        tf_p = self.data.predict_proba([[self.age, self.gender, self.heart, self.blood, self.clst, self.hbit]])[:,0]
        return tf, tf_p

    def create_model(self):
        tf, tf_p = self.into_xgb_model()

        return tf, tf_p