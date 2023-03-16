import streamlit as st
import pandas as pd
import numpy as np

def create_set():
  # 중앙 정렬
  st.set_page_config(layout="wide") 
  # 단일 컬럼 생성
  col = st.columns(1)[0]
  # 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다. 
  tab1, tab2= st.tabs(['Tab_1' , 'Tab_2'])

def create_df():
  # DF_URL
  df_URL = "https://raw.githubusercontent.com/cc5547/Python/main/submission/cc5547/02_second_webapp/%EC%8B%9C%ED%97%98%EC%9E%A5%EC%86%8C_%EA%B0%80%EA%B3%B5%EC%B2%98%EB%A6%AC.csv"
  # df언네임 삭제
  df = pd.read_csv(df_URL).iloc[:, 1:]
  # df인덱스 올림
  df.index += 1


# 사이드바
def side_bar() :
  # 사이드바 생성 : 사이드 바를 s_bar 로 생성.
  s_bar = st.sidebar

  s_bar.title('여기가 사이드바 입니다.\n 지역(특별시, 광역시, 시 ...)')
  area = ['서울특별시', '인천광역시', '경기도']

  choice = s_bar.selectbox('지역 선택', area)

  if choice == area[0] :
    st.write('서울을 선택하셨습니다.')
  elif choice == area[1] :
    st.write('인천광역시를 선택하셨습니다.')
  elif choice == area[2] :
    st.write('경기도를 선택하셨습니다.')
  else : pass
  

def main():
  create_set()
  create_df()
  side_bar()
  with col :
    # column 에 담을 내용
    st.title('# 프레임 결과')
    st.write(df.head(40), width = 5000)
  
  with tab1 :
    # tab1 에 담을 내용
    pass
  with tab2 :
    # tab2 에 담을 내용
    pass

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
