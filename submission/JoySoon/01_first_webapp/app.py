# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 나에게 가장
    ## 도움이 될 것 같은 유튜브
    ![](https://ouch-cdn2.icons8.com/8FMlpaAfpOBUuTXT0v_3h0-C-UslBKs-XAf_Ql0y6us/rs:fit:256:309/czM6Ly9pY29uczgu/b3VjaC1wcm9kLmFz/c2V0cy9wbmcvNTI4/L2ZhYTU5MzcyLTA5/YjctNGU0OC1hM2Jh/LTg1YzIwNzg2ZWI5/NC5wbmc.png)
    ---
    *노마드코더*
    ---
    > 이유 : 주로 개발시장에 현황에 대해 소신 발언이 많은 편이며
    자칫 어려운 코딩 내용들을 쉬운 말로 풀어내서 이야기하기 때문에 
    나같은 입문자들에게 개발시장의 현황에 대해서 알 수 있었다.
    ### 최신 댓글 반응
    | 댓글러 | 내용 |
    |:----:|:----:|
    |   한*   | 현직 플러터 개발자입니다 플러터에 대해 잘 정리해주셔서 감사합니다 이 영상을 통해서 플러터 시장이 많이 발전했음 좋겠네요 ! |
    |   -**   | 리액트 네이티브에서 왜 플러터로 넘어가게 되었는지 니꼬쌤의 개인적인 견해도 들어간 설명이 있으면 좋을거 같습니다 :) |


    # 다른 학생들에게 가장 
    ## 도움이 될 것 같은 유튜브
    ![](https://ouch-cdn2.icons8.com/SaA2mPHCnnMuPfAaLtPt7s-AFaV8S9zJzIfT3DJPpA4/rs:fit:256:290/czM6Ly9pY29uczgu/b3VjaC1wcm9kLmFz/c2V0cy9wbmcvOTE3/L2NiOTE0NTFkLTI4/NjMtNGVhMy04MDNj/LWE2ZTJmNDJlMDJk/OS5wbmc.png)
    ---
    *나도 코딩*
    ---
    > 이유 : 주로 고퀄리티 기초 무료 강좌들을 업로드하지만
    가끔씩 개발자로써의 조언과 재밌는 심심풀이 영상을 올리기 때문에
    다양한 재미를 느낄 수 있는 채널이다.

    ### 최신 댓글 반응
    | 댓글러 | 내용 |
    |:----:|:----:|
    |   김*   | 훌륭한 강의 정말 감사드립니다. 이틀동안 4시간씩 공부하면서 기본편 완강했습니다. 바로 심화편 결재하러 갑니다. 지금 이순간 너무 신나고 행복합니다. 적절한 비유와 예시, 표준어, 좋은 중저음의 목소리, 공백없는 마이크, 완벽한 편집으로 집중력 1도 잃지 않고 정주행할 수 있었습니다. 가장 감사드리는 부분은 저의 시간을 아껴주셨단 겁니다. ㅠㅠ 단 8시간 30분 정도만에 ... 감사합니다. |
    |   이**   | html, css, javascript, react를 배우고 backend 공부를 하고 싶어 java 입문을 찾던 중에 이 강의를 발견하게 되었는데 너무 잘 이해되고 아주 좋은 강의였습니다. 확실히 한가지 프로그래밍 언어를 알고 배우는게 훨씬 이해가 빠르긴 하네요 감사합니다. |


    ## 참고사이트
    * [icons8](http://icons8.com)
    * [flaticon](http://flaticon.com)
    * [pixabay](http://pixabay.com)

    """
)

# """ """ : 여러 줄을 묶어서 표시할 수 있는 문자열
# ''' ''' (동일 기능)