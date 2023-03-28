import streamlit as st
# import imageio
# import requests
# from io import BytesIO
# from PIL import Image
from DataFrame import CreateDataFrame
from FuncTion import Function
from SideBar import Sidebar

st.set_page_config(page_title="마싯는 머신러닝", layout="wide")


 # DataFrame.py의 CreateDataFrame 클래스의 create_df()에서 데이터프레임 생성
@st.cache_data
def get_data():
    df = CreateDataFrame() # 객체 생성
    df = df.create_df()
    return df

# SideBar.py의 Sidebar 클래스의 sidebar()를 통해 사이드바 생성 및 기능 구현
def get_sidebar(df):
    sb = Sidebar(df) # 객체 생성
    result = sb.result_sidebar()
    return result

# FuncTion.py의 Function클래스의 ment 받아 오기 // 추후 기능부로 수정하기
def get_function():
    fc = Function() # 객체 생성
    ment = fc.ment()
    return ment

def user_interface(age, sex):
    st.title("신도시에서 살아남기............")

    col1, col2 = st.columns([5, 5])

    with col1 :
        # Title
        st.write(f"나이는 {age}입니다.")
        st.write(f"성별은 {sex}입니다.")
        

    with col2 :
        st.write("컬럼2")


# main 시작점 최대한 간단하게 짜기. 
def main() :
    # 객체 return 받기
    df = get_data()

    age, sex = get_sidebar(df)
    
    ment = get_function()

    if age == None : st.write("대기중")
    else : user_interface(age, sex)

    # if on_off is True :
    #     user_interface(name, age)
    # else : 
    #     img = "https://i.imgur.com/GoeOLuK.gif"
    #     st.image(img, width=1000)
        
        

# 메인 실행
if __name__ == '__main__' :
    main()