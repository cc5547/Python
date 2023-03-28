import streamlit as st
import requests
from PIL import Image
from io import BytesIO
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

def user_interface(result):

    st.title("신도시에서 살아남기............")
    col1, col2 = st.columns([5, 5])
    with col1 :
        # Title
        st.title("컬럼1")
        # Header
        st.header("안녕")
        # Subheader
        st.subheader("하이")
        # Text
        st.text("여기가 output되는 값 예정")
        # DF
        st.write(result)

    with col2 :
        st.write("컬럼2")


# main 시작점 최대한 간단하게 짜기. 
def main() :
    # 객체 return 받기
    df = get_data()
    result, on_off = get_sidebar(df)
    ment = get_function()

    if on_off is True :
        user_interface(result)
    else : 
        # response = requests.get('https://github.com/cc5547/Python/blob/main/submission/cc5547/03_third_webapp/%EA%B3%A0%EC%96%91%EC%9D%B4.gif')
        # img = Image.open(BytesIO(response.content))
        st.image("https://github.com/cc5547/Python/blob/main/submission/cc5547/03_third_webapp/%EA%B3%A0%EC%96%91%EC%9D%B4.gif", width=1000)
        
        

# 메인 실행
if __name__ == '__main__' :
    main()