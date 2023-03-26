import streamlit as st
from DataFrame import CreateDataFrame
from Function import SideBar
st.set_page_config(layout="wide")

def main() :
    # 데이터프레임 생성
    df_loader = CreateDataFrame()
    df = df_loader.create_df()

    # Function.py의 SideBar 클래스를 sb로 접근 // 추후 기능부로 수정하기
    sb = SideBar(df)
    result = sb.sb_function()

    # ment 받아 오기 
    ment = Ment()
    get_ment = sb.ment()

    st.title(get_ment)

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
        st.dataframe(result, width = 1000, height = 500)

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