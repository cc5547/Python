import streamlit as st

#셀렉박스

st.write("""## 어떤 유튜브 채널을 알아볼까?""")
whichChannel=[None,"나에게 가장 도움이 될 것 같은 유튜브", "다른 학생들에게 가장 도움이 될 것 같은 유튜브"]
my_choice = st.selectbox('선택하세요', whichChannel)


if my_choice==whichChannel[1]:
    st.write(

    """

    ### 나에게 가장 도움이 될 것 같은 유튜브
    ##### 노마드코더
    ![유튜브 이미지](https://yt3.googleusercontent.com/ytc/AL5GRJWCKbcOn_YX6jhiTrNoYBV3pg0eWu41jb2zpkXHjA=s88-c-k-c0x00ffffff-no-rj)
    [link](https://www.youtube.com/@nomadcoders)

    > 이유: 최신 IT 경향을 파악할 수 있음

    """
    )


if my_choice==whichChannel[2]:
    st.write(

    """
    ### 다른 학생들에게 가장 도움이 될 것 같은 유튜브
    ##### 나도코딩
    ![유튜브 이미지](https://yt3.googleusercontent.com/ytc/AL5GRJVI23E18Rn0Ha_MfPZoybsD2_J8Uy73pEqmoSvvfA=s88-c-k-c0x00ffffff-no-rj)
    [link](https://www.youtube.com/@nadocoding)

    > 이유 : 프로그래밍을 전혀 모르는 입문자도 알아들을 수 있는 쉬운 설명

    """
    )
