import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

class Function:
    def __init__(self, data, blood, clst, hbit, gender, heart, age) -> None:
        self.data = data
        self.blood = blood
        self.clst = clst
        self.hbit = hbit
        self.gender = gender
        self.heart = heart
        self.age = age
        
    def create_model(self):
        # 나이, 성별, 심장병, 혈압, 콜레스테롤, 최대심박수
        tf = self.data.predict([[self.age, self.gender, self.heart, self.blood, self.clst, self.hbit]])
        tf_p = self.data.predict_proba([[self.age, self.gender, self.heart, self.blood, self.clst, self.hbit]])[:,0]
        # tf_p = self.data.predict_proba([[self.age, self.gender, self.heart, self.blood, self.clst, self.hbit]])[:, 1]
        return tf, tf_p

    def create_graph(self) :
        # prob = self.data.predict_proba([[self.age, self.gender, self.heart, self.blood, self.clst, self.hbit]])[:, 1]
        
        probabilities = []

        for self.clst in range(self.clst, 150, -1):
            # prob = self.data.predict_proba([[self.age, self.gender, self.heart, self.blood, self.clst, self.hbit]])[:, 1]
            prob = self.data.predict_proba([[self.age, self.gender, self.heart, self.blood, self.clst, self.hbit]])[:,0]
            probabilities.append(prob)
            if prob < 0.5:
                break
        fig, ax = plt.subplots()
        ax.plot(range(self.clst, self.clst-len(probabilities), -1), probabilities)
        ax.set_xlabel("Cholesterol")
        ax.set_ylabel("Probability of Heart Disease")
        ax.set_title("Probability of Heart Disease by Cholesterol Level")

        return fig

    # handle에서 밑 함수를 통하여 클래스 내부 함수를 한번에 다 호출
    def result_model(self) : 
        tf, tf_p = self.create_model()
        graph = self.create_graph()
        return tf, tf_p, graph