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
        tf_p = self.data.predict_proba([[self.age, self.gender, self.heart, self.blood, self.clst, self.hbit]])[:, 1]
        return tf, tf_p

    def create_graph(self, tf_p) :
        probabilities = []
        for self.clst in range(self.clst, 150, -1):
            probabilities.append(tf_p)
            if tf_p < 0.5:
                break
        plt.plot(range(self.clst, self.clst-len(probabilities), -1), probabilities)
        plt.xlabel("Cholesterol")
        plt.ylabel("Probability of Heart Disease")
        plt.title("Probability of Heart Disease by Cholesterol Level")

        return plt

    def create_model(self):
        tf, tf_p = self.into_xgb_model()
        graph_1 = self.create_graph(tf_p)

        return tf, tf_p, graph_1

    # from joblib import dump, load
    # import numpy as np
    # import matplotlib.pyplot as plt
    # model1 = load('xgb_model.joblib')
    # age = int(input("나이를 입력하세요: "))
    # sex = bool(input("성별을 입력하세요 (남자: True, 여자: False): "))
    # hs = bool(input("고혈압 여부를 입력하세요 (예: True, 아니오: False): "))
    # bp = int(input("혈압을 입력하세요: "))
    # col = int(input("콜레스테롤 수치를 입력하세요: "))
    # hb = int(input("혈색소 수치를 입력하세요: "))
    # probabilities = []
    # for col_val in range(col, 150, -1):
    #     prob = model1.predict_proba([[age, sex, hs, bp, col_val, hb]])[:, 1]
    #     probabilities.append(prob)
    #     if prob < 0.5:
    #         break
    # plt.plot(range(col, col-len(probabilities), -1), probabilities)
    # plt.xlabel("Cholesterol")
    # plt.ylabel("Probability of Heart Disease")
    # plt.title("Probability of Heart Disease by Cholesterol Level")
    # plt.show()