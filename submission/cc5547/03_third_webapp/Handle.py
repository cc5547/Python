import streamlit as st
from Data import CreateData
from FuncTion import Function
from SideBar import Sidebar
st.set_page_config(page_title="마싯는 머신러닝", layout="wide")

# DataFrame.py의 CreateDataFrame 클래스의 create_df()에서 데이터프레임 생성
# @st.cache_data
def get_data():
    dt = CreateData()  # 객체 생성
    data = dt.create_data()
    return data

# SideBar.py의 Sidebar 클래스의 sidebar()를 통해 사이드바 생성 및 기능 구현
def get_sidebar():
    sb = Sidebar()  # 객체 생성
    result = sb.result_sidebar()
    return result

# FuncTion.py의 Function클래스의 ment 받아 오기 // 추후 기능부로 수정하기
def get_function(data, blood, clst, hbit, gender, heart, age):
    fc = Function(data, int(blood), int(clst), int(hbit), float(gender), int(heart), float(age))  # 객체 생성 타입 형변환
    result = fc.create_model()
    return result

def user_interface(blood, clst, hbit, gender, heart, age): 
    data = get_data()
    tf, tf_p = get_function(data, blood, clst, hbit, gender, heart, age)

    st.title("🦾입력한 정보로 분석한 결과 입니다🦾")
    st.markdown("---")
    col1, col2 = st.columns([3, 7])
    tab1, tab2 = st.tabs(['탭_1_그래프_1' , '탭_2_그래프_2'])   
    with col1 :
        gender = "남자" if gender == 1 else "여자"
        heart = "有" if heart == 1 else "無"
        
        st.write(f"## 👇분석 결과👇")
        st.write(f"### 성별 : {gender}")
        st.write(f"### 나이 : {age}세")
        st.write(f"### 심장병(有, 無) : {heart}")
        st.write(f"### 혈압 : {blood}mmHg")
        st.write(f"### 콜레스트롤 : {clst}TC")
        st.write(f"### 심박수 : {hbit}bpm")
    with col2 : 
        with tab1 :
            pass
        with tab2 :
            pass
    st.markdown("---")
    if tf == 1 : st.write("# 분석 결과 -> <span style='color:red'>고혈압</span> 입니다.", unsafe_allow_html=True)
    elif tf == 0 : st.write("# 분석 결과 -> <span style='color:blue'>정상</span> 입니다.", unsafe_allow_html=True)
    # st.write(f"# 당신 죽을 확률{tf_p}")
    st.write(f"# 당신 죽을 확률 {', '.join(str(p) for p in tf_p).04f * 100}")

# main 시작점
def main():
    # 사이드바 문진표를 통해 사용자의 정보를 받아온다.
    blood, clst, hbit, gender, heart, age = get_sidebar()

    if age != "" : user_interface(blood, clst, hbit, gender, heart, age)
    else : st.markdown('<a href="https://www.notion.so/82e465017bfe45dd82bbf78b46f24469"><img src="https://i.imgur.com/ktulthH.gif" width=1000></a>', unsafe_allow_html=True)
# 메인 실행
if __name__ == '__main__':
    main()