# streamlit 라이브러리 호출
import streamlit as st
#
# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 장우혁 공부방  *Since 2023-02-27*
    ---

    * |링크 모음|
      |-|
      |[수업 자료 링크](https://the-fat-cat.notion.site/26-ef748e37e6fa4dfc821ce8972dd9c5fe)|
      |[slack 링크](https://app.slack.com/client/T04NR00MM5F/C04NC7H3K0B/rimeto_profile/U04QX4NB2PR)|
      |[마크다운 링크](https://the-fat-cat.notion.site/Markdown-42c07b9f12be439c9d6a9f1a240ade4b)|
      |[Github](https://github.com/woohyukjang)|
      |[구글](https://google.com)|
      |[챗 GPT](https://chat.openai.com/chat)|




    * ###### 내가 들어야 할 강의

     >[나도코딩](https://www.youtube.com/watch?v=kWiCuklohdY&t=10s) 
    
     >[혁펜하임](https://www.youtube.com/@hyukppen)



     듣다 손놓은 6시간 강의 완강하자





    * ###### 내가 추천하는 강의

     >[혁펜하임](https://www.youtube.com/@hyukppen)

     머신러닝 이론을 정말 잘 설명해 주심
    
    




    * ###### 참고 사이트
     * [icons8](https://icons8.com)
     * [flation](https://flaticon.com)
     * [pixabay](https://pixabay.com/ko/)


    """
)

# https://pixabay.com/ko
st.image(
    "https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_960_720.jpg"
)
