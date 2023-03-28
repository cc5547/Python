import streamlit as st
from Data import CreateData
from FuncTion import Function
from SideBar import Sidebar

st.set_page_config(page_title="마싯는 머신러닝", layout="wide")


# DataFrame.py의 CreateDataFrame 클래스의 create_df()에서 데이터프레임 생성
@st.cache_data
def get_data():
    df = CreateData()  # 객체 생성
    df = df.create_d()
    return df

# SideBar.py의 Sidebar 클래스의 sidebar()를 통해 사이드바 생성 및 기능 구현
def get_sidebar():
    sb = Sidebar()  # 객체 생성
    result = sb.result_sidebar()
    return result


# FuncTion.py의 Function클래스의 ment 받아 오기 // 추후 기능부로 수정하기
def get_function():
    fc = Function()  # 객체 생성
    ment = fc.ment()
    return ment


def user_interface(blood, clst, hbit, gender, heart, age):
    st.title(":smile: 입력한 정보로 분석한 결과 입니다. :smile:")
    col1, col2 = st.columns([5, 5])

    gender = "남자" if gender == 1 else "여자"
    heart = "유" if heart else "무"
        
    with col1:
        # Title
        st.write(f"나이는 {age}세 입니다.")
        st.write(f"성별은 {gender} 입니다.")
        st.write(f"심장질환 유뮤 : {heart}")
        st.write(f"혈압 : {blood}")
        st.write(f"콜레스트롤 : {clst}")
        st.write(f"심박수 : {hbit}")

    with col2:
        st.write("컬럼2")


# main 시작점 최대한 간단하게 짜기.
def main():
    data = get_data()
    st.write(type(data))

    blood, clst, hbit, gender, heart, age = get_sidebar()
    ment = get_function()

    if age != "" : user_interface(blood, clst, hbit, gender, heart, age)
    else : 
        img = "https://i.imgur.com/rDN49gl.gif"
        st.image(img, width = 1000)

# 메인 실행
if __name__ == '__main__':
    main()