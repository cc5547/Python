# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 나에게 가장 도움이 될 것 같은 유튜브

    ##

    >>이유:

    ## 부족하지만 많이 사랑해주세요!

    # 다른 학생들에게 가장 도움이 될 것 같은 유튜브

    ##

    >>이유:

    * 1$ = 1,300원
    * ^_^
    #나에게 가장 도움이 될 것 같은 유튜브
  ## 빵형의 개발도상국
  > 이유 : 새로운 머신러닝/딥러닝 지식들이 많다
  
  # 다른 학생들에게 가장 도움이 될 것 같은 유튜브
  ## 노마드코더
  > 이유 : 최신 IT 트렌드를 쉽고 재밌게 전달해준다
  #참고사이트
  [icons8](https://icons8.com)
  [flaticon](https://flaticon.com)
  [pixabay](https://pixabay.com)
   
    #### 나에게 가장 도움이 될 것 같은 유튜브
    ### 퇴근후딴짓
    **이유** : 제목이 마음에 듬.
    
    #### 다른 학생들에게 가장 도움이 될 것 같은 유튜브
    ### 드림코딩
    **이유** : 친절.
    
    ![이미지 설명] https://icons8.com/illustrations/illustration/demure-man-programs-on-laptop-while-sitting-in-an-armchair-1
    ![남자] https://icons8.com/illustrations/illustration/demure-man-programs-on-laptop-while-sitting-in-an-armchair-1
    
    """
)

# 숙제
# 유튜브 추천 (for me, for classmate)

# https://pixabay.com/ko
st.image(
    "https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_960_720.jpg"
)
