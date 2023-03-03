# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 나에게 가장 도움이 될 것 같은 영상
    ## 프로그래머 김플 스튜디오
    > 이유: 파이썬 복습에 좋은 자료들입니다.

    
    # 다른 사람들에게 도움이 될 것 같은 영상
    ## 코딩애플
    > 이유: 짧은 영상 길이와 간단한 설명으로 예습과 복습이 용이할 것 같다. 

    # 참고 사이트
    * [icons8](https://icons8.com/)
    * [flaticon](https://www.flaticon.com/)
    * [pixabay](https://pixabay.com/ko/)

    """
)
