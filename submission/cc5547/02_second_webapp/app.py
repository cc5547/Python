import streamlit as st
st.set_page_config(layout="wide")

# 단일 컬럼 생성
col = st.columns(1)

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다. 
tab1, tab2= st.tabs(['Tab_1' , 'Tab_2'])

# 사이드바 생성 : 사이드 바를 s_bar 로 생성.
s_bar = st.sidebar

 # 사진 URL
picture_URL = "https://i.imgur.com/JHLVene.png"

def side_bar(s) :
  # 사이드바
  s.title('여기가 사이드바 입니다.\n 지역(특별시, 광역시, 시 ...)')
  # s.checkbox('체크박스에 표시될 문구입니다.')
  language = ['서울특별시', '인천광역시', '경기도']
  my_choice = st.selectbox('지역 선택', language)

  if my_choice == language[0] :
    st.write('파이썬을 선택하셨습니다.')
  elif my_choice == language[1] :
    st.write('C언어를 선택하셨습니다.')
  elif my_choice == language[2] :
    st.write('자바를 선택하셨습니다')
  else : pass     

def main():
  side_bar(s_bar)

  with col[0] :
    # column 에 담을 내용
    st.title('#지도')
    st.image(picture_URL)

  with tab1 :
    #tab A 를 누르면 표시될 내용
    st.write('안녕하다')

  with tab2 :
    #tab B를 누르면 표시될 내용
    st.write('안녕')

if __name__ == '__main__':
  main()





# with 구문 말고 다르게 사용 가능 
# col1.subheader(' i am column1  subheader !! ')
# col2.checkbox('this is checkbox2 in col2 ') 
#=>위에 with col2: 안의 내용과 같은 기능을합니다

# 컬럼 생성 : 공간을 8:2 으로 분할하여 col1, col2 이름을 가진 컬럼을 생성합니다.  
# col1, col2 = st.columns([8, 2])
 # with col2 :
  #   # column 2 에 담을 내용
  #   st.title('컬럼2')
  #   st.checkbox('컬럼2의 체크박스')






















# streamlit 라이브러리 호출
# 상대경로 복사 : material/02_second_webapp/app.py
# , use_column_width = True << 가운데 정렬
# st.number_input(label, value) << 데이터 입력

# -----------------------------------------------------
# # 은행 이자 계산기
# import streamlit as st
# from PIL import Image
# st.set_page_config(layout="wide")

# def start():
#   start_ment = "# 은행 이자 계산기"
#   picture_URL = "https://i.imgur.com/D7uu8FN.jpg" 
#   st.image(picture_URL, use_column_width = True)
#   st.write(start_ment, use_column_width = True)
#   st.image(picture_URL, use_column_width = True)


# start()

# -----------------------------------------------------



# st.write(
#   start_ment
#   )


# st.image(
#   "https://i.imgur.com/D7uu8FN.jpg", width=800, height= 500)



# 적금 사진 링크

# start_img = "https://i.imgur.com/D7uu8FN.jpg"
# st.image(
#   "https://i.imgur.com/D7uu8FN.jpg"  width="300" height="200"

    
#     use_column_width=True
#     # 유튜브 사진 // "https://blog.kakaocdn.net/dn/JvPqb/btqAiWpd8sf/Ah9IYr6lDRBb8oxSCJYQyK/img.png"
#   )
