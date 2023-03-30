import streamlit as st
from Handle import Get
st.set_page_config(page_title="마싯는 머신러닝", layout="wide")

# 사용자가 보는 화면
def user_interface(blood, clst, hbit, gender, heart, age) : 
    if st.button("") : st.image("https://i.imgur.com/4Xd3Mdn.gif", width = 1000)
    
    get = Get()
    
    tf, tf_p = get.get_function(get.get_data(), blood, clst, hbit, gender, heart, age)

    st.title("🦾입력한 정보로 분석한 결과 입니다🦾")
    st.markdown("---")

    col1, col2 = st.columns([3, 7])
    with col1 :
        if tf == 0 : st.write("# 분석 결과 🤦‍♂️ <span style='color:red'>고혈압</span> 🤦‍♂️입니다.", unsafe_allow_html=True)
        elif tf == 1 : st.write("# 분석 결과 😊 <span style='color:blue'>정상</span> 😊입니다.", unsafe_allow_html=True)
        else : pass
        gender = "남자" if gender == 1 else "여자"
        heart = "有" if heart == 0 else "無"
        
        st.write(f"""
            ## 👇분석 결과👇
            ### 👉 성별 : {gender}
            ### 👉 나이 : {age}세
            ### 👉 심장병(有, 無) : {heart}
            ### 👉 혈압 : {blood}mmHg
            ### 👉 콜레스트롤 : {clst}TC
            ### 👉 심박수 : {hbit}bpm
        """)
    st.write(f"""
        ## 결과에 실망하지 마세요😭
        ### 👇확률을 알려드립니다👇
        ### 👉 {', '.join([f'{p*100:.4f}%' for p in tf_p])}
    """)
    with col2 : 
        pass
        
        

        