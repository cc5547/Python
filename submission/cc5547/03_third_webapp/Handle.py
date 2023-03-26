import streamlit as st
from DataFrame import CreateDataFrame
from FuncTion import Function
from SideBar import Sidebar
st.set_page_config(
    page_title="My Streamlit App",
    # page_icon=":guardsman:",
    layout="wide",
    # initial_sidebar_state="auto",
)

@st.cache
def get_data():
    # DataFrame.py의 CreateDataFrame 클래스의 create_df()에서 데이터프레임 생성
    df = CreateDataFrame() # 객체 생성
    df = df.create_df()
    return df

def get_sidebar(df):
    # SideBar.py의 Sidebar 클래스의 sidebar()를 통해 사이드바 생성 및 기능 구현
    sb = Sidebar(df) # 객체 생성
    result = sb.create_sidebar()
    return result

def get_function():
    # FuncTion.py의 Function클래스의 ment 받아 오기 // 추후 기능부로 수정하기
    fc = Function() # 객체 생성
    ment = fc.ment()
    return ment

def main() :
    df = get_data()
    result = get_sidebar(df)
    ment = get_function()
    num = list(range(1,6))

    st.title("마싯는 머신러닝")

    # tab, column 생성 
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["1번탭", "2번탭", "3번탭", "4번탭", "5번탭"])
    col1, col2 = st.columns([8, 2])

    with tab1 : st.write(ment, num[0])
    with tab2 : st.write(ment, num[1])
    with tab3 : st.write(ment, num[2])
    with tab4 : st.write(ment, num[3])
    with tab5 : st.write(ment, num[4])

    with col1 :
        # Title
        st.title("컬럼1")
        # Header/Subheader
        st.header("안녕")
        st.subheader("하이")
        # Text
        st.text("여기가 output되는 값 예정")
        st.dataframe(result, width = 1000, height = 500)

    with col2 :
        # Select Box
        st.title("컬럼2")
        
if __name__ == '__main__' :
    main()