
import streamlit as st
from Handle import Get
st.set_page_config(page_title="마싯는 머신러닝", layout="wide")

def user_interface(blood, clst, hbit, gender, heart, age) : 
    if st.button("") : st.image("https://i.imgur.com/4Xd3Mdn.gif", width = 1000)
    
    get = Get()
    
    data = get.get_data()
    
    tf, tf_p = get.get_function(data, blood, clst, hbit, gender, heart, age)

    st.title("🦾입력한 정보로 분석한 결과 입니다🦾")
    st.markdown("---")

    col1, col2 = st.columns([3, 7])
    with col1 :
        gender = "남자" if gender == 1 else "여자"
        heart = "有" if heart == 0 else "無"
        
        st.write(f"## 👇분석 결과👇")
        st.write(f"### 👉 성별 : {gender}")
        st.write(f"### 👉 나이 : {age}세")
        st.write(f"### 👉 심장병(有, 無) : {heart}")
        st.write(f"### 👉 혈압 : {blood}mmHg")
        st.write(f"### 👉 콜레스트롤 : {clst}TC")
        st.write(f"### 👉 심박수 : {hbit}bpm")
    with col2 : 
        if tf == 0 : st.write("# 분석 결과 🤦‍♂️ <span style='color:red'>고혈압</span> 🤦‍♂️입니다.", unsafe_allow_html=True)
        elif tf == 1 : st.write("# 분석 결과 😊 <span style='color:blue'>정상</span> 😊입니다.", unsafe_allow_html=True)
        st.write("# 결과에 실망하지 마세요😭")
        st.write("# 👇확률을 알려드립니다👇")
        st.write(f"# 👉 {', '.join([f'{p*100:.4f}%' for p in tf_p])}")

# main 시작점
def main():
    # 사이드바 문진표를 통해 사용자의 정보를 받아온다.
    get = Get()
    blood, clst, hbit, gender, heart, age = get.get_sidebar()

    if age != "" : user_interface(blood, clst, hbit, gender, heart, age)
    else : st.markdown('<a href="https://sparkly-prince-933.notion.site/1ccb865a95e54590bfd61e22b45520fa"><img src="https://i.imgur.com/ktulthH.gif" width=1000></a>', unsafe_allow_html=True)
    
# 메인 실행
if __name__ == '__main__':
    main()

# 노션 옹되 = https://www.notion.so/82e465017bfe45dd82bbf78b46f24469
# 노션 쟂인 = https://sparkly-prince-933.notion.site/1ccb865a95e54590bfd61e22b45520fa
# @st.cache_data