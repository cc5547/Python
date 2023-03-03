# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    ### 나에게 가장 도움이 될 것 같은 유튜브 :blush:
    #### **생활코딩**
    > 이유 : 썸네일이 깔끔해서 보고싶은 동영상을 잘 찾아볼 수 있을 것 같다.\n
    > [생활코딩 채널 바로가기](https://www.youtube.com/@coohde)

    ---

    ### 다른 학생들에게 가장 도움이 될 것 같은 유튜브 :satisfied:
    #### **노마드코더**
    > 이유 : 유명한 채널이고 코딩말고도 개발자들을 위한 팁들도 있어서 유용할 것 같다.\n
    > [노마드코더 채널 바로가기](https://www.youtube.com/@nomadcoders)

    ---
    
    ##### 참고 사이트
    * [icons8](https://icons8.com/)
    * [flaticon](https://www.flaticon.com/)
    * [pixabay](https://pixabay.com/)
    """
)

# """ """ : 여러 줄을 묶어서 표시할 수 있는 문자열
# ''' ''' (동일가능)