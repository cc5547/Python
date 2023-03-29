import streamlit as st
import UI
from Handle import Get

# main 시작점
def main():
    # 사이드바 문진표를 통해 사용자의 정보를 받아온다.
    get = Get()
    blood, clst, hbit, gender, heart, age = get.get_sidebar()

    # 사이드바에서 마지막 나이를 받을때 ""이 아니라면 UI.user_interface() 실행
    if age != "" : 
        UI.user_interface(blood, clst, hbit, gender, heart, age)
    else : 
        # ""이라면 톱니바퀴
        st.markdown('<a href="https://sparkly-prince-933.notion.site/1ccb865a95e54590bfd61e22b45520fa"><img src="https://i.imgur.com/ktulthH.gif" width=1000></a>', unsafe_allow_html=True)
    
# 메인 실행
if __name__ == '__main__':
    main()

# 노션 옹되 = https://www.notion.so/82e465017bfe45dd82bbf78b46f24469
# 노션 쟂인 = https://sparkly-prince-933.notion.site/1ccb865a95e54590bfd61e22b45520fa
# @st.cache_data