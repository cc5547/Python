# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
       ## # 나에게 가장 도움이 될 것 같은 유튜브
    ## 오늘코드###
    > 이유 : 데이터분석에 관한 영상들이 많다
    # 다른 학생들에게 가장 도움이 될 것 같은 유튜브
    ## 김플 스튜디오
    > 이유 : short로 만든 컨텐츠와 다양한 예제가 존재한다.
    # 참고 사이트####
    * [icons8](https://icons8.com/)
    * [flaticon](https://www.flaticon.com/)
    * [pixabay](https://pixabay.com/ko/)
    """
)

# """ """ : 여러 줄을 묶어서 표시할 수 있는 문자열
# ''' ''' (동일기능)