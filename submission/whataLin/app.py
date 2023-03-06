import streamlit as st
import random

def my_fun():
    st.balloons()
    result=random.choice(range(1,11))
    if result==number:
        st.success(f"당첨입니다! 상금 {prize}원을 받으세요!")
    else:
        st.error(f"아쉽습니다. 낙첨입니다.")
        
    st.info(f"뽑힌 번호는 {result}입니다.")


st.write("함수를 응용해서 페이지 만들어보기")

st.write("# 행운뽑기")

#1-5개까지 살 수 있음
#1-3등까지

#0-9까지 고름
#당첨 시 상금 - 직접 입력
#button - 당첨/낙첨

number=st.selectbox("번호를 골라주세요",list(range(1,11)))
st.write(f"내가 고른 번호 : {number}")

prize=st.slider(
    "당첨 시의 상금을 입력해주세요.",
    1000,
    10000,
    step=100,
)

st.write(f"당첨 시의 상금 : {prize}")

pushed = st.button("당첨 알아보기", on_click=my_fun)
if pushed:
    st.write("버튼이 눌렸습니다.")
