import streamlit as st

# 이름과 점수를 저장할 리스트를 생성합니다.
name_list = []
score_list = []
# 입력 폼을 생성합니다.
st.write('이름과 점수를 입력하세요.')
name = st.text_input('이름')
score = st.number_input('점수')
# '추가' 버튼을 누르면 입력받은 값을 리스트에 추가합니다.
if st.button('추가'):
    # name_list.append(name)
    # score_list.append(score)
    st.write('이름: {}, 점수: {}'.format(name, score))
    # 추가한 값을 리스트에 출력합니다.
    # st.write('이름 리스트: {}'.format(name_list))
    # st.write('점수 리스트: {}'.format(score_list))
# '종료' 버튼을 누르면 리스트를 출력합니다.
if st.button('종료'):
    name_list.append(name)
    score_list.append(score)
    st.write('이름 리스트: {}'.format(name_list))
    st.write('점수 리스트: {}'.format(score_list))









def handler():
    name_list = []
    score_list = []

    name = st.text_input
    return pass

handler()