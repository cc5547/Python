# streamlit 라이브러리 호출
import streamlit as st
# 수정
# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 나에게 추천하는 유튜브
    ## 나도코딩
    > 이유 : 영상 길이가 짧아 짧게 끊어서 공부하기 좋을 것 같음

     # 남에게 추천하는 유튜브
    ## 생활코딩 
    > 이유 : 썸네일이 깔끔하고 간단명료하여 원하는 정보를 찾기 쉬움


    # 참고 사이트
    *[youtube1](youtube.com/@nadocoding)
    *[youtube2](https://www.youtube.com/@coohde)

    ![이미지에 대한 설명](![이미지에 대한 설명](https://ouch-cdn2.icons8.com/llLHKo43gAdT2ZjeLQl1u4V_Gt5c8h59In2dgFsJXg0/rs:fit:256:256/czM6Ly9pY29uczgu/b3VjaC1wcm9kLmFz/c2V0cy9wbmcvNjY0/LzRiZTZiMzkyLTlk/NWUtNDA2Zi04ZTAx/LWRlODYzMjQ2YzBi/My5wbmc.png))

    """
    # """ """ : 여러 줄을 묶어서 표시할 수 있는 문자열
    # ''' ''' : (통일기능)
)
