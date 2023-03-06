# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    ---
    ## 나에게 가장 도움이 될 것 같은 유튜브

    > 노마드코더 :smiley:

    [![이미지 설명](https://i.ytimg.com/vi/Cnbmrh99c1o/hqdefault.jpg)](https://www.youtube.com/@nomadcoders)

    이유: `영어`로 IT지식을 배울수 있어서
  

    ~~영어공부해야겠다는 생각이 듦~~

    ---

    ## 다른 학생들에게 가장 도움이 될 것 같은 유튜브

    > 드림코딩 :wink:

    [![이미지 설명](https://i.ytimg.com/vi/TTLHd3IyErM/hqdefault.jpg)](https://www.youtube.com/@dream-coding)

    이유: 웹개발 프론트엔드의 `기초`부터 `심화`까지 배울 수 있음
    

    ~~웹 개발 공부 지옥에 발 담근..~~

    ---

  ### 참고사이트
  + [icons8](https://icons8.com)
  + [flaticon](https://flaticon.com)
  + [pixabay](https://pixabay.com)
  

    """
)

option1 = st.selectbox(
    '코딩 유튜브 리스트',
    ('생활코딩', '드림코딩', '노마드코더','조코딩','코딩애플'))

st.write('You selected:', option1)

html1 = """
    <head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
    </head>
    <button type="button" class="btn btn-primary">바로가기</button>
"""

st.markdown(html1, unsafe_allow_html=True)

st.write(
  """
  ---
  """
)
option2 = st.selectbox(
    '데이터엔지니어링 유튜브 리스트',
    ('빵', '퇴근후딴짓', '메타코드M','혁펜하임','오늘코드'))

st.write('You selected:', option2)

html2 = """
    <head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
    </head>
    <button type="button" class="btn btn-warning">바로가기</button>
"""

st.markdown(html2, unsafe_allow_html=True)