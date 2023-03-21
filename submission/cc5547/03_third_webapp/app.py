import streamlit as st


def handler():
    name_list = []
    score_list = []

    col1, col2 = st.columns([8, 2])   
    with col1 :
        st.write('이름과 점수를 입력하세요.')
        name = st.text_input('이름')
        score = st.number_input('점수')
        if st.button('추가') :
            name_list.append(name)
            score_list.append(score)
            st.write('이름: {}, 점수: {}'.format(name, score))
    with col2 : 
        if st.button('종료'):
            st.write(f'이름: {name_list[0]}, 점수: {score_list[0]}')

handler()