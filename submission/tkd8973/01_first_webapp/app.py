# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # DAY1
    ## 알아두면 유용한 Colab-PYTHON 단축키
    > alt + shift + ↑↓ : 같은 코드 복붙 
    
    > shift + home, end : 현재 위치에서 앞,뒤로 드래그

    > 실행 : ctrl+enter, 셀추가 : alt+enter

    > a,b = divmod(c,d) : c를 d로 나누었을때 몫과 나머지

    > ctrl + m + m : 코드셀 -> 텍스트셀

    > ctrl + m + y : 텍스트셀 -> 코드셀

    > ctrl + m + a : 현재 셀 기준 위로 코드셀 생성

    > ctrl + m + b : 현재 셀 기준 아래에 코드셀 생성

    > ctrl + m + t : 현재 셀 기준 아래에 텍스트셀 생성

    ---
    ## 나에게 가장 도움이 될 것 같은 유튜브
    ### [혁펜하임](https://www.youtube.com/@hyukppen)
    > 머신러닝, 딥러닝에 대한 기초 수학과 tensorflow, pytorch 등 머신러닝 플랫폼 사용법을 알 수 있고, 더 깊은 지식을 쌓을 수 있기 때문이다

    ## 다른 학생들에게 가장 도움이 될 것 같은 유튜브
    ### [조코딩](https://www.youtube.com/@jocoding)
    > 입문자를 위한 기초 코딩 뿐만 아니라 빠른 개발자 트렌드 변화에 맞춰 OpenAI와 최신 트렌드 내용들을 커뮤니티에 업로드 해주기 때문에 코딩에 익숙하지 않은 사람들도 편안하게 볼 수 있다.

    ---
    ## 참고 사이트
    * [icons8](https://icons8.com/)
    * [flaticon](https://www.flaticon.com/)
    * [pixabay](https://pixabay.com/ko/)

    ---

    """
)
