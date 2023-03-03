# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 나에게 가장 도움이 될 것 같은 유튜브
    ## 생활코딩
    > 이유 : css나 자바 등 프로그래밍언어 위주의 재생목록이 실력향상에 도움이 된다
    # 다른 학생들에게 가장 도움이 될 것 같은 유튜브
    ## 오늘코드
    > 이유 : 다양한 데이터의 분석, 캐글활용으로 데이터분석가로서의 방향성을 잘 잡아 줄 수 있다
    # 참고 사이트
    * [icons8](https://icons8.com/)
    * [flaticon](https://www.flaticon.com/)
    * [pixabay](https://pixabay.com/ko/)
    """
)

# """ """ : 여러 줄을 묶어서 표시할 수 있는 문자열
# ''' ''' (동일기능)