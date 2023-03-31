import streamlit as st
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="마싯는 머신러닝", layout="wide")

# main 시작점
def main():
    # 사이드바 내용 시작점 ---------------------------------------------------------
    sb = st.sidebar
    gender_choice = ['남자', '여자']
    yes_no = ['예', '아니요']

    sb.title('문진표를 작성해 주세요👇')
    # int(blood), int(clst), int(hbit), float(gender), int(heart), float(age)
    blood = sb.slider('혈압을 입력해주세요.', 90, 200, 1)
    clst = sb.slider('콜레스트롤을 입력하세요.', 120, 564, 1)
    hbit = sb.slider('심박수를 입력하세요', 70, 202, 1)

    gender = sb.radio('성별을 선택 해주세요.', gender_choice)
    if gender == gender_choice[0] : gender = 1  
    else : gender = 0

    heart = sb.radio('심장병이 있습니까?', yes_no)
    if heart == yes_no[0] : heart = 1  
    else : heart = 0

    age = sb.text_input('나이를 입력해 주세요.')
    # 사이드바 내용 끝점 ---------------------------------------------------------


    # 잡립 끌어오고 계산까지 시작 점 -----------------------------------------------
    data = joblib.load("submission/cc5547/03_third_webapp/xgb_model.joblib")
    # tf = data.predict([[age, gender, heart, blood, clst, hbit]])
    # tf_p = data.predict_proba([[age, gender, heart, blood, clst, hbit]])[:,0]
    tf = data.predict([[float(age), float(gender), int(heart), int(blood), int(clst), int(hbit)]])
    tf_p = data.predict_proba([[float(age), float(gender), int(heart), int(blood), int(clst), int(hbit)]])[:, 0]
    # tf_p = data.predict_proba([[float(age), float(gender), int(heart), int(blood), int(clst), int(hbit)]])[:, 1]
    # 잡립 끌어오고 계산까지 끝 점 -------------------------------------------------


    # 그래프 만들기 --------------------------------------------------------------
    probabilities = []
    for clst in range(clst, 150, -1): 
        prob = tf_p
        # prob = data.predict_proba([[float(age), float(gender), int(heart), int(blood), int(clst), int(hbit)]])[:,0]
        # prob = data.predict_proba([[float(age), float(gender), int(heart), int(blood), int(clst), int(hbit)]])[:, 1]
        probabilities.append(prob)
        if prob < 0.5 : 
            break

    fig, ax = plt.subplots() 
    
    ax.plot(range(clst, clst-len(probabilities), -1), probabilities)
    ax.set_xlabel("Cholesterol")
    ax.set_ylabel("Probability of Heart Disease")
    ax.set_title("Probability of Heart Disease by Cholesterol Level")
    # fig가 그래프를 담고 있음
    # 그래프 만들기 --------------------------------------------------------------


    # 사용자 UI 시작 -------------------------------------------------------------
    st.title("🦾입력한 정보로 분석한 결과 입니다🦾")
    st.markdown("---")
    col1, col2 = st.columns([4, 6])
    with col1 :
        if tf == 0 : st.write("""
                                # 분석 결과 
                                # 🤦‍♂️ <span style='color:red'>고혈압</span> 🤦‍♂️입니다. """, unsafe_allow_html=True)
        elif tf == 1 : st.write("""
                                # 분석 결과 
                                # 😊 <span style='color:blue'>정상</span> 😊입니다. """, unsafe_allow_html=True)
        else : pass
        gender = "남자" if gender == 1 else "여자"
        heart = "有" if heart == 1 else "無"
        
        st.write(f"""
                ## 👇분석 결과👇
                ### 👉 성별 : {gender}
                ### 👉 나이 : {age}세
                ### 👉 심장병(有, 無) : {heart}
                ### 👉 혈압 : {blood}mmHg
                ### 👉 콜레스트롤 : {clst}TC
                ### 👉 심박수 : {hbit}bpm """)
        st.write(f"""
                ## 결과에 실망하지 마세요😭
                ### 👉확률을 알려드립니다 👉 {', '.join([f'{p*100:.4f}%' for p in tf_p])} """)

    with col2 : st.pyplot(fig)
    # 사용자 UI 끝 -------------------------------------------------------------

# 메인 실행
if __name__ == '__main__':
    main()