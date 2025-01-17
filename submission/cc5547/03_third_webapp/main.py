import streamlit as st
import UI
import Handle
img_url = '<a href="https://sparkly-prince-933.notion.site/1ccb865a95e54590bfd61e22b45520fa"><img src="https://i.imgur.com/ktulthH.gif" width=1200></a>'

# main 시작점
def main():
    blood, clst, hbit, gender, heart, age = Handle.get_sidebar()
    
    if age != "" :
        UI.user_interface(blood, clst, hbit, gender, heart, age)  
    else : 
        st.markdown(img_url, unsafe_allow_html=True)
    
# 메인 실행
if __name__ == '__main__':
    main()

# 노션 옹되 = https://www.notion.so/82e465017bfe45dd82bbf78b46f24469
# 노션 쟂인 = https://sparkly-prince-933.notion.site/1ccb865a95e54590bfd61e22b45520fa
# @st.cache_data