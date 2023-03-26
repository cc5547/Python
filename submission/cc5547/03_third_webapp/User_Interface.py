import streamlit as st
import numpy as np
from DataFrame import CreateDataFrame

st.set_page_config(layout="wide")


def side_bar(df) :
    s = st.sidebar
    s.title('여기가 타이틀')
    area = df['지사명'].unique().tolist()
    choice = s.selectbox('선택', area, index = 10)
    result = df[df['지사명'] == choice]
    result.index = np.arange(1, len(result) + 1)
    return result

def main() :
    df_loader = CreateDataFrame()
    df = df_loader.create_df()
    st.title("마싯는 머신러닝")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["1번탭", "2번탭", "3번탭", "4번탭", "5번탭"])
    col1, col2 = st.columns([8, 2])

    with tab1 :
        st.write("여기가 머신러닝 시각화_1")
    with tab2 :
        st.write("여기가 머신러닝 시각화_2")
    with tab3 :
        st.write("여기가 머신러닝 시각화_3")
    with tab4 :
        st.write("여기가 머신러닝 시각화_4")
    with tab5 :
        st.write("여기가 머신러닝 시각화_5")

    with col1 :
        # Title
        st.title("Hi")
        # Header/Subheader
        st.header("나야")
        st.subheader("하이")
        # Text
        st.text("여기가 output되는 값 예정")
        st.dataframe(side_bar(df), width = 1000, height = 500)

    with col2 :
        # Select Box
        job = st.selectbox("직군을 선택하세요.",
                                    ["Backend Developer",
                                    "Frontend Developer",
                                    "ML Engineer",
                                    "Data Engineer",
                                    "Database Administrator",
                                    "Data Scientist",
                                    "Data Analyst",
                                    "Security Engineer"])
        st.write(f"당신의 직군은 {job}입니다.")

        
if __name__ == '__main__' :
    main()